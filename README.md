<<<<<<< HEAD

# Survivals_MACS30112 Final Project: The Effect of Google Customer Ratings on Dallas Hotels' Revenue


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


## Overview of final_code.py
- The most important thing to note in github is final_code.py. The main logic of this file is as following:
  - Data Concatenation: The script processes and concatenates multiple CSV files containing hotel data from January to November 2023. These files are concatenated to form a comprehensive dataset for analysis.
  - Data Cleaning and Preparation: The code include steps to clean and prepare the data for analysis. This could involve handling missing values, converting data types, and merging the original Dallas DataFrame with the unique_locations to include the Location_ID.
  - Statistical Modeling: Utilizing statsmodels and linearmodels.panel to examine the impact of customer reviews on hotel revenues, among other analyses.
  - Data Visualization: With matplotlib, the script likely generates plots and charts to visualize the findings from the statistical analysis, providing insights into the data and model results.
   - Output Generation: The final part of the script might involve generating output files or summaries of the analyses, including saving visualizations, exporting results to CSV files, or printing summaries to the console.


## Team Members & Responsibilities
- All team members are responsible for slides
- Joyce Fu: Web Scraping Google Reviews Data, Cleaning Google Reviews Data, Presentation
- Shuyi Zhang: Web Scraping Google Reviews Data, Data Visualization
- Sitong Zhang: Cleaning Hotel Revenue Data, Model Estimation, Presentation
- Guanhong Liu: Data Analysis, Data Visualization, Presentation


## Links
- link to in-class presentation slides:
- link to uodated presentation slides:
- link to video:
>>>>>>> 63423e2c644a7301a55108c999737e32a09278f7
