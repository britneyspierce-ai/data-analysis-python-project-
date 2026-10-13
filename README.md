# Predictive Maintenance Data Analysis Using Python

## Project Overview

**Predictive Maintenance Data Analysis Using Python** is a data analysis project that focuses on processing, cleaning, exploring, and visualizing machine-related sensor data. The project analyzes parameters such as ball-bearing measurements, humidity, and vibration to understand data distributions, identify trends, and investigate relationships between variables.

The project uses Python libraries such as Pandas, Matplotlib, and Seaborn to perform data preprocessing, exploratory data analysis (EDA), and visualization. It follows a modular structure in which each Python file is responsible for a specific stage of the workflow.

A Jupyter Notebook is also included to demonstrate the complete analysis interactively. All generated graphs are organized in a dedicated `Visualization` folder.

## Problem Statement

To develop a Python-based data analysis system that cleans predictive maintenance sensor data and visualizes distributions, trends, categories, and relationships to support the investigation of potentially abnormal machine operating patterns.

## Objectives

- Load and process raw sensor data using Python.
- Identify and handle missing values, duplicate records, and invalid numeric values.
- Perform exploratory data analysis to understand the dataset's characteristics.
- Analyze ball-bearing measurements, humidity, and vibration.
- Generate visualizations to identify trends, distributions, and correlations.
- Automate data processing through modular Python scripts.
- Store the cleaned dataset and visualization outputs in organized folders.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, cleaning, manipulation, and statistical analysis |
| Matplotlib | Line charts, scatter plots, and other visualizations |
| Seaborn | Distribution plots and correlation heatmaps |
| OS module | Directory creation and file path management |
| Jupyter Notebook | Interactive analysis and code execution |

## Project Structure

```text
Data-Analysis-Python-Project/
│
├── README.md
│
├── Dataset/
│   ├── raw_dataset.csv
│   ├── cleaned_dataset.csv
│   └── temp.txt
│
├── Notebook/
│   ├── Data-Analysis-Python-Project_with_visualizations.ipynb
│   └── temp.txt
│
├── Python/
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   └── data_visualization.py
│
└── Visualization/
    ├── ball_bearing_trend.png
    ├── humidity_trend.png
    ├── vibration_trend.png
    ├── ball_bearing_vs_vibration.png
    ├── humidity_vs_vibration.png
    ├── distribution_analysis.png
    ├── category_analysis.png
    ├── trend_analysis.png
    ├── correlation_analysis.png
    └── class_balance_analysis.png
```

**Folder descriptions:**

