import os
import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(country_name):
    country_name_lower = country_name.lower()
    input_file = f'../data/processed/feature_engineering_data_{country_name_lower}.csv'
    train_dir = f'../data/processed/train/{country_name_lower}'
    test_dir = f'../data/processed/test/{country_name_lower}'

    # Load the feature-engineered data
    data = pd.read_csv(input_file)

    # Ensure 'date' column is of datetime type
    data['date'] = pd.to_datetime(data['date'])

    # Specify the target variable and features
    target = 'new_cases'
    features = data.columns.drop(target)

    # Shuffle the data before splitting
    data = data.sample(frac=1, random_state=42).reset_index(drop=True)

    # Split the data into features (X) and target (y)
    X = data[features]
    y = data[target]

    # Ensure the directories exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Perform the train-test split
    split_date = data['date'].quantile(0.8)
    train_data = data[data['date'] <= split_date]
    test_data = data[data['date'] > split_date]

    X_train = train_data[features]
    y_train = train_data[target]
    X_test = test_data[features]
    y_test = test_data[target]

    # Save the split data to CSV files
    X_train.to_csv(os.path.join(train_dir, 'X_train.csv'), index=False)
    X_test.to_csv(os.path.join(test_dir, 'X_test.csv'), index=False)
    y_train.to_csv(os.path.join(train_dir, 'y_train.csv'), index=False)
    y_test.to_csv(os.path.join(test_dir, 'y_test.csv'), index=False)

    print("Data has been split and saved successfully.")

if __name__ == "__main__":
    country_name = input("Enter the country name for data splitting: ")
    split_data(country_name)
