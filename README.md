[README.md](https://github.com/user-attachments/files/33277133/README.md)
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
2. Clean the dataset and save `cleaned_dataset.csv`
3. Perform exploratory data analysis
4. Generate visualizations

You can still run the individual modules separately if needed.
