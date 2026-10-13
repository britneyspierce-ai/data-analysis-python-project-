[README.md](https://github.com/user-attachments/files/33277133/README.md)

**Title:**

Predictive Maintenance and Failure Prediction for Industrial Machinery

**Project Overview**

Predictive Maintenance Data Analysis Using Python is a data analysis project designed to process, clean, explore, and visualize machine-related sensor data. The project focuses on analyzing parameters such as ball-bearing measurements, humidity, and vibration to understand data distributions, identify trends, examine relationships between variables, and investigate potentially abnormal operating patterns.

The project implements a modular data analysis workflow using Python and libraries such as Pandas, Matplotlib, and Seaborn. It automates the major stages of data analysis, from loading the raw dataset to generating meaningful visualizations. All generated graphs are automatically stored in a dedicated "Visualization" folder, making the results easy to access and review.
 
**Problem Statement**

To develop a Python-based data analysis system that cleans predictive maintenance sensor data and visualizes distributions, trends, categories, and relationships to support the investigation of potentially abnormal machine operating patterns.

**Project Objectives**

- Load and process the predictive maintenance dataset using Python.
- Identify and handle missing values, duplicate records, and invalid numeric entries.
- Perform exploratory data analysis to understand the dataset's structure and statistical characteristics.
- Analyze ball-bearing measurements, humidity, and vibration patterns.
- Generate visualizations to examine distributions, trends, correlations, and value categories.
- Automate the complete data analysis workflow through a single execution file.
- Save the cleaned dataset and generated graphs for further analysis and reporting.

**Technologies Used**

Technology-- Purpose

Python-- Core programming language

Pandas-- Data loading, manipulation, cleaning, and statistical analysis

Matplotlib-- Creating line charts and scatter plots

Seaborn-- Creating distribution plots and correlation heatmaps

OS module-- Creating directories and managing output file paths

Jupyter Notebook-- Interactive development and analysis

**Project Structure**

Python/
├── main.py
├── data_loading.py
├── data_cleaning.py
├── exploratory_analysis.py
├── data_visualization.py
├── README.md
├── predictive-maintenance-dataset.csv
├── predictive-maintenance-cleaned.csv
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

Note: The CSV files and visualization images are generated or supplied at runtime. They may not exist in a fresh checkout until the project is executed.

**Project Workflow**

The project follows a structured data analysis pipeline.

**1. Data Loading**

The source CSV dataset is imported using Pandas. Initial records, column information, and data types are inspected to understand the dataset before processing.

**2. Data Cleaning**

The data cleaning stage performs the following operations:

- Checks for missing values.
- Identifies and removes duplicate records.
- Converts the ball-bearing, humidity, and vibration columns into numeric format.
- Handles invalid numeric values by converting them into missing values.
- Removes rows containing missing values.
- Saves the cleaned dataset for subsequent analysis.

**3. Exploratory Data Analysis**

Exploratory data analysis is used to understand the characteristics of the cleaned dataset. It includes:

- Examining dataset dimensions and column names.
- Inspecting data types.
- Calculating descriptive statistics.
- Reviewing missing-value counts.
- Studying relationships between numeric variables.

**4. Data Visualization**

The project generates ten visualizations to support the interpretation of the dataset.

**5. Automated Execution**

The "main.py" file acts as the main entry point and connects the individual Python modules. Running this file executes the data loading, cleaning, exploratory analysis, and visualization stages in sequence.

**Visualizations**

The project generates the following graphs.

Existing Visualizations

**1. Ball-Bearing Trend Analysis**

Displays ball-bearing measurements across observations to help identify changes, variations, and unusual values.

**2. Humidity Trend Analysis**

Shows the variation in humidity measurements across the dataset.

**3. Vibration Trend Analysis**

Displays vibration values across observations to help examine fluctuations and potentially unusual patterns.

**4. Ball-Bearing vs Vibration**

A scatter plot used to investigate the relationship between ball-bearing measurements and vibration.

**5. Humidity vs Vibration**

A scatter plot used to examine whether humidity and vibration exhibit any observable relationship.

**Additional Visualizations**

**6. Distribution Analysis**

Histograms illustrate the distributions of numeric variables, helping reveal their spread, concentration, and potential extreme values.

**7. Category Analysis**

Groups numeric measurements into categories such as Low, Medium, and High to compare the number of observations in each range.

**8. Trend Analysis**

Displays multiple sensor variables together to provide an overall view of how their values vary across observations.

**9. Correlation Analysis**

A correlation heatmap summarizes the linear relationships between numeric variables and helps identify positive or negative associations.

**10. Class Balance Analysis**

Displays the distribution of derived vibration categories to show how observations are distributed among the defined groups.

All graphs are saved as PNG images inside the "Visualization" folder. The code creates this folder automatically if it does not already exist.

**Installation and Setup**

**Prerequisites**

- Python 3.9 or later recommended
- pip package manager
- Git
- A compatible Python editor, such as VS Code, or Jupyter Notebook

**Step 1: Clone the Repository**

git clone <your-repository-url>
cd <your-repository-folder>

Replace the placeholders with your actual GitHub repository URL and folder name.

**Step 2: Install Dependencies**

pip install pandas matplotlib seaborn

**Step 3: Add the Dataset**

Place the source dataset in the project directory and ensure its filename and path match the values specified in the code.

The original data-loading implementation uses a semicolon (";") as the CSV separator. If your dataset uses commas, update the separator accordingly.

**Step 4: Run the Project**

From the project directory, execute:

python main.py

The program will load the dataset, clean the data, perform exploratory analysis, generate the visualizations, and save the outputs.

**Expected Outputs**

After successful execution, the project produces:

- A cleaned CSV dataset.
- Console output containing data information and descriptive statistics.
- Five existing graphs showing trends and relationships.
- Five additional graphs covering distributions, categories, combined trends, correlations, and derived vibration classes.
- A "Visualization" folder containing the generated PNG files.

**Applications**

This project can support:

- Initial analysis of industrial sensor datasets.
- Exploratory analysis of equipment operating parameters.
- Identification of unusual patterns for further investigation.
- Visualization of relationships between machine-related variables.
- Preparation of data for future machine learning and predictive maintenance research.

**Future Enhancements**

Potential extensions include:

- Developing machine learning models for equipment fault prediction using labelled historical data.
- Comparing classification and regression algorithms where appropriate.
- Implementing anomaly detection techniques.
- Establishing domain-validated thresholds for abnormal operating conditions.
- Adding interactive dashboards for exploring sensor data.
- Integrating time-stamped data for temporal analysis.
- Evaluating model performance using suitable metrics and independent test data.

**Limitations**

This project currently focuses on data cleaning, exploratory analysis, and visualization. It does not train or validate a machine learning model for predicting equipment failure.

The Low, Medium, and High vibration categories are derived for analysis and should not be interpreted as verified machine health or failure labels. Similarly, correlations and visual patterns do not independently establish causation or confirm equipment faults.

**Conclusion**

Predictive Maintenance Data Analysis Using Python provides a structured and automated approach to preparing, exploring, and visualizing machine-related sensor data. By combining data cleaning, descriptive statistics, and multiple visualization techniques, the project makes it easier to understand the dataset and identify patterns that may warrant further investigation.

The modular design and automated execution workflow also provide a foundation for extending the project with advanced analytics, anomaly detection, and validated machine learning models in the future.

---

**Project Category:** Data Analysis / Predictive Maintenance

**Primary Language:** Python

**Key Libraries:** Pandas, Matplotlib, Seaborn
## Visualization output

Running `python main.py` creates a `Visualization/` folder automatically and saves all existing plots plus these additional plots: `distribution_analysis.png`, `category_analysis.png`, `trend_analysis.png`, `correlation_analysis.png`, and `class_balance_analysis.png`. If a graph cannot be meaningfully calculated because the dataset lacks the required column types, a labelled placeholder image is saved so all requested filenames are present.

