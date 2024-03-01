# Importing necesseary libraries
import csv
import pandas as pd
import numpy as np
import statsmodels.api as sm
from linearmodels.panel import PanelOLS
import matplotlib.pyplot as plt

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
file_path_17_to_22= [hotel_2021_path, hotel_2022_path]


# Data type specification for zip codes as strings
dtype_spec = {'Taxpayer_Zip': str, 'Location_Zip': str}

# Function to clean zip codes
def clean_zip_code(zip_code):
    clean_zip = ''.join(filter(str.isdigit, str(zip_code)))
    return clean_zip[:5] if len(clean_zip) >= 5 else None



df1s = []

for file in file_path_17_to_22:
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
df_path = 'cleaned_final_ver2.csv' # 这两行基于需求考虑是否被120-125中间的code 代替
df =  pd.read_csv(df_path, encoding='ISO-8859-1')

# Cleaning
df.drop(index=1844, inplace=True)
df.drop(index=4230, inplace=True)

# Select observations which have revnue at that time period
df = df[df["TotalRoomReceipts"] != 0]

# Setting up variables for future regressions
df['revenue'] =  np.log(df['TotalRoomReceipts']+1)
rating = df['present_stars']
by_hotel = df['hotelid']

# Convert 'PublishedAtDate' to datetime format
df['publishedAtDate'] = pd.to_datetime(df['publishedAtDate'])

# Create entity and time indices
df = df.set_index(['hotelid', 'publishedAtDate'])

# Create Threshold for later regressions
df['T'] = (df['actual_stars'] < df['present_stars']).astype(int)
actual_rating = df['actual_stars']

# Regressions results will be shown below
def run_regression(formula, data, regression_number):
    # Define the model
    model = PanelOLS.from_formula(formula, data)

    # Fit the model
    results = model.fit()

    # Print the summary of the regression results
    print(f"Regression {regression_number} Results")
    print("=" * 80)
    print(results)

# 1st regression, use run_regression function
run_regression('revenue ~ rating', df, 1)

# 2nd regression
run_regression('revenue ~ rating + EntityEffects + TimeEffects', df, 2)

# 3rd regression
run_regression('revenue ~ T + actual_rating + EntityEffects + TimeEffects', df, 3)

# 4th regression (with interaction term)
run_regression('revenue ~ T + rating + reviewLength + rating:reviewLength + EntityEffects + TimeEffects', df, 4)

# 5th regression (with another interaction term)
run_regression('revenue ~ T + rating + reviewContained + rating:reviewContained + EntityEffects + TimeEffects', df, 5)