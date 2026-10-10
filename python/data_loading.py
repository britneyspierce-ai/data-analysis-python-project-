"""Load the raw dataset."""

from pathlib import Path
import pandas as pd


def load_data(file_path="raw_dataset.csv", sep=";"):
    """Load a CSV dataset and display a quick preview."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path.resolve()}\n"
            "Place the CSV file in the project folder or pass its full path."
        )

    df = pd.read_csv(path, sep=sep)
    print("Dataset preview:")
    print(df.head())
    print("\nDataset information:")
    df.info()
    return df


if __name__ == "__main__":
    load_data()
