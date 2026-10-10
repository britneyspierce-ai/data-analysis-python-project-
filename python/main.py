"""Run the complete data-analysis workflow from one entry point."""

from data_loading import load_data
from data_cleaning import clean_data, save_cleaned_data
from exploratory_analysis import explore_data
from data_visualization import visualize_data


def main():
    dataset_path = "raw_dataset.csv"
    cleaned_path = "cleaned_dataset.csv"

    print("\n" + "=" * 60)
    print("STEP 1: DATA LOADING")
    print("=" * 60)
    df = load_data(dataset_path)

    print("\n" + "=" * 60)
    print("STEP 2: DATA CLEANING")
    print("=" * 60)
    cleaned_df = clean_data(df)
    save_cleaned_data(cleaned_df, cleaned_path)

    print("\n" + "=" * 60)
    print("STEP 3: EXPLORATORY DATA ANALYSIS")
    print("=" * 60)
    explore_data(cleaned_df)

    print("\n" + "=" * 60)
    print("STEP 4: DATA VISUALIZATION")
    print("=" * 60)
    visualize_data(cleaned_df)

    print("\nAll analysis steps completed successfully.")


if __name__ == "__main__":
    main()
