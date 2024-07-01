import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to load the dataset
def load_dataset(filepath):
    try:
        data = pd.read_csv(filepath)
        data['date'] = pd.to_datetime(data['date'])
        logging.info(f"Loaded dataset from {filepath}")
        return data
    except Exception as e:
        logging.error(f"Error loading dataset: {e}")
        raise

# Function to create date-based features
def create_date_features(data):
    data['day_of_week'] = data['date'].dt.dayofweek
    data['week_of_year'] = data['date'].dt.isocalendar().week
    data['month'] = data['date'].dt.month
    data['quarter'] = data['date'].dt.quarter
    logging.info("Date-based features created")
    return data

# Function to distribute new cases over intervals where total cases rise
def distribute_new_cases(data):
    try:
        total_cases_list = data['total_cases'].tolist()
        new_cases_list = [0] * len(total_cases_list)
        
        last_idx = 0
        for i in range(1, len(total_cases_list)):
            if total_cases_list[i] > total_cases_list[last_idx]:
                increase = total_cases_list[i] - total_cases_list[last_idx]
                days = i - last_idx
                for j in range(last_idx, i):
                    new_cases_list[j] = increase / days
                last_idx = i
        
        data['new_cases'] = new_cases_list
        logging.info("New cases distributed over intervals")
        return data
    except Exception as e:
        logging.error(f"Error distributing new cases: {e}")
        raise

# Function to aggregate data by date
def aggregate_by_date(data):
    try:
        # Aggregate relevant features by date
        agg_data = data.groupby('date').agg({
            'total_cases': 'max',
            'total_deaths': 'max',
            'total_tests': 'max',
            'new_cases': 'max',  # This will be recalculated
            'new_deaths': 'max',
            'new_tests': 'max',
            'population': 'max'
        }).reset_index()

        logging.info("Data aggregated by date")
        return agg_data
    except Exception as e:
        logging.error(f"Error aggregating data by date: {e}")
        raise

# Function to create lag features
def create_lag_features(data, lag_features):
    try:
        data = data.sort_values(by=['date'])
        for feature in lag_features:
            data[f'{feature}_lag1'] = data[feature].shift(1)
            data[f'{feature}_lag7'] = data[feature].shift(7)
        logging.info("Lag features created")
        return data
    except Exception as e:
        logging.error(f"Error creating lag features: {e}")
        raise

# Function to create rolling averages
def create_rolling_averages(data, rolling_features, window):
    try:
        for feature in rolling_features:
            data[f'{feature}_{window}d_avg'] = data[feature].rolling(window, min_periods=1).mean()
        logging.info("Rolling averages created")
        return data
    except Exception as e:
        logging.error(f"Error creating rolling averages: {e}")
        raise

# Function to create per capita metrics
def create_per_capita_metrics(data, features, population_feature):
    try:
        for feature in features:
            data[f'{feature}_per_capita'] = data[feature] / data[population_feature]
        logging.info("Per capita metrics created")
        return data
    except Exception as e:
        logging.error(f"Error creating per capita metrics: {e}")
        raise

# Function to create growth rates
def create_growth_rates(data, features):
    try:
        for feature in features:
            growth_rate = data[feature] / (data[feature].shift(1) + 1) - 1
            data[f'{feature}_growth_rate'] = growth_rate.fillna(0).replace([np.inf, -np.inf], 0)
        logging.info("Growth rates created")
        return data
    except Exception as e:
        logging.error(f"Error creating growth rates: {e}")
        raise

# Custom function to scale features with an option to exclude some
def custom_scale_features(data, selected_features, features_to_exclude=[]):
    try:
        scaler = StandardScaler()
        features_to_scale = [feature for feature in selected_features if feature not in features_to_exclude]
        data[features_to_scale] = scaler.fit_transform(data[features_to_scale])
        
        logging.info("Features scaled")
        return data
    except Exception as e:
        logging.error(f"Error scaling features: {e}")
        raise

# Ensure no negative values in new_cases or new_deaths
def ensure_non_negative(data, features):
    try:
        for feature in features:
            data[feature] = data[feature].apply(lambda x: max(x, 0))
        logging.info("Ensured non-negative values for features")
        return data
    except Exception as e:
        logging.error(f"Error ensuring non-negative values: {e}")
        raise

# Main function to perform the steps up to creating lag features
def perform_feature_engineering(filepath, save_path):
    try:
        # Step 1: Load dataset
        data = load_dataset(filepath)
        
        # Step 2: Create date-based features
        data = create_date_features(data)
        
        # Step 3: Aggregate data by date
        data = aggregate_by_date(data)
        
        # Step 4: Distribute new cases over intervals
        data = distribute_new_cases(data)

        # Step 5: Create lag features
        lag_features = ['new_cases', 'new_deaths']
        data = create_lag_features(data, lag_features)

        # Step 6: Create rolling averages
        rolling_features = ['new_cases', 'new_deaths', 'new_tests']
        window = 7
        data = create_rolling_averages(data, rolling_features, window)

        # Step 7: Create per capita metrics
        per_capita_features = ['total_cases', 'total_deaths', 'total_tests', 'new_cases', 'new_deaths', 'new_tests']
        data = create_per_capita_metrics(data, per_capita_features, 'population')

        # Step 8: Create growth rates
        growth_rate_features = ['new_cases', 'new_deaths', 'new_tests']
        data = create_growth_rates(data, growth_rate_features)
        
        # Step 9: Custom scale features excluding new_cases and new_deaths
        selected_features = ['new_cases', 'new_deaths', 'new_cases_lag1', 'new_deaths_lag1', 'new_cases_lag7', 'new_deaths_lag7',
                             'new_cases_7d_avg', 'new_deaths_7d_avg', 'total_cases_per_capita', 'new_cases_per_capita', 
                             'total_deaths_per_capita', 'new_deaths_per_capita', 'total_tests_per_capita', 'new_tests_per_capita',
                             'new_cases_growth_rate', 'new_deaths_growth_rate', 'new_tests_growth_rate']
        features_to_exclude = ['new_cases', 'new_deaths']
        data = custom_scale_features(data, selected_features, features_to_exclude)
        
        # Ensure no negative values for new_cases and new_deaths
        data = ensure_non_negative(data, ['new_cases', 'new_deaths'])

        # Fill missing values for lag features
        data.fillna(0, inplace=True)

        # Save the processed data to a new CSV file
        data.to_csv(save_path, index=False)
        logging.info(f"Feature engineering completed and saved to {save_path}")
    except Exception as e:
        logging.error(f"Error in perform_feature_engineering: {e}")
        raise

# Run the feature engineering process
perform_feature_engineering('../data/processed/merged_data_aus.csv', '../data/processed/feature_engineering_data.csv')