- **Dataset/** — Contains the original dataset, cleaned dataset, and supporting files.
- **Notebook/** — Contains the Jupyter Notebook with the data analysis and visualization workflow.
- **Python/** — Contains the individual Python modules for loading, cleaning, exploratory analysis, and visualization.
- **Visualization/** — Stores the generated graphs as PNG files.
- **README.md** — Documents the project, setup instructions, workflow, and outputs.

*Note: `temp.txt` files are optional placeholders. Git does not track empty directories, so these files are only necessary if you want to preserve otherwise empty folders.*

## Project Workflow

### 1. Data Loading

The raw dataset is loaded into a Pandas DataFrame. The initial records, column names, data types, and dataset structure are inspected.

### 2. Data Cleaning

The data cleaning stage:

- Identifies missing values.
- Detects and removes duplicate records.
- Converts the ball-bearing, humidity, and vibration columns to numeric data types.
- Converts invalid numeric entries into missing values.
- Removes rows containing missing values.
- Saves the cleaned dataset for further analysis.

### 3. Exploratory Data Analysis

Exploratory data analysis examines the cleaned dataset using:

- Dataset dimensions and column information.
- Data type inspection.
- Descriptive statistics.
- Missing-value checks.
- Correlation analysis between numeric variables.

### 4. Data Visualization

The project generates graphs to examine sensor trends, variable relationships, distributions, category counts, and correlations.

### 5. Output Storage

The cleaned dataset is stored in `Dataset/cleaned_dataset.csv`, and the visualization images are stored in the `Visualization/` folder.

The visualization directory can be created automatically by the Python code if it does not already exist.

## Visualizations

The project includes ten visualizations.

### Existing Graphs

**1. Ball-Bearing Trend Analysis**

Displays ball-bearing measurements across observations to identify changes and variations.

**2. Humidity Trend Analysis**

Shows changes in humidity measurements across the dataset.

**3. Vibration Trend Analysis**

Displays vibration measurements across observations to help identify fluctuations and potentially unusual patterns.

**4. Ball-Bearing vs. Vibration**

A scatter plot used to explore the relationship between ball-bearing measurements and vibration.

**5. Humidity vs. Vibration**

A scatter plot used to investigate the relationship between humidity and vibration.

### Additional Graphs

**6. Distribution Analysis**

Uses histograms to examine the distribution, spread, and concentration of numeric sensor values.

**7. Category Analysis**

Groups numeric measurements into Low, Medium, and High ranges to compare the number of observations in each category.

**8. Trend Analysis**

Displays multiple sensor variables together to compare their variations across observations.

**9. Correlation Analysis**

Uses a correlation heatmap to visualize the direction and strength of linear relationships between numeric variables.

**10. Class Balance Analysis**

Displays the distribution of derived vibration categories. These categories are used for exploratory analysis and are not verified machine-failure labels.

## Installation and Setup

### Prerequisites

- Python 3.9 or later recommended
- pip package manager
- Git
- Visual Studio Code or Jupyter Notebook

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
cd Data-Analysis-Python-Project
```

Replace the placeholder with your actual GitHub repository URL.

### Step 2: Install Dependencies

```bash
pip install pandas matplotlib seaborn jupyter
```

### Step 3: Check the Dataset Path

Ensure that `raw_dataset.csv` is available inside the `Dataset/` directory.

Update the file paths in the Python scripts or notebook if necessary.

If the dataset uses semicolons as separators, use:

```python
pd.read_csv("Dataset/raw_dataset.csv", sep=";")
```

If it uses commas, use the default CSV separator instead.

### Step 4: Run the Jupyter Notebook

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
Notebook/Data-Analysis-Python-Project_with_visualizations.ipynb
```

Execute the cells sequentially.

### Step 5: Run the Python Modules

The Python directory contains separate modules for each operation. Run the relevant scripts from the project root using:

```bash
python Python/data_loading.py
python Python/data_cleaning.py
python Python/exploratory_analysis.py
python Python/data_visualization.py
```

If the scripts use relative paths, run them from the project root or adjust the paths to match the project structure.

**Note:** The four-module structure above does not include a `main.py` file. To execute all four modules through a single command, add a `main.py` entry point that imports and calls their functions in the correct order.

## Expected Outputs

After successful execution, the project produces:

- A cleaned dataset stored in the `Dataset/` directory.
- Console output showing data information and descriptive statistics.
- Five graphs showing individual trends and variable relationships.
- Five additional graphs showing distributions, categories, combined trends, correlations, and derived vibration groups.
- A `Visualization/` directory containing the saved PNG images.

## Applications

This project can be used for:

- Exploratory analysis of industrial sensor datasets.
- Understanding machine-related operating parameters.
- Investigating unusual patterns in sensor measurements.
- Studying relationships between different operating variables.
- Preparing data for future machine learning and predictive maintenance research.

## Limitations

- The current project focuses on data cleaning, exploratory analysis, and visualization.
- It does not currently train or validate a machine learning model for equipment failure prediction.
- Low, Medium, and High vibration categories are derived for analysis and should not be interpreted as verified machine health labels.
- Correlation does not establish causation.
- Identifying actual equipment faults requires suitable labelled data, validated thresholds, and domain-specific evaluation.

## Future Enhancements

- Integrate machine learning models for equipment fault prediction using labelled datasets.
- Implement anomaly detection techniques.
- Compare machine learning algorithms using appropriate evaluation metrics.
- Add interactive dashboards for real-time or historical sensor data exploration.
- Incorporate timestamp-based analysis.
- Develop validated warning thresholds based on equipment specifications.
- Automate reporting and visualization generation.

## Conclusion

Predictive Maintenance Data Analysis Using Python provides a structured workflow for loading, cleaning, exploring, and visualizing machine-related sensor data. By organizing the project into separate modules, a Jupyter Notebook, a dataset directory, and a visualization directory, it supports reproducible analysis and clear presentation of results.

The project also provides a foundation for future enhancements involving anomaly detection, advanced analytics, and validated machine learning models.

---

**Project Type:** Data Analysis and Visualization

**Programming Language:** Python

**Libraries:** Pandas, Matplotlib, Seaborn

**Domain:** Predictive Maintenance and Industrial Sensor Data Analysis
