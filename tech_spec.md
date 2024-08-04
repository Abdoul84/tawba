# Tech Spec for "TAWBA" Project

## Project Overview
"TAWBA" is a web portal providing dynamic reports and dashboards for analyzing and predicting Senegal's development. The focus will be on GDP and key human development indicators.

## Data Sources
1. **World Bank GDP Data**
2. **IMF GDP Data**
3. **HDRO Human Development Data**

## Data Pipeline
1. **Data Collection**
   - **World Bank GDP Data**: API to fetch GDP data.
   - **IMF GDP Data**: API to fetch GDP data.
   - **HDRO Data**: API to fetch human development indicators.

2. **Data Cleaning and Processing**
   - Convert data types.
   - Handle missing values.
   - Ensure data consistency and remove duplicates.

3. **Storage**
   - Raw data: `../data/raw/`
   - Processed data: `../data/processed/`

## Analysis and Visualization
1. **Total Amount per Sector**
   - Bar chart showing total funds allocated to different sectors.

2. **Number of Projects per Status**
   - Pie chart showing the distribution of project statuses (Approved, Ongoing, etc.).

3. **GDP and Human Development Indicators**
   - Trends and correlations between GDP and human development indicators.

## Tools and Libraries
1. **Python**
   - `pandas` for data manipulation.
   - `requests` for API calls.
   - `matplotlib` for visualizations.

2. **Version Control**
   - Git and GitHub for version control and collaboration.

## Next Steps
1. **Set Up Data Pipeline**
   - Write scripts to fetch and process data from World Bank, IMF, and HDRO.

2. **Run Initial Analysis**
   - Load processed data and create initial visualizations.

3. **Develop Dashboard**
   - Integrate visualizations into a web dashboard.
