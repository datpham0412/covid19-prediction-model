# scripts/model_training.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

# Load the training data
X_train = pd.read_csv('../data/processed/train/X_train.csv')
y_train = pd.read_csv('../data/processed/train/y_train.csv')

# Define a function to extract date features
def extract_date_features(df):
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    return df.drop(columns=['date'])

# Apply the date feature extraction
date_transformer = FunctionTransformer(extract_date_features)

# Identify categorical features
categorical_features = ['location', 'country_region', 'sub_region_1', 'sub_region_2']

# Create a ColumnTransformer to preprocess the data
preprocessor = ColumnTransformer(
    transformers=[
        ('date', date_transformer, ['date']),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough'  # Leave the rest of the columns unchanged
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

# Save the trained model pipeline
joblib.dump(model_pipeline, '../models/linear_regression_model.pkl')

print("Model trained and saved successfully.")
