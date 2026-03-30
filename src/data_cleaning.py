"""
data_cleaning.py

This module contains functions for loading and cleaning the
Telecom Customer Churn dataset.
"""

import pandas as pd
import numpy as np


import pandas as pd

def load_data(file_path):
    """
    Load dataset from CSV file
    """

    df = pd.read_csv(file_path)

    print("Dataset Loaded Successfully")

    return df


def basic_cleaning(df):
    """
    Perform basic dataset cleaning
    """

    # Remove whitespace from column names
    df.columns = df.columns.str.strip()

    return df


def clean_total_charges(df):
    """
    Convert TotalCharges column to numeric
    """

    df["TotalCharges"] = df["TotalCharges"].replace(" ", np.nan)
    df["TotalCharges"] = df["TotalCharges"].astype(float)

    return df


def handle_missing_values(df):
    """
    Handle missing values in dataset
    """

    # Drop rows with missing TotalCharges
    df = df.dropna()

    return df


def remove_invalid_rows(df):
    """
    Remove rows with invalid tenure values
    """

    df = df[df["tenure"] >= 0]

    return df