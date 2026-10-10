"""Create visualizations for the predictive-maintenance dataset."""

import matplotlib.pyplot as plt
import pandas as pd


def visualize_data(df):
    """Plot trends for key variables and relationships with vibration."""
    columns = ["ball-bearing", "humidity", "vibration"]
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"Required column(s) missing from dataset: {missing}")

    for column in columns:
        plt.figure(figsize=(10, 5))
        plt.plot(df[column])
        plt.title(f"{column.replace('-', ' ').title()} Trend")
        plt.xlabel("Observation")
        plt.ylabel(column.replace("-", " ").title())
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    plt.figure(figsize=(8, 5))
    plt.scatter(df["ball-bearing"], df["vibration"], alpha=0.3)
    plt.title("Ball-Bearing vs Vibration")
    plt.xlabel("Ball-Bearing")
    plt.ylabel("Vibration")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.scatter(df["humidity"], df["vibration"], alpha=0.3)
    plt.title("Humidity vs Vibration")
    plt.xlabel("Humidity")
    plt.ylabel("Vibration")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("cleaned_datadet.csv")
    visualize_data(df)
