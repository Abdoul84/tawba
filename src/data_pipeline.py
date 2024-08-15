import os
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Create directories for raw and processed data if they don't exist
os.makedirs('../data/raw', exist_ok=True)
os.makedirs('../data/processed', exist_ok=True)

# API key for HDRO Data API
HDRO_API_KEY = 'HDR-PAZVKzfcEOhHxPHMFkkzi4WyAbtTasB6'  # Replace with your actual API key

def download_world_bank_gdp_data():
    WORLD_BANK_API_URL = 'http://api.worldbank.org/v2/country/SN/indicator/NY.GDP.MKTP.CD'
    params = {'format': 'json', 'per_page': 1000}
    response = requests.get(WORLD_BANK_API_URL, params=params)
    data = response.json()
    records = [{'Year': entry['date'], 'GDP': entry['value']} for entry in data[1]]
    df = pd.DataFrame(records)
    raw_data_path = '../data/raw/world_bank_gdp_data.csv'
    df.to_csv(raw_data_path, index=False)
    df.fillna(method='ffill', inplace=True)
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    df.drop_duplicates(inplace=True)
    processed_data_path = '../data/processed/cleaned_world_bank_gdp_data.csv'
    df.to_csv(processed_data_path, index=False)
    print(f"GDP data from World Bank cleaned and saved to {processed_data_path}")

# def download_imf_gdp_data():
#     IMF_API_URL = 'https://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/Q.SN.NGDP_R'
#     params = {'startPeriod': '2000', 'endPeriod': '2024'}

#     # Setup retry strategy
#     retry_strategy = Retry(
#         total=5,
#         backoff_factor=1,
#         status_forcelist=[429, 500, 502, 503, 504],
#         allowed_methods=["HEAD", "GET", "OPTIONS"]
#     )
#     adapter = HTTPAdapter(max_retries=retry_strategy)
#     http = requests.Session()
#     http.mount("https://", adapter)
#     http.mount("http://", adapter)

#     try:
#         response = http.get(IMF_API_URL, params=params, timeout=20)
#         response.raise_for_status()
#         data = response.json()
#         records = [{'Year': entry['@TIME_PERIOD'], 'GDP': entry['@OBS_VALUE']} for entry in data['CompactData']['DataSet']['Series']['Obs']]
#         df = pd.DataFrame(records)
#         raw_data_path = '../data/raw/imf_gdp_data.csv'
#         df.to_csv(raw_data_path, index=False)
#         df.fillna(method='ffill', inplace=True)
#         df['Year'] = pd.to_datetime(df['Year'], format='%Y')
#         df.drop_duplicates(inplace=True)
#         processed_data_path = '../data/processed/cleaned_imf_gdp_data.csv'
#         df.to_csv(processed_data_path, index=False)
#         print(f"GDP data from IMF cleaned and saved to {processed_data_path}")
#     except requests.exceptions.RequestException as e:
#         print(f"Failed to download IMF GDP data: {e}")

def download_hdro_data():
    HDRO_API_URL = 'https://hdrdata.org/api/CompositeIndices/query'
    params = {
        'apikey': HDRO_API_KEY,
        'countryOrAggregation': 'SEN',
        'year': '2022'
    }
    response = requests.get(HDRO_API_URL, params=params, timeout=20)
    response.raise_for_status()
    data = response.json()

    # Print the response to understand its structure
    print(data)

    records = [{'Year': entry['year'], 'Indicator': entry['indicator_value']} for entry in data]
    df = pd.DataFrame(records)
    raw_data_path = '../data/raw/hdro_data.csv'
    df.to_csv(raw_data_path, index=False)
    df.fillna(method='ffill', inplace=True)
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    df.drop_duplicates(inplace=True)
    processed_data_path = '../data/processed/cleaned_hdro_data.csv'
    df.to_csv(processed_data_path, index=False)
    print(f"HDRO data cleaned and saved to {processed_data_path}")

if __name__ == "__main__":
    download_world_bank_gdp_data()
    # download_imf_gdp_data()
    download_hdro_data()
