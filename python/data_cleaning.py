"""Clean the predictive-maintenance dataset."""

import pandas as pd


def clean_data(df):
    """Remove duplicates, convert selected columns to numeric, and drop nulls."""
    df = df.copy()

    print("Missing values before cleaning:")
    print(df.isnull().sum())
    print("\nDuplicate rows before cleaning:", df.duplicated().sum())

    df = df.drop_duplicates()

    numeric_columns = ["ball-bearing", "humidity", "vibration"]
    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    print("\nMissing values after numeric conversion:")
    print(df.isnull().sum())

    df = df.dropna()

    print("\nFinal shape:", df.shape)
    print("Final duplicates:", df.duplicated().sum())
    return df


def save_cleaned_data(df, output_path="cleaned_dataset.csv"):
    """Save the cleaned dataset to CSV."""
    df.to_csv(output_path, index=False)
    print(f"\nCleaned dataset saved to: {output_path}")


if __name__ == "__main__":
    from data_loading import load_data

    data = load_data()
    cleaned_data = clean_data(data)
    save_cleaned_data(cleaned_data)
