# Survivals_MACS30112 Final Project: The Effect of Google Customer Ratings on Dallas Hotels' Revenue


## Project Goals
The Survivals group's project aims to investigate the reputational and signaling effects of customer reviews on online platforms, specifically focusing on their impact on Dallas hotel revenues. Specifically, we will answer the following **research questions**:
- Do customer ratings affect Texas hotel revenues?
- How do online customer ratings influence Dallas hotel revenues through signal or reputation channels
- How great are the reputational effects and signaling effects?


## Data Sources
- Dallas Hotel Tax Receipts: Monthly occupancy tax data from the Texas government for hotels in Dallas, covering January 2021 to November 2023. The dataset can be directly downloaded from the Texas Comptroller of Public Accounts (https://data-secure.comptroller.texas.gov/main/files/public-files).

- Google Reviews: Data scraped from Google Reviews, including hotel names, addresses, ratings, and reviews per month, for the same period.


## Required Libraries and Version Numbers
This project requires the following Python libraries:

- pandas (2.1.4): for data manipulation and analysis
- numpy (1.26.3): for numerical calculations
- matplotlib (3.8.0): for plotting graphs
- seaborn (0.13.2): for making statistical graphics.
- BeautifulSoup (4.12.2): for web scraping Google Reviews data 检查一下用没有用！
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
