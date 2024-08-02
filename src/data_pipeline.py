import os
import pandas as pd
import requests

# Create directories for raw and processed data if they don't exist
os.makedirs('../data/raw', exist_ok=True)
os.makedirs('../data/processed', exist_ok=True)

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

def download_imf_gdp_data():
    IMF_API_URL = 'https://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/Q.SN.NGDP_R'
    params = {'startPeriod': '2000', 'endPeriod': '2024'}
    response = requests.get(IMF_API_URL, params=params)
    data = response.json()
    records = [{'Year': entry['@TIME_PERIOD'], 'GDP': entry['@OBS_VALUE']} for entry in data['CompactData']['DataSet']['Series']['Obs']]
    df = pd.DataFrame(records)
    raw_data_path = '../data/raw/imf_gdp_data.csv'
    df.to_csv(raw_data_path, index=False)
    df.fillna(method='ffill', inplace=True)
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    df.drop_duplicates(inplace=True)
    processed_data_path = '../data/processed/cleaned_imf_gdp_data.csv'
    df.to_csv(processed_data_path, index=False)
    print(f"GDP data from IMF cleaned and saved to {processed_data_path}")

def download_undp_data():
    print("UNDP data function is a placeholder. Please replace with actual implementation.")

def download_transparency_data():
    print("Transparency International data function is a placeholder. Please replace with actual implementation.")

def download_afdb_data():
    print("AfDB data function is a placeholder. Please replace with actual implementation.")

def download_ecowas_data():
    print("ECOWAS data function is a placeholder. Please replace with actual implementation.")

def download_senegal_stats_data():
    print("Senegal National Bureau of Statistics data function is a placeholder. Please replace with actual implementation.")

def validate_data():
    world_bank_df = pd.read_csv('../data/processed/cleaned_world_bank_gdp_data.csv')
    imf_df = pd.read_csv('../data/processed/cleaned_imf_gdp_data.csv')
    merged_df = pd.merge(world_bank_df, imf_df, on='Year', suffixes=('_wb', '_imf'))
    inconsistencies = merged_df[abs(merged_df['GDP_wb'] - merged_df['GDP_imf']) > 1e9]
    if not inconsistencies.empty:
        print("Inconsistencies found in the GDP data:")
        print(inconsistencies)
    else:
        print("No inconsistencies found in the GDP data.")

if __name__ == "__main__":
    download_world_bank_gdp_data()
    download_imf_gdp_data()
    download_undp_data()
    download_transparency_data()
    download_afdb_data()
    download_ecowas_data()
    download_senegal_stats_data()
    validate_data()
