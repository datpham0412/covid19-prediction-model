import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Function to set display options
def set_display_options():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

def reset_display_options():
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.max_colwidth')

# Function to print summary statistics
def print_summary_statistics(data):
    print("\nSummary statistics:")
    print(data.describe())

# Function to print missing values analysis
def print_missing_values(data):
    print("\nMissing values: ")
    print(data.isnull().sum())

# Function to print correlation matrix
def print_correlation_matrix(data):
    numeric_cols = data.select_dtypes(include=[np.number])
    correlation_matrix = numeric_cols.corr()
    print("\nCorrelation Matrix: ")
    print(correlation_matrix)
    return correlation_matrix

# Function to plot correlation heatmap
def plot_correlation_heatmap(correlation_matrix):
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix Heatmap")
    plt.show()

# Function to plot new cases and new deaths over time
def plot_cases_and_deaths_over_time(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['date'], data['new_cases'], label='New Cases')
    plt.plot(data['date'], data['new_deaths'], label='New Deaths')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Covid-19 New Cases and New Deaths Over Time')
    plt.legend()
    plt.show()

# Function to plot residential vs workplaces scatter plot
def plot_residential_vs_workplaces(data):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=data['residential'], y=data['workplaces'])
    plt.xlabel('Residential')
    plt.ylabel('Workplaces')
    plt.title('Residential vs Workplaces')
    plt.show()

# Function to plot histogram for distribution of new cases
def plot_distribution_of_new_cases(data):
    plt.figure(figsize=(12, 6))
    sns.histplot(data['new_cases'], bins=30, kde=True)
    plt.xlabel('New Cases')
    plt.ylabel('Frequency')
    plt.title('Distribution of New Cases')
    plt.show()

# Main function to perform EDA
def perform_eda(data):
    set_display_options()

    print_summary_statistics(data)
    print_missing_values(data)

    correlation_matrix = print_correlation_matrix(data)
    plot_correlation_heatmap(correlation_matrix)

    plot_cases_and_deaths_over_time(data)
    plot_residential_vs_workplaces(data)
    plot_distribution_of_new_cases(data)

    reset_display_options()

def main():
    # Load merged data from csv file
    merged_data = pd.read_csv('../data/merged_data_aus.csv')

    print("\nMerged data table: ")
    print(merged_data.head())

    perform_eda(merged_data)

if __name__ == "__main__":
    main()
