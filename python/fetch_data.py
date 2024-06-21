import pandas as pd
import requests

def fetch_covid_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    df = pd.read_csv(url)
    return df

def process_covid_data(df):
    df = df[['location', 'date', 'total_cases', 'total_deaths', 'total_tests', 'new_cases', 'new_deaths', 'new_tests', 'population']].copy()
    df['date'] = pd.to_datetime(df['date'])
    return df

def fetch_mobility_data():
    url = "https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv"
    df = pd.read_csv(url)
    return df

def main():
    covid_data = fetch_covid_data()
    processed_covid_data = process_covid_data(covid_data)
    processed_covid_data.to_csv('../data/covid_data.csv', index=False)

    mobility_data = fetch_mobility_data()
    mobility_data.to_csv('../data/mobility_data.csv', index=False)

if __name__ == "__main__":
    main()
