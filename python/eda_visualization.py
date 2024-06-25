import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Function to perform EDA
def perform_eda(merged_data):
    # Summary statistics
    print("\nSummary statistics:")
    print(merged_data.describe())

    # Missing values analysis
    print("\nMissing values: ")
    print(merged_data.isnull().sum())

def main():
    # Load merged data from csv file:
    merged_data = pd.read_csv('../data/merged_data.csv')

    print("\nMerged data table: ")
    print(merged_data.head())

    perform_eda(merged_data)

if __name__ == "__main__":
    main()