<<<<<<< HEAD

# Survivals_MACS30112 Final Project: The effect of Google customer ratings on Dallas hotels’ revenue


## Project Description
The Survivals group's project aims to provide empirical support for the mechanism of the effects of online ratings on firm revenue, this project builds on reputation theories. In reputation theories, there are two effects of reviews/ratings on firm performance: 1) reputational effect and 2) signaling effect. Reputation effect is company is incentivized to build reputation to set higher prices or increase customer loyalty and purchases to gain more profits; thus reducing moral hazard problems. Signaling effect is the reviews/ratings are signals implicating product quality, reducing the probability of adverse selection/information asymmetry. Our group focused the effect of customer ratings on Google on Dallas hotel revenues. Specifically, we will answer the following ***research questions***: 

- Do customer ratings affect Dallas hotel revenues?
- How do ratings influence hotel revenues, through signal or reputation channels?
- Are there heterogeneous effects due to hotel reviews?

We target the hotel industry for several reasons. First, for hotels, a kind of experience goods, reviews are important quality indicators affecting consumers’ buying decisions, shaping customers' perspectives to hotels. Also, chain hotels have taken a substantial amount of market shares. Chained-brand hotels with good reputations may have possible moral hazard problems as they share mutual reputation and some of them may be free-riders and put less effort on maintaining good qualities. If online reviews are effective signal and reputation building channels, then the moral hazard problems can be reduced. The empirical mechanisms being explored can demonstrate how online platforms with online reviews affect the hotel industry and be a reference for managerial decisions of hotels and evaluation of the rating/review system of hotel review platforms. As the Texas hotel revenue data is the only accessible revenue data, we chose Dallas as our target city as according to the American tourist, Dallas is one of the most visited tourist cities in the US. More than 22 million people visit Dallas every year, spending $6 billion and generating a total economic impact of $9.6 billion. Also, more than one-third of hotels in Dallas are chain-affiliated. Thus, the project results may be generalized to other big cities such as NY, LA, etc.

Using hotel revenue data from the Texas government and hotel reviews data scraped from Google Maps using Apify, we investigate the effect of online ratings on hotel profits and employed 3-part analysis. We first adopted OLS with hotel characteristics control variables and fixed effect regression model to estimate the effects of customer ratings on hotel revenues. Next, to decompose signal effect from reputational effect, we adopted the regression discontinuity model, utilizing threshold set by the Google rating system. Finally, to examine the heterogenous effects due to online reviews, we further included online reviews variables in OLS estimation beyond models in part1.

Our project has the following ***key findings***:
- Rating has positive effect on revenue.
- Signal effect (Threshold presence) has negative or insignificant positive effect on revenue. The results are sensitive to choices of bandwidths.
- Google threshold is smaller than other rating platforms (Yelp, Tripadvisor, etc). Their actual ratings is very close to present ratings.
- Both ratings and reviews positively affect hotel revenue.

## Data Sources
- Dallas Hotel Tax Receipts: Monthly occupancy tax data from the Texas government for hotels in Dallas, covering January 2021 to November 2023. The dataset can be directly downloaded from the Texas Comptroller of Public Accounts (https://data-secure.comptroller.texas.gov/main/files/public-files).

- Google Reviews: Data is scraped from Google Maps Reviews using Apify, including hotel names, addresses, ratings, and reviews. (https://apify.com/compass/google-maps-reviews-scraper)


## Required Libraries and Version Numbers
This project requires the following Python libraries:

- pandas (2.1.4): for data manipulation and analysis
- numpy (1.26.3): for numerical calculations
- matplotlib (3.8.0): for plotting graphs
- seaborn (0.13.2): for making statistical graphics
- statsmodels (0.14.1): for statistical models
- linearmodels (5.4): for panel data models
- apify_client (1.6.3): for working with the Apify API to scrape web data

The specific version numbers for these libraries will ensure compatibility and reproducibility of the project's results.


## How to Run the Software
1. Ensure all required libraries are installed. You can install them using pip:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn beautifulsoup4
```

2. Clone the project repository from GitHub:
```bash
git clone https://github.com/MaxwelllzZ/Survivals_MACS30112FP
```

3. Navigate to the project directory
```bash
cd Survivals_MACS30112FP
```

4. Run the main project script
```bash
python final_code.py
```


## Structure of the Files
- Data
  - Data folder contains information (CSV files) of the hotel's tax information which are downloaded from Taxas government-related websites. The datasets have info from Jan 2021 to Sep 2023
- DataCleaning
  - In this folder, there are relevant cleaned CSV files using IPYNB files.
  - We used hotelrevenue.ipynb file to output Dallas_with_ID.csv.
  - We used hotelreview_cleaning.py to output combinedhotelreviews.csv. review_cleaning.py is used to contain functions used in hotelreview_cleaning.py to clean reviews data for each hotel.
  - We used merge_finaldata.ipynb to output cleaned_final.csv.
- DataCollection
  -  query_generation.py provides function to scrape the information and form them as a query.
  -  hotelreview_scraping.py is the file we used to scrape data from the web.
  -  hotel_revenue_23q4.xlsx is used to calibrate and obtain the final list of hotels across the datasets.
- DataAnalysis
  -  summary_stat_visualization.ipynb contains the visualizations for the cleaned_final.csv. It has distributino graphs, statistics, and graph of relationship between revenue and observed rating, etc.
  -  regression_analysis contains the estimation strategies we used for the cleaned_final.csv. There are multiple regression models used. Fixed effect, necessary dummies, interaction terms are included
- READ.ME
  -  This file.



## Team Members & Responsibilities
- All team members are responsible for slides
- Joyce Fu: Web Scraping Google Reviews Data, Cleaning Google Reviews Data, Presentation
- Shuyi Zhang: Web Scraping Google Reviews Data, Data Visualization
- Sitong Zhang: Cleaning Hotel Revenue Data, Model Estimation, Presentation
- Guanhong Liu: Data Analysis, Data Visualization, Presentation


## Links
- link to in-class presentation slides: https://docs.google.com/presentation/d/1D-oqwv20HpieeWVBs7Tvtis7JcCGzB67PGVg6JB_NME/edit?usp=sharing
- link to updated presentation slides: https://docs.google.com/presentation/d/1ea_9mrO6-Vtf1EiDFohD78guCcHMBsf9/edit#slide=id.p1
- link to video: https://drive.google.com/file/d/1AUGA9E-5cmu-Ahrh3nu26id2G7I3Qk1H/view?usp=sharing
>>>>>>> 63423e2c644a7301a55108c999737e32a09278f7
