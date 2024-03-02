<<<<<<< HEAD
# Survivals_MACS30112 Final Project: The Effect of Google Customer Ratings on Dallas Hotels' Revenue


## Project Description
The Survivals group's project aims to find empirical support for the mechanism of the effects of online reviews on firm performance, this project builds on reputation theories. In reputation theories, customers form belief or learn from experience to observe product quality. There are two effects of reviews/ratings on firm performance: 1) reputational effect and 2) signaling effect. Reputation effect is one company is incentivized to build reputation to set higher prices or increase customer loyalty and purchases to gain more profits. Signaling effect is the reviews/ratings can implicate product quality, reducing the probability of adverse selection/information asymmetry.
]Specifically, our group focused customer reviews of online platforms on Dallas hotel revenues. Specifically, we will answer the following **research questions**:

- Do customer ratings affect Texas hotel revenues?
- How do online customer ratings influence Dallas hotel revenues through signal or reputation channels
- How great are the reputational effects and signaling effects?
  
We target the hotel industry for several reasons. First, for hotels, a kind of experience goods, reviews are important quality indicators affecting consumers’ buying decisions. With higher ratings or more positive reviews (eWOM effect), hotels build better reputations, make more revenues with more customer visits. Also, chain hotels have taken a substantial amount of market shares. Chained-brand hotels with good reputations may have possible moral hazard problems as they share mutual reputation and some of them may be free-riders and put less effort on maintaining good qualities. If online reviews are effective signal and reputation building channels, then the moral hazard problems can be reduced. The empirical mechanisms being explored can demonstrate how online platforms with online reviews affect the hotel industry and be a reference for managerial decisions of hotels and evaluation of the rating/review system of hotel review platforms. We chose Dallas as our target city as according to the American tourist, Dallas is one of the most visited tourist cities. More than 22 million people visit Dallas every year, spending $6 billion and generating a total economic impact of $9.6 billion. These travelers support the hotel industry.

**The relavance of this study** cannot be overstated, particularly in an era where digital platforms have become the foundation of consumer decision-making. Hotels, like many other service-oriented businesses, rely heavily on online reviews. These reviews not only serve as social proof, but also as a signaling mechanism that can enhance or harm a hotel's reputation. Understanding the dynamics is critical for organizations to effectively manage their online reputation and use consumer input to optimize revenue.

To investigate the links between online ratings, review counts, and hotel profits, the project employed a robust **methodological framework**, utilizing a mix of quantitative data analysis and statistical modeling. To estimate the effects of customer ratings (independent variable) on hotel revenues (dependent variable), our group adopted the fixed effect regression model to control for unobservable variables that vary across entities and time, and also adopted the regression discontinuity model to do a supplementary analysis. To examine whether the magnitude of the effect changes with the number of online reviews, we drew an OLS table to see if the coefficient of customer ratings strictly increases with the number of online reviews.

Our project has the following **key findings**:
- Rating has positive effect on revenue.
- Signal Effect (Threshold presence) has negative effect on revenue.
- Google threshold is smaller than Yelp. Their actual ratings is very close to present ratings.
- Rating itself is insufficient. Review Count matters.



## Data Sources
- Dallas Hotel Tax Receipts: Monthly occupancy tax data from the Texas government for hotels in Dallas, covering January 2021 to November 2023. The dataset can be directly downloaded from the Texas Comptroller of Public Accounts (https://data-secure.comptroller.texas.gov/main/files/public-files).

- Google Reviews: Data is scraped from Google Reviews, including hotel names, addresses, ratings, and reviews per month, for the same period.


## Overall Findings
- Rating has positive effect on revenue.
- Signal Effect(Threshold presence) has negative effect on revenue.
- Google threshold is smaller than Yelp. Their actual ratings is very close to present ratings.
- Rating itself is insufficient. Review Count matters.


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
- Joyce Fu: Web Scraping Google Reviews Data, Model Estimation
- Shuyi Zhang: Web Scraping Google Reviews Data, Data Visualization
- Sitong Zhang: Data Cleaning, Data Processing
- Guanhong Liu: Data Analysis, Data Visualization


## Links
- link to in-class presentation slides:
- link to uodated presentation slides:
- link to video:
>>>>>>> 63423e2c644a7301a55108c999737e32a09278f7
