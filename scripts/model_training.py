import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import dill as pickle
import os

# Define your custom function to extract date features
def extract_date_features(df):
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    return df.drop(columns=['date'])

# Load the training data
X_train = pd.read_csv('../data/processed/train/X_train.csv')
y_train = pd.read_csv('../data/processed/train/y_train.csv').squeeze()  # Ensure y_train is a Series

# Apply the date feature extraction
date_transformer = FunctionTransformer(extract_date_features, validate=False)

# Identify categorical features and numeric features
categorical_features = []
numeric_features = ['total_cases', 'total_deaths', 'total_tests', 'new_deaths', 'new_tests', 'population',
                    'new_cases_lag1', 'new_cases_lag7', 'new_deaths_lag1', 'new_deaths_lag7',
                    'new_cases_7d_avg', 'new_deaths_7d_avg', 'new_tests_7d_avg',
                    'total_cases_per_capita', 'total_deaths_per_capita', 'total_tests_per_capita',
                    'new_cases_per_capita', 'new_deaths_per_capita', 'new_tests_per_capita',
                    'new_cases_growth_rate', 'new_deaths_growth_rate', 'new_tests_growth_rate']

# Create a ColumnTransformer to preprocess the data
preprocessor = ColumnTransformer(
    transformers=[
        ('date', date_transformer, ['date']),
        ('num', StandardScaler(), numeric_features)
    ],
    remainder='passthrough'
)

# Create a pipeline that first transforms the data then fits the model
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# Train the model
model_pipeline.fit(X_train, y_train)

# Ensure the models directory exists
os.makedirs('../models', exist_ok=True)

# Save the trained model pipeline using dill
with open('../models/linear_regression_model.pkl', 'wb') as f:
    pickle.dump(model_pipeline, f)

print("Model trained and saved successfully.")
