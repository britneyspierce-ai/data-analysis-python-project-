"""Create and save existing and additional visualizations."""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

# All plots are saved in this folder, created automatically if necessary.
OUTPUT_DIR = Path(__file__).resolve().parent / "Visualization"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def _save_plot(filename):
    """Save the current figure into the Visualization folder."""
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()


def visualize_data(df):
    """Create the project's existing plots and save each one to disk."""
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
        _save_plot(f"{column.replace('-', '_')}_trend.png")

    plt.figure(figsize=(8, 5))
    plt.scatter(df["ball-bearing"], df["vibration"], alpha=0.3)
    plt.title("Ball-Bearing vs Vibration")
    plt.xlabel("Ball-Bearing")
    plt.ylabel("Vibration")
    plt.grid(True)
    _save_plot("ball_bearing_vs_vibration.png")

    plt.figure(figsize=(8, 5))
    plt.scatter(df["humidity"], df["vibration"], alpha=0.3)
    plt.title("Humidity vs Vibration")
    plt.xlabel("Humidity")
    plt.ylabel("Vibration")
    plt.grid(True)
    _save_plot("humidity_vs_vibration.png")

    # New requested graphs
    create_additional_visualizations(df)


def create_additional_visualizations(df):
    """Create distribution, category, trend, correlation and class-balance plots."""
    numeric_df = df.select_dtypes(include="number")
    categorical_columns = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

    # 1. Distribution analysis
    if not numeric_df.empty:
        ax = numeric_df.hist(figsize=(12, 8), bins=20)
        plt.gcf().suptitle("Distribution Analysis", y=1.02)
        _save_plot("distribution_analysis.png")
    else:
        _save_placeholder("distribution_analysis.png", "Distribution Analysis", "No numeric columns available")

    # 2. Category analysis
    if categorical_columns:
        column = categorical_columns[0]
        plt.figure(figsize=(10, 5))
        df[column].astype(str).value_counts().head(20).plot(kind="bar")
        plt.title(f"Category Analysis: {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        _save_plot("category_analysis.png")
    else:
        _save_placeholder("category_analysis.png", "Category Analysis", "No categorical columns available")

    # 3. Trend analysis
    if not numeric_df.empty:
        plt.figure(figsize=(10, 5))
        for column in numeric_df.columns[:5]:
            plt.plot(numeric_df[column].reset_index(drop=True), label=str(column))
        plt.title("Trend Analysis")
        plt.xlabel("Observation")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)
        _save_plot("trend_analysis.png")
    else:
        _save_placeholder("trend_analysis.png", "Trend Analysis", "No numeric columns available")

    # 4. Correlation analysis
    if len(numeric_df.columns) >= 2:
        plt.figure(figsize=(10, 7))
        correlation = numeric_df.corr()
        image = plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1, aspect="auto")
        plt.colorbar(image, label="Correlation")
        plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45, ha="right")
        plt.yticks(range(len(correlation.columns)), correlation.columns)
        for i in range(len(correlation.columns)):
            for j in range(len(correlation.columns)):
                value = correlation.iloc[i, j]
                if pd.notna(value):
                    plt.text(j, i, f"{value:.2f}", ha="center", va="center", fontsize=8)
        plt.title("Correlation Analysis")
        _save_plot("correlation_analysis.png")
    else:
        _save_placeholder("correlation_analysis.png", "Correlation Analysis", "At least two numeric columns are required")

    # 5. Class balance analysis. Prefer common target names; otherwise use a categorical column.
    target_candidates = ["class", "target", "label", "status", "failure", "machine_failure", "class_label"]
    target_column = next((c for c in target_candidates if c in df.columns), None)
    if target_column is None and categorical_columns:
        target_column = categorical_columns[0]

    if target_column is not None:
        plt.figure(figsize=(8, 5))
        df[target_column].astype(str).value_counts().plot(kind="bar")
        plt.title(f"Class Balance Analysis: {target_column}")
        plt.xlabel(target_column)
        plt.ylabel("Count")
        _save_plot("class_balance_analysis.png")
    else:
        _save_placeholder("class_balance_analysis.png", "Class Balance Analysis", "No class/target column available")

    print(f"\nAll visualizations saved in: {OUTPUT_DIR}")


def _save_placeholder(filename, title, message):
    """Save a labelled image when the dataset lacks columns for a graph."""
    plt.figure(figsize=(8, 5))
    plt.axis("off")
    plt.title(title)
    plt.text(0.5, 0.5, message, ha="center", va="center", wrap=True)
    _save_plot(filename)


if __name__ == "__main__":
    df = pd.read_csv("predictive-maintenance-cleaned.csv")
    visualize_data(df)
