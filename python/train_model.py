import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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
    
    # Debugging: Print the date columns to check for matching values
    print("\nCovidData Dates:")
    print(covid_data['date'].unique())
    print("\nMobilityData Dates:")
    print(mobility_data['date'].unique())
    
    # Drop rows with missing values
    merged_data.dropna(inplace=True)
    
    # Convert date to datetime
    merged_data['date'] = pd.to_datetime(merged_data['date'])
    
    return merged_data

# Function to train and evaluate the model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f'Mean Squared Error: {mse}')
    print(f'R^2 Score: {r2}')
    
    return model

# Main function
def main():
    db_path = '../data/processed_data.db'
    
    covid_data, mobility_data = load_data(db_path)
    merged_data = preprocess_data(covid_data, mobility_data)
    
    # Print the merged data table
    print("\nMerged Data Table:")
    print(merged_data)
    
    # Feature selection for model training
    X = merged_data[['retail_and_recreation', 'grocery_and_pharmacy', 'parks', 'transit_stations', 'workplaces', 'residential']]
    y = merged_data['new_cases']
    
    model = train_model(X, y)
    
    print("Model training complete.")

if __name__ == "__main__":
    main()
