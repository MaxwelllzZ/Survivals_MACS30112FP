"""
Scrape hotel reviews on Google Maps using Google Maps Review Scraper on Apify

This file is to scrape hotel review data. The procedure proceeds as follows:
1. Generating hotel query link for actor to scrape 
2. Scrape reviews for each hotel

Note: The api-key has been hidden. The codes cannot be ran without apify account.
Users also need to download apify_client package.
"""

import json
import pandas as pd
from apify_client import ApifyClient
import query_generation

# generate query link based on hotel with data in 2023 Quarter4 (latest data)
rev = pd.read_excel("~/Desktop/final_project/hotel_revenue_23q4.xlsx",
                    usecols="J:N,Q,T,V")
rev = query_generation.querylink(rev)
rev["map_search_url"] = "https://google.com/maps/search/" + rev["hotel_query"]
rev = rev.sort_values("Unit_Capacity", ascending=False,ignore_index=True)
rev.drop(rev[rev["Total_Room_Receipts"] == 0].index, inplace=True)
print(len(rev))

rev.to_csv('/Users/joycepeiting/Desktop/final_project/hotel_scrape_list.csv',
           index=False)

# api_key can be attained on Apify website
client = ApifyClient("api_key")
def hotel_review_scrap(url, output_dir):
    """
    This function calls actor to scrape hotel reviews based on url provided and
    save scraped data in output_dir provided.

    input:
        url(string): url (query link) to be scraped
        output_dir(string): directory to save data

    """
    # Prepare the Actor input
    run_input = {
        "startUrls": [{ "url": url }],
        "maxReviews": 1000,
        "reviewsSort": "newest",
        "language": "en",
        "personalData": False,
    }

    # Run the Actor
    run = client.actor("compass/Google-Maps-Reviews-Scraper").call(
        run_input=run_input)
    dataset_items = ApifyClient.dataset(client, run['defaultDatasetId']
                                        ).list_items().items

    # Write into json file
    with open(output_dir, 'w') as f:
        json.dump(dataset_items, f)

# Run for all hotels
j = 0
scraped_lst = []
pass_lst = []
p_directory = "/Users/joycepeiting/Desktop/final_project/hotel"
for i in rev["map_search_url"]:
    output_dir = p_directory + str(j)
    try:
        hotel_review_scrap(i, output_dir)
    except:
        pass_lst.append(i)
        pass
    j+=1