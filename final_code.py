# Importing necesseary libraries
import csv
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from linearmodels.panel import PanelOLS

# Concatenate Datasets Part
hotel_2301 = 'Data/HOTEL_2023_01to11/Hotel_data2023/HOT2301.CSV'
hotel_2302 = 'Data/HOTEL_2023_01to11/Hotel_data2023/HOT2302.CSV'
hotel_2303 = 'Data/HOTEL_2023_01to11/Hotel_data2023/HOT2303.CSV'
hotel_2304 = 'Data/HOTEL_2023_01to11/Hotel_data2023/HOT2304.CSV'
hotel_2305 = 'Data/HOTEL_2023_01to11/Hotel_data2023/HOT2305.CSV'
hotel_2306 = 'Data/HOTEL_2023_01to11/Hotel_data2023/HOT2306.CSV'
hotel_2307 = 'Data/HOTEL_2023_01to11/Hotel_data2023/HOT2307.CSV'
hotel_2308 = 'Data/HOTEL_2023_01to11/Hotel_data2023/HOT2308.CSV'
hotel_2309 = 'Data/HOTEL_2023_01to11/Hotel_data2023/HOT2309.CSV'
hotel_2310 = 'Data/HOTEL_2023_01to11/Hotel_data2023/HOT2310.CSV'
hotel_2311 = 'Data/HOTEL_2023_01to11/Hotel_data2023/HOT2311.CSV'

file_paths_2023 = [hotel_2301, hotel_2302, hotel_2303, hotel_2304,\
              hotel_2305, hotel_2306, hotel_2307, hotel_2308,\
              hotel_2309, hotel_2310, hotel_2311]
# append data from Jan 2023 to Nov 2023
dfs = []

headers = [
    "Taxpayer_Number", "Taxpayer_Name", "Taxpayer_Address", "Taxpayer_City",
    "Taxpayer_State","Taxpayer_Zip", "Taxpayer_County", "Taxpayer_Phone",
    "Location_Number", "Location_Name", "Location_Address", "Location_City",
    "Location_State", "Location_Zip", "Location_County","Location_Phone",
    "Unit_Capacity", "Responsibility_Begin_Date_(YYYYMMDD)",
    "Responsibility_End_Date_(YYYYMMDD)", "Obligation_End_Date_(YYYYMMDD)",
    "Filer_Type", "Total_Room_Receipts", "Taxable_Receipts"
]

# Using for loop to contcatenate monthly dataset into one 2023 dataset
for file in file_paths_2023:
    try:
        df = pd.read_csv(file, names=headers, header=None, encoding='ISO-8859-1')  # or 'latin1' or 'windows-1252'
        dfs.append(df)
    except UnicodeDecodeError as e:
        print(f"Error reading {file}: {e}")

# Make sure dataset structure stays align
hotel_2023 = pd.concat(dfs, ignore_index=True)

# Pulling needed annual tax report
hotel_2021_path = 'Data/HOTEL2021/HOTEL2021.CSV'
hotel_2022_path = 'Data/HOTEL2022/HOTEL2022.CSV'

# Updated has 2021 to 2023
file_path_21_to_22= [hotel_2021_path, hotel_2022_path]

# Data type specification for zip codes as strings
dtype_spec = {'Taxpayer_Zip': str, 'Location_Zip': str}

# Function to clean zip codes
def clean_zip_code(zip_code):
    clean_zip = ''.join(filter(str.isdigit, str(zip_code)))
    return clean_zip[:5] if len(clean_zip) >= 5 else None

# Concatenate dfs
df1s = []
for file in file_path_21_to_22:
    try:
        # Adding low_memory=False parameter
        df = pd.read_csv(file, names=headers, header=None, encoding='ISO-8859-1', dtype=dtype_spec, low_memory=False)
        # Clean Location_Zip
        df['Location_Zip'] = df['Location_Zip'].apply(clean_zip_code)
        df = df[df['Location_Zip'].str.isnumeric()]  # Filter only numeric zips
        df1s.append(df)
    except UnicodeDecodeError as e:
        print(f"Error reading {file}: {e}")

hotel_21_to_22 = pd.concat(df1s, ignore_index=True)

hotel_21_to_Nov23 = pd.concat([hotel_21_to_22, hotel_2023], ignore_index=True)

Dallas = hotel_21_to_Nov23[hotel_21_to_Nov23['Location_City'].str.contains('DALLAS')]

# Keep filtering hotel which still are in the market, delete the ones which has value in Responsibility_End_Date
# Filter the DataFrame to keep only rows where the 'Responsibility End Date (YYYYMMDD)' column is an empty string after stripping white spaces
Dallas_active_hotels = Dallas[Dallas['Responsibility_End_Date_(YYYYMMDD)'].str.strip() == '']

# Overwrite Dallas dataset to keep cleaning
Dallas = Dallas_active_hotels

unique_payer = len(set(Dallas['Taxpayer_Number']))

# Drop duplicate rows based on the specified columns
unique_locations = Dallas.drop_duplicates(subset=['Location_Number', 'Location_Name', 'Location_Address','Location_County'])

# Reset the index to ensure it starts from 0
unique_locations.reset_index(drop=True, inplace=True)

# Add a new column 'Location_ID' with incremental values starting from 1
unique_locations['Location_ID'] = range(1, len(unique_locations) + 1)

# Get the number of unique locations
num_unique_locations = unique_locations.shape[0]

# Merge the original Dallas DataFrame with the unique_locations to include the Location_ID
Dallas_with_ID = Dallas.merge(unique_locations[['Location_Number', 'Location_Name', 'Location_Address', 'Location_County', 'Location_ID']],
                              on=['Location_Number', 'Location_Name', 'Location_Address', 'Location_County'],
                              how='left')

# Sort dataset by Location_ID and Obligation_End_Date_(YYYYMMDD)
Dallas_with_ID_sorted = Dallas_with_ID.sort_values(by=['Location_ID', 'Obligation_End_Date_(YYYYMMDD)'])

Dallas_with_ID_sorted.to_csv("Dallas_with_ID.csv",index=False, header=False)

# Cleaning Tax Government Data Part is Done, output is Dallas_with_ID dataset


# *************************************




# *************************************

# Regressions Part
# Loading dataset
df_path = 'cleaned_final_ver4.csv' # 这两行基于需求考虑是否被120-125中间的code 代替
df =  pd.read_csv(df_path, encoding='ISO-8859-1')
df = df.dropna(subset=['additionalInfo'])
# Drop the ones have problems with calculating ratings
df.drop(index=[1856, 1857, 1858, 4239, 4240, 4241, 4242, 4243, 4244], inplace=True)
df["additionalInfo"] = df["additionalInfo"].apply(lambda x: eval(x))
df = df[df["additionalInfo"].apply(lambda x: "Amenities" in x.keys())]

# New additional information
n = df["additionalInfo"].apply(lambda x: x["Amenities"])
n = n.apply(lambda i: {k: v for d in i for k, v in d.items()})
df["freeWifi"] = n.apply(lambda i: i.get("Free Wi-Fi", None))
df["freeBreakfast"] = n.apply(lambda i: i.get("Free breakfast", None))
df["freeParking"] = n.apply(lambda i: i.get("Free parking", None))
df["pool"] = n.apply(lambda i: i.get("Pool", None))
df["restaurant"] = n.apply(lambda i: i.get("Restaurant", None))
df["fitnessCenter"] = n.apply(lambda i: i.get("Fitness center", None))

none_counts = {
    "freeWifi": df["freeWifi"].isna().sum(),
    "freeBreakfast": df["freeBreakfast"].isna().sum(),
    "freeParking": df["freeParking"].isna().sum(),
    "pool": df["pool"].isna().sum(),
    "restaurant": df["restaurant"].isna().sum(),
    "fitnessCenter": df["fitnessCenter"].isna().sum()
}
print(none_counts)

# Select observations which have revnue at that time period
df = df[df["TotalRoomReceipts"] != 0]
df['revenue'] =  np.log(df['TotalRoomReceipts']+1)
by_hotel = df['hotelid']

# Convert 'PublishedAtDate' to datetime format
df['publishedAtDate'] = pd.to_datetime(df['publishedAtDate'])

# Create entity and time indices
df = df.set_index(['hotelid', 'publishedAtDate'])

# Create Threshold for later regressions
df['T'] = (df['actual_stars'] < df['present_stars']).astype(int)
actual_rating = df['actual_stars']


