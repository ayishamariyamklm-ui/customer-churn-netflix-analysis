"""
utils.py

Utility functions used across the project.
"""

import pandas as pd


def dataset_overview(df):
    """
    Print dataset info and summary statistics
    """

    print("\nDATASET INFO\n")
    print(df.info())

    print("\nSUMMARY STATISTICS\n")
    print(df.describe())


def check_missing_values(df):
    """
    Display missing values
    """

    print("\nMISSING VALUES\n")

    print(df.isnull().sum())


def save_clean_data(df, path):
    """
    Save cleaned dataset
    """

    df.to_csv(path, index=False)

    print(f"\nCleaned dataset saved to: {path}")


def unique_values(df):
    """
    Display unique values in each column
    """

    for col in df.columns:

        print(f"\nColumn: {col}")

        print(df[col].unique())