"""Perform basic exploratory data analysis."""

import pandas as pd


def explore_data(df):
    """Print column names, data types, descriptive statistics, and null counts."""
    print("Columns:")
    print(df.columns.tolist())

    print("\nFirst five rows:")
    print(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nDataset summary:")
    print(df.describe(include="all"))

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDataset shape:", df.shape)
    print("Duplicate rows:", df.duplicated().sum())


if __name__ == "__main__":
    from data_loading import load_data

    explore_data(load_data())