# OLS Regressions
# Function to perform OLS regression and print the summary
def perform_ols(formula, data):
    model = ols(formula, data=data).fit()
    print(model.summary())

# Regression 1
perform_ols("revenue ~ present_stars", df)

# Regression 2
perform_ols("revenue ~ present_stars + hotelStars + C(publishedAtDate)", df)

# Regression 3
perform_ols("revenue ~ present_stars + C(fitnessCenter) + C(restaurant) + C(freeWifi) + C(publishedAtDate)", df)

# Regression Discontinuity
#3 kinds: 0.025, 0.02, 0.05(all data, which is df itself)
def perform_rd_analysis(data, bandwidth, formula):
    # Filter the data based on the specified bandwidth
    df_rd = data[abs(data['actual_stars'] - data['present_stars']) <= bandwidth]

    # Perform OLS regression
    model = ols(formula, data=df_rd).fit()
    print(f"Regression Discontinuity Analysis for Bandwidth: {bandwidth}")
    print(model.summary())

# With different bandwidths and formulas
# Functions of formula = 'revenue ~ T + actual_stars + C(hotelStars) + C(publishedAtDate)'
# RD Analysis for Bandwidth 0.025
perform_rd_analysis(df, 0.025, "revenue ~ T + actual_stars + C(hotelStars) + C(publishedAtDate)")
# RD Analysis for Bandwidth 0.02
perform_rd_analysis(df, 0.02, "revenue ~ T + actual_stars + C(hotelStars) + C(publishedAtDate)")
# RD Analysis for Bandwidth 0.05
perform_rd_analysis(df, 0.05, "revenue ~ T + actual_stars + C(hotelStars) + C(publishedAtDate)")

# Functions of formula = 'revenue ~ T + actual_stars + C(fitnessCenter) + C(restaurant) + C(freeWifi) + C(publishedAtDate)'
# 3 Amenities features
# RD Analysis for Bandwidth 0.025
perform_rd_analysis(df, 0.025, "revenue ~ T + actual_stars + C(fitnessCenter) + C(restaurant) + C(freeWifi) + C(publishedAtDate)")
# RD Analysis for Bandwidth 0.02
perform_rd_analysis(df, 0.02, "revenue ~ T + actual_stars + C(fitnessCenter) + C(restaurant) + C(freeWifi) + C(publishedAtDate)")
# RD Analysis for Bandwidth 0.05
perform_rd_analysis(df, 0.05, "revenue ~ T + actual_stars + C(fitnessCenter) + C(restaurant) + C(freeWifi) + C(publishedAtDate)")

#heterogeneous
#reviewContained 0-10, 10-20, etc
# Version of using ols
def PO_run_regression_for_review_contained_ranges(formula, data, lower_bound, upper_bound):
    # Filter the data based on the specified range of reviewContained
    df_filtered = data[(data['reviewContained'] >= lower_bound) & (data['reviewContained'] < upper_bound)]
    # Performing OLS regression
    model = ols(formula, data=df_filtered).fit()
    print(f"PanelOLS Regression for reviewContained range {lower_bound}-{upper_bound}")
    print(model.summary())

PO_run_regression_for_review_contained_ranges('revenue ~ T + rating + reviewContained + rating:reviewContained', df, 0, 10)
PO_run_regression_for_review_contained_ranges('revenue ~ T + rating + reviewContained + rating:reviewContained', df, 0, 20)

# Version of using PanelOls
def run_regression_for_reviewContained_range(formula, data, lower_bound, upper_bound):
    # Filter the data based on the specified range of reviewContained
    df_filtered = data[(data['reviewContained'] >= lower_bound) & (data['reviewContained'] < upper_bound)]
    model = PanelOLS.from_formula(formula, data=df_filtered)
    results = model.fit()

    # Print the summary of the regression results
    print(f"OLS Regression Results for reviewContained Range {lower_bound}-{upper_bound}")
    print(results)

# Example usage of the function
run_regression_for_reviewContained_range('revenue ~ T + rating + reviewContained + rating:reviewContained + EntityEffects + TimeEffects', df, 0, 10)
run_regression_for_reviewContained_range('revenue ~ T + rating + reviewContained + rating:reviewContained + EntityEffects + TimeEffects', df, 10, 20)