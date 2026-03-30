"""
feature_engineering.py

This module contains functions to create new features
for churn analysis.
"""

import pandas as pd


def create_tenure_group(df):
    """
    Create tenure buckets
    """

    bins = [0, 12, 24, 48, 60, 72]
    labels = ["0-12", "13-24", "25-48", "49-60", "61-72"]

    df["TenureGroup"] = pd.cut(df["tenure"], bins=bins, labels=labels)

    return df


def average_monthly_spend(df):
    """
    Calculate average monthly spend
    """

    df["AvgMonthlySpend"] = df["TotalCharges"] / df["tenure"]

    df["AvgMonthlySpend"] = df["AvgMonthlySpend"].fillna(0)

    return df


def binary_encoding(df):
    """
    Convert Yes/No columns to binary values
    """

    binary_columns = [
        "Partner",
        "Dependents",
        "PhoneService",
        "PaperlessBilling",
        "Churn"
    ]

    for col in binary_columns:

        if col in df.columns:
            df[col] = df[col].map({"Yes": 1, "No": 0})

    return df


def encode_gender(df):
    """
    Encode gender column
    """

    df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

    return df


def one_hot_encoding(df):
    """
    Perform one hot encoding for categorical features
    """

    categorical_columns = [
        "Contract",
        "InternetService",
        "PaymentMethod"
    ]

    df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

    return df