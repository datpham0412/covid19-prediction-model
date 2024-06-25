import pandas as pd
import sqlite3

def load_data():
    covid_data = pd.read_csv("../data/covid_data.csv")
    mobility_data = pd.read_csv("../data/mobility_data.csv")
    return covid_data, mobility_data

def preprocess_covid_data(df):
    df = df[['location', 'date', 'total_cases', 'total_deaths', 'total_tests', 'new_cases', 'new_deaths', 'new_tests', 'population']]
    df['date'] = pd.to_datetime(df['date'])
    df.fillna(0, inplace=True)
    df['total_cases'] = df['total_cases'].astype(float)
    df['total_deaths'] = df['total_deaths'].astype(float)
    df['total_tests'] = df['total_tests'].astype(float)
    df['new_cases'] = df['new_cases'].astype(float)
    df['new_deaths'] = df['new_deaths'].astype(float)
    df['new_tests'] = df['new_tests'].astype(float)
    df['population'] = df['population'].astype(float)
    return df

def preprocess_mobility_data(df):
    df = df[['country_region', 'date', 'retail_and_recreation_percent_change_from_baseline', 
             'grocery_and_pharmacy_percent_change_from_baseline', 'parks_percent_change_from_baseline',
             'transit_stations_percent_change_from_baseline', 'workplaces_percent_change_from_baseline', 
             'residential_percent_change_from_baseline']]
    df['date'] = pd.to_datetime(df['date'])
    df.fillna(0, inplace=True)
    return df

def save_to_database(df, db_filename):
    conn = sqlite3.connect(db_filename)
    df.to_sql('Data', conn, if_exists='replace', index=False)
    conn.close()

def main():
    covid_data, mobility_data = load_data()
    processed_covid_data = preprocess_covid_data(covid_data)
    processed_mobility_data = preprocess_mobility_data(mobility_data)
    save_to_database(processed_covid_data, '../data/processed_data.db')
    save_to_database(processed_mobility_data, '../data/processed_mobility_data.db')

if __name__ == "__main__":
    main()
