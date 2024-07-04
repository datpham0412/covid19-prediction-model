import sqlite3
import pandas as pd
import os

# Function to load data from the SQLite database
def load_data(db_path):
    conn = sqlite3.connect(db_path)
    covid_query = "SELECT * FROM CovidData"
    mobility_query = "SELECT * FROM MobilityData"
    
    covid_data = pd.read_sql_query(covid_query, conn)
    mobility_data = pd.read_sql_query(mobility_query, conn)
    
    conn.close()
    return covid_data, mobility_data

# Function to preprocess data
def preprocess_data(covid_data, mobility_data):
    print("CovidData:")
    print(covid_data.head())
    print("\nMobilityData:")
    print(mobility_data.head())
    
    # Merge data on the date column
    merged_data = pd.merge(covid_data, mobility_data, left_on='date', right_on='date')
    
    # Drop rows with missing values
    merged_data.dropna(inplace=True)

    # Drop unnecessary columns
    merged_data.drop(columns=['id_x', 'id_y'], inplace=True)
    
    # Convert date to datetime
    merged_data['date'] = pd.to_datetime(merged_data['date'])
    
    # Convert total_cases and total_tests to numeric, coercing errors
    merged_data['total_cases'] = pd.to_numeric(merged_data['total_cases'], errors='coerce')
    merged_data['total_tests'] = pd.to_numeric(merged_data['total_tests'], errors='coerce')
    
    # Fill NaN values in total_cases and total_tests with 0
    merged_data['total_cases'].fillna(0, inplace=True)
    merged_data['total_tests'].fillna(0, inplace=True)

    # Calculate new cases and new tests
    merged_data = merged_data.sort_values(by=['date'])
    merged_data['new_cases'] = merged_data['total_cases'].diff().fillna(0)
    merged_data['new_tests'] = merged_data['total_tests'].diff().fillna(0)
    
    # Ensure new_cases and new_tests are non-negative
    merged_data['new_cases'] = merged_data['new_cases'].apply(lambda x: max(x, 0))
    merged_data['new_tests'] = merged_data['new_tests'].apply(lambda x: max(x, 0))
    
    return merged_data

def main():
    country_name = input("Enter the country name: ").strip().lower()
    db_filename = f"processed_data_{country_name}.db"
    db_path = os.path.join('../data/db', db_filename)
    
    if not os.path.exists(db_path):
        print(f"Database for {country_name} not found.")
        return
    
    covid_data, mobility_data = load_data(db_path)
    merged_data = preprocess_data(covid_data, mobility_data)
    
    print("\nMerged Data Table:")
    print(merged_data.head())

    # Print column names
    print("\nColumn Names:")
    print(merged_data.columns)

    # Ensure the processed directory exists
    processed_dir = '../data/processed'
    os.makedirs(processed_dir, exist_ok=True)
    
    # Save merged data to a CSV file for EDA
    output_filename = f"merged_data_{country_name}.csv"
    output_path = os.path.join(processed_dir, output_filename)
    merged_data.to_csv(output_path, index=False)
    print(f"Merged data saved to '{output_path}'")

if __name__ == "__main__":
    main()
