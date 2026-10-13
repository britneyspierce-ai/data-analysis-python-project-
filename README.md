[README.md](https://github.com/user-attachments/files/33277133/README.md)

**Title:**

Predictive Maintenance and Failure Prediction for Industrial Machinery

**Problem statement:**

To develop a Python-based data analysis system that cleans and explores predictive maintenance data and visualizes machine operating parameters to identify trends, relationships, and potential equipment abnormalities.
# Python data-analysis project

## Folder structure

```text
Python/
├── main.py
├── data_loading.py
├── data_cleaning.py
├── exploratory_analysis.py
├── data_visualization.py
└── README.md
```

## Install dependencies

```bash
pip install pandas matplotlib
```

Place `raw_dataset.csv` in this folder. The loader uses `sep=";"`, matching the supplied notebook.

## Run the whole project

From a terminal opened in this folder, run:

```bash
python main.py
```

`main.py` executes the workflow in order:
1. Load the dataset
2. Clean the dataset and save `predictive-maintenance-cleaned.csv`
3. Perform exploratory data analysis
4. Generate visualizations

You can still run the individual modules separately if needed.


## Visualization output

Running `python main.py` creates a `Visualization/` folder automatically and saves all existing plots plus these additional plots: `distribution_analysis.png`, `category_analysis.png`, `trend_analysis.png`, `correlation_analysis.png`, and `class_balance_analysis.png`. If a graph cannot be meaningfully calculated because the dataset lacks the required column types, a labelled placeholder image is saved so all requested filenames are present.

