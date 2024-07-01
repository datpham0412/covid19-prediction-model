import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import dill as pickle

# Load the test data
X_test = pd.read_csv('../data/processed/test/X_test.csv')
y_test = pd.read_csv('../data/processed/test/y_test.csv')

# Convert y_test to a Series to ensure it's 1-dimensional
y_test = y_test.squeeze()

# Load the trained model using dill
with open('../models/linear_regression_model.pkl', 'rb') as f:
    model_pipeline = pickle.load(f)

# Make predictions
y_pred = model_pipeline.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2): {r2}")

# Ensure y_test and y_pred are both 1-dimensional
if y_test.ndim > 1:
    y_test = y_test.squeeze()
if y_pred.ndim > 1:
    y_pred = y_pred.squeeze()

# Optional: Save predictions to a CSV file for further analysis
predictions = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
predictions.to_csv('../data/processed/predictions.csv', index=False)

print("Model evaluation completed and predictions saved.")
