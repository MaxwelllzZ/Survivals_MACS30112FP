"""
This file is to clean and organize all hotel reviews data.
This file needs to import review_cleaning.py which contain cleaning functions for every hotel.

Note: This file cannot be ran due to difficulty in uploading all original
datasets for each hotel.
"""
import review_cleaning
import pandas as pd

def all_hotels_review(h_directory, recheck_data, hotel_dfs, query_df, cleaned_lst):
    """
    The function is to clean all reviews data for all hotels and concatenate all
    data into one dataframe.

    input:
        h_directory(str): location of hotel data + common part of all hotel names
        recheck_data(list): reviews data that need extra handling or cannot be used
        hotel_dfs(list): all cleaned hotel reviews dataframe
        query_df(dataframe): df includes querylink column
        cleaned_lst(list): check whether cleaned data in right formats
    """
    for j in range(0, 382):
        output_dir = h_directory + str(j)
        d, output_dir = review_cleaning.all_hotels_data_clean(output_dir)
        final_d = review_cleaning.scrape_data_clean(output_dir, d, recheck_data)
        if final_d is not None:
            final_d["rev_index"] = j
            final_d["hotelQuery"] = query_df.iloc[j,8]
            cleaned_lst.append(final_d.shape)
            hotel_dfs.append(final_d)
        else:
            print(output_dir)

    combined_df = pd.concat(hotel_dfs, ignore_index=True)
    columns_to_check = ['publishedAtDate', 'title', 'address', 'city',
                        'state', 'totalScore', 'reviewsCount']
    combined_df_final = combined_df.drop_duplicates(subset=columns_to_check,
                                                    keep='first')
    return combined_df_final

cleaned_lst = []
hotel_dfs = []
recheck_data = []
h_directory = "/Users/joycepeiting/Desktop/final_project/data/hotel"
rev = pd.read_csv("~/Desktop/final_project/rev.csv", index_col= 0)
combined_df_final = all_hotels_review(h_directory, recheck_data, hotel_dfs, rev)
combined_df_final.to_csv("combinedhotelreviews.csv")
