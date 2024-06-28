import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Function to load the dataset
def load_dataset(filepath):
    data = pd.read_csv(filepath)
    data['date'] = pd.to_datetime(data['date'])
    return data

# Function to create date-based features
def create_date_features(data):
    data['day_of_week'] = data['date'].dt.dayofweek
    data['week_of_year'] = data['date'].dt.isocalendar().week
    data['month'] = data['date'].dt.month
    data['quarter'] = data['date'].dt.quarter
    return data

# Function to create lag features
def create_lag_features(data, lag_features):
    # Fill missing or zero sub_region_2 with a placeholder value
    data['sub_region_2'] = data['sub_region_2'].replace(0, 'unknown').fillna('unknown')
    
    data = data.sort_values(by=['country_region', 'sub_region_1', 'sub_region_2', 'date'])
    grouped = data.groupby(['country_region', 'sub_region_1', 'sub_region_2'])
    for feature in lag_features:
        data[f'{feature}_lag1'] = grouped[feature].shift(1)
        data[f'{feature}_lag7'] = grouped[feature].shift(7)
    return data

# Function to create rolling averages
def create_rolling_averages(data, rolling_features, window):
    grouped = data.groupby(['country_region', 'sub_region_1', 'sub_region_2'])
    for feature in rolling_features:
        data[f'{feature}_{window}d_avg'] = grouped[feature].transform(lambda x: x.rolling(window, min_periods=1).mean())
    return data

# Function to create per capita metrics
def create_per_capita_metrics(data, features, population_feature):
    for feature in features:
        data[f'{feature}_per_capita'] = data[feature] / data[population_feature]
    return data

# Function to create growth rates
def create_growth_rates(data, features):
    for feature in features:
        growth_rate = data[feature] / (data[feature].shift(1) + 1) - 1
        data[f'{feature}_growth_rate'] = growth_rate.fillna(0).replace([np.inf, -np.inf], 0)
    return data

# Function to select and scale specified features
def select_and_scale_features(data, selected_features):
    scaler = StandardScaler()
    data[selected_features] = scaler.fit_transform(data[selected_features])
    return data


# Main function to perform the steps up to creating lag features
def perform_feature_engineering(filepath, save_path):
    # Step 1: Load dataset
    data = load_dataset(filepath)
    
    # Step 2: Create date-based features
    data = create_date_features(data)
    
    # Step 3: Create lag features
    lag_features = ['new_cases', 'new_deaths']
    data = create_lag_features(data, lag_features)

    # Step 4: Create rolling averages
    rolling_features = ['new_cases', 'new_deaths', 'new_tests']
    window = 7
    data = create_rolling_averages(data, rolling_features, window)

    # Step 5: Create per capita metrics
    per_capita_features = ['total_cases', 'total_deaths', 'total_tests', 'new_cases', 'new_deaths', 'new_tests']
    data = create_per_capita_metrics(data, per_capita_features, 'population')

    # Step 6: Create growth rates
    growth_rate_features = ['new_cases', 'new_deaths', 'new_tests']
    data = create_growth_rates(data, growth_rate_features)
    
    # Step 7: Select and scale features
    selected_features = ['new_cases', 'new_deaths', 'new_cases_lag1', 'new_deaths_lag1', 'new_cases_lag7', 'new_deaths_lag7',
                         'new_cases_7d_avg', 'new_deaths_7d_avg', 'total_cases_per_capita', 'new_cases_per_capita', 
                         'total_deaths_per_capita', 'new_deaths_per_capita', 'total_tests_per_capita', 'new_tests_per_capita',
                         'new_cases_growth_rate', 'new_deaths_growth_rate', 'new_tests_growth_rate']
    data = select_and_scale_features(data, selected_features)

    # Fill missing values for lag features
    data.fillna(0, inplace=True)

    # Save the processed data to a new CSV file
    data.to_csv(save_path, index=False)

# Run the feature engineering process
perform_feature_engineering('../data/processed/merged_data_aus.csv', '../data/processed/feature_engineering_data.csv')
