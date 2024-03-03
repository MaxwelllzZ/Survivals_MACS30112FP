"""
This file is to clean reviews data for each hotel.
This file is imported in hotelreview_cleaning.py
The cleaning steps include:
1. Check hotel reviews are rightly scrapped
2. Basic cleaning
3. Convert to monthly data
3. Caculate review length, counts
4. Recover actual rating and observed rating
"""
import pandas as pd
import numpy as np

def all_hotels_data_clean(json_file):
    """
    Read hotel reviews data (json file)

    input:
        json_file(str): data directory
    output:
        json_file(str): data directory
        hotel_scraped(df): original hotel reviews data
    """
    hotel_scraped = pd.read_json(json_file)
    return hotel_scraped, json_file

def scrape_data_clean(json_file, hotel_scraped, recheck_data):
    """
    Check whether abnormality exists in reviews data.
    If not, clean hotel reviews data.

    input:
        json_file(str): data directory
        hotel_scraped(df): original hotel reviews data
        recheck_data(list): saving data directory for abnormal reviews data
    output:
        hotel_monthly_data(df): final cleaned
    """
    try:
        _ = hotel_scraped[["title", "address"]]
    except KeyError:
        print("Scrap Failed")
        recheck_data.append(json_file)
        return None

    if len(hotel_scraped["title"].unique()) != 1 or len(hotel_scraped["address"].unique()) != 1:
        print("Check: Multiple hotels being scrapped")
        recheck_data.append(json_file)
        return None
    else:
        hotel = hotel_data_cleaning(json_file, hotel_scraped, recheck_data)
        if hotel is None:
            return None
        else:
            return hotel_monthly_data(hotel)

def hotel_data_cleaning(json_file, hotel_scraped, recheck_data):
    """
    Basic Cleaning before converting to monthly data.

    input:
        json_file(str): data directory
        hotel_scraped(df): original hotel reviews data
        recheck_data(list): saving data directory for abnormal reviews data
    output:
        hotel(df): df being cleaned (first stage)
    """
    try:
        hotel = hotel_scraped[["title", "address", "city", "state", "totalScore",
                            "reviewsCount", "reviewsDistribution", "hotelStars",
                            "url", "text", "publishedAtDate", "stars", "rating",'additionalInfo']]

    except KeyError:
        print("Lacking Column")
        recheck_data.append(json_file)
        return None

    date_revision = pd.to_datetime(hotel["publishedAtDate"]).copy()
    hotel.loc[:, "publishedAtDate"] = date_revision.dt.strftime("%Y%m")
    hotel = hotel.dropna(subset="stars")

    hotel["reviewLength"] = hotel["text"].apply(lambda i: len(i) if i else 0)
    hotel["reviewContained"] = hotel["text"].apply(lambda i: 1 if i else 0)
    return hotel

def hotel_monthly_data(hotel):
    """
    Recover actual rating, observed rating, review count, review length
    for each month, convert the rating records df to monthly data.

    input:
        hotel(df): df being cleaned (first stage)
        recheck_data(list): saving data directory for abnormal reviews data
    output:
        hotel_monthly(df): final data for each hotel
    """
    # group data by month
    attributes_list = ["title", "address", "city", "state", "totalScore", "additionalInfo",
                    "reviewsCount", "reviewsDistribution", "hotelStars", "url"]
    d = {i: 'first' for i in attributes_list}
    d.update({"stars":sum,"reviewContained":sum, "reviewLength":np.mean})
    hotel_monthly = hotel.groupby(["publishedAtDate"], as_index=False).agg(d)
    hotel_monthly['ratingContained'] = hotel.groupby(
        ["publishedAtDate"]).size().values
    hotel_monthly['ratingContained'].sum()

    # calculate actual rating, observed rating, review counts
    assert list(hotel_monthly["reviewsDistribution"][0].keys()) == \
        ['oneStar', 'twoStar', 'threeStar', 'fourStar', 'fiveStar'],\
            "Wrong Distribution"
    rating_sum = 0
    count = 0
    for i, c in enumerate(hotel_monthly["reviewsDistribution"][0].values()):
        rating_sum += (i+1)*c
        count += c
    act_rating = rating_sum/count
    hotel_monthly["actualRating"] = act_rating
    rev_count = hotel_monthly["reviewsCount"][0]
    hotel_monthly = hotel_monthly.sort_values(
        "publishedAtDate",ascending=False).reset_index(drop=True)
    rr_cumsum = hotel_monthly["reviewsCount"] - \
        hotel_monthly["ratingContained"].cumsum()
    hotel_monthly["ratingReviewCumSum"] = rr_cumsum
    review_cumsum = hotel_monthly["reviewsCount"] - \
        hotel_monthly["reviewContained"].cumsum()
    hotel_monthly["reviewCumSum"] = [rev_count] + list(review_cumsum)[:-1]
    act_rating_monthly = (hotel_monthly["reviewsCount"]*act_rating - \
                        hotel_monthly["stars"].cumsum())/hotel_monthly["ratingReviewCumSum"]
    hotel_monthly["ratingReviewCumSum"] = [rev_count] + \
    list(hotel_monthly["ratingReviewCumSum"])[:-1]

    hotel_monthly['actual_stars'] = [act_rating] + list(act_rating_monthly)[:-1]
    hotel_monthly['present_stars'] = round(hotel_monthly['actual_stars'], 1)

    # leave data in the timespan of research
    hotel_monthly = hotel_monthly[
        (hotel_monthly["publishedAtDate"] <= "202311") & \
        (hotel_monthly["publishedAtDate"] >= "202101")].reset_index(drop=True)

    # fill lacking months to ensure data being cleaned correctly
    if hotel_monthly.shape[0] != 35:
        hotel_monthly.set_index("publishedAtDate", inplace=True)
        months = pd.date_range(start="2021-01", end="2023-11", freq="MS")
        m_index = [m.strftime("%Y%m") for m in months]
        hotel_monthly = hotel_monthly.reindex(m_index)
        hotel_monthly = hotel_monthly.ffill()
        hotel_monthly.reset_index(inplace=True)

    return hotel_monthly
