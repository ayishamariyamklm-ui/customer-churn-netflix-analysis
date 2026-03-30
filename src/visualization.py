"""
visualization.py

This module contains visualization functions
for exploratory data analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def churn_countplot(df):
    """
    Plot churn distribution
    """

    plt.figure(figsize=(8, 5))

    sns.countplot(x="Churn", data=df)

    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Customer Count")

    plt.show()


def contract_vs_churn(df):
    """
    Plot contract type vs churn
    """

    if "Contract" in df.columns:

        plt.figure(figsize=(8, 5))

        sns.countplot(x="Contract", hue="Churn", data=df)

        plt.title("Contract Type vs Churn")

        plt.show()

    else:
        print("Contract column encoded - cannot plot original contract comparison")


def monthlycharges_boxplot(df):
    """
    Monthly charges vs churn
    """

    plt.figure(figsize=(8, 5))

    sns.boxplot(x="Churn", y="MonthlyCharges", data=df)

    plt.title("Monthly Charges by Churn")

    plt.show()


def tenure_boxplot(df):
    """
    Tenure distribution by churn
    """

    plt.figure(figsize=(8, 5))

    sns.boxplot(x="Churn", y="tenure", data=df)

    plt.title("Customer Tenure vs Churn")

    plt.show()


def correlation_heatmap(df):
    """
    Correlation heatmap
    """

    plt.figure(figsize=(12, 8))

    corr = df.corr(numeric_only=True)

    sns.heatmap(corr, cmap="coolwarm")

    plt.title("Correlation Heatmap")

    plt.show()


def pairplot_visual(df):
    """
    Pairplot for key numerical features
    """

    columns = ["tenure", "MonthlyCharges", "TotalCharges", "Churn"]

    sns.pairplot(df[columns], hue="Churn")

    plt.show()