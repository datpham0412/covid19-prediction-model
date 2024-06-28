import pandas as pd
from sklearn.model_selection import train_test_split

# Load the feature-engineered data
data = pd.read_csv('../data/processed/feature_engineering_data.csv')

# Specify the target variable and features
target = 'new_cases'  # or any other target variable you have
features = data.columns.drop(target)

# Shuffle the data before splitting
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Ensure 'sub_region_1' is included in the features for stratified split
features_with_subregion = data.columns.drop([target])

# Split the data into features (X) and target (y)
X = data[features_with_subregion]
y = data[target]

# Perform the train-test split with stratification by 'sub_region_1'
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=data['sub_region_1'])

X_train.to_csv('../data/processed/X_train.csv', index=False)
X_test.to_csv('../data/processed/X_test.csv', index=False)
y_train.to_csv('../data/processed/y_train.csv', index=False)
y_test.to_csv('../data/processed/y_test.csv', index=False)

print("Data has been split and saved successfully.")

# Check the distribution of sub_region_1 in training and testing sets
print("Training set distribution of sub_region_1:")
print(X_train['sub_region_1'].value_counts(normalize=True))

print("\nTesting set distribution of sub_region_1:")
print(X_test['sub_region_1'].value_counts(normalize=True))