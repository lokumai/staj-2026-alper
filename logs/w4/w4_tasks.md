# Week 4 – Mini-Project: TCDD Train Delay Prediction & Data Pipeline

## 📖 Background & Context

In railway operations like TCDD (*Türkiye Cumhuriyeti Devlet Demiryolları*), train arrival delays cause scheduling ripple effects, increase operational costs, and lower passenger satisfaction. Predicting delays before or during a journey allows operations teams to dynamically adjust schedules, optimize track utilization, and notify passengers proactively.

In previous weeks, you worked with clean, single-file educational datasets (like Iris or Diabetes) where every column was pre-selected and ready to use. 

**In real-world engineering projects, data is rarely handed to you on a silver platter.** Data lives across multiple database tables filled with administrative metadata, missing records, bad sensor data, and inconsistent text formatting. This week, you will take on the role of an ML Engineer at Intellica building an end-to-end data processing and prediction pipeline for TCDD.

---

## 🎯 Project Goal

Your goal is to build an **end-to-end machine learning pipeline** in a Jupyter Notebook ([`projects/w4_tcdd_delay_prediction.ipynb`](file:///home/amirkia/Desktop/staj-2026-alper/projects/w4_tcdd_delay_prediction.ipynb)) that:
1. Inspects and merges 3 separate relational database tables from [`projects/tcdd_data/`](file:///home/amirkia/Desktop/staj-2026-alper/projects/tcdd_data).
2. Filters out irrelevant database noise and cleans real-world data quality issues.
3. Engineers domain-specific features and explores what factors drive delays.
4. Trains, evaluates, and fine-tunes multiple ML models to accurately predict train arrival delays in minutes (`gecikme_suresi_dk`).

---

## 🗄️ Scenario & Data Overview

You are provided with 3 database dumps in [`projects/tcdd_data/`](file:///home/amirkia/Desktop/staj-2026-alper/projects/tcdd_data):

1. **`seferler_log.csv`**: Contains operational records of individual train trips.
2. **`tren_bakim_gecmisi.csv`**: Contains technical specs and maintenance records for locomotives in the fleet.
3. **`hat_bilgileri.csv`**: Contains route details, distance, and track infrastructure information across Turkey.

### 💡 Hints for Your Data Investigation
* **Not all columns are relevant:** Database tables often store administrative metadata (e.g. phone numbers, app versions, staff names) that have no predictive value for ML. Inspect the columns and keep only what matters.
* **Tables need to be connected:** Look for common identifier keys across the 3 files so you can join them into one unified dataset for modeling.
* **Expect real-world data noise:** During your exploratory analysis, look out for:
  * Missing (`NaN`) values in technical metrics.
  * System error codes (e.g. negative values or invalid entries).
  * Inconsistent string casing or typos in station names and weather conditions.
  * Unstandardized date/time formats.

---

## 🛠️ Project Phases & Workflow

### Phase 1: Schema Audit & Relational Joining (Day 1)
* Load all 3 CSV files into pandas DataFrames.
* Inspect data types, column names, and sample rows (`info()`, `head()`).
* Identify useful feature columns vs. irrelevant administrative noise.
* Discover key relationships and merge the 3 tables into a single master DataFrame.

### Phase 2: Data Cleaning & Preprocessing (Day 2)
* Investigate distributions and summary stats (`describe()`, `isna().sum()`).
* Handle missing values with sensible imputation strategies.
* Filter out invalid records and outlier error codes.
* Parse date strings into datetime objects and standardize inconsistent text columns.

### Phase 3: Exploratory Data Analysis & Feature Engineering (Day 3)
* Extract new time features (e.g., departure hour, day of week, weekend indicator).
* Create domain features (e.g., calculated speed/distance ratios).
* Generate visual plots (histograms, scatter plots, correlation heatmaps) to discover key delay drivers (e.g. weather impact, peak traffic hours, train age).

### Phase 4: Model Training, Selection & Fine-Tuning (Day 4)
* Split the dataset into 80% Training and 20% Testing sets.
* Train and compare **at least 3 different regression algorithms**:
  * **Linear Models:** e.g., `LinearRegression`, `Ridge`, or `Lasso` (fast, interpretable baseline).
  * **Tree-Based Models:** e.g., `DecisionTreeRegressor` (captures non-linear relationships).
  * **Ensemble Models:** e.g., `RandomForestRegressor` or `GradientBoostingRegressor` / `HistGradientBoostingRegressor` (handles complex interactions).
* Tune key hyperparameters (e.g., `max_depth`, `n_estimators`, `alpha`) to prevent overfitting and boost performance.
* Evaluate test performance using 3 key metrics:
  * **MAE** (Mean Absolute Error) — average error in minutes.
  * **RMSE** (Root Mean Squared Error) — penalizes large delay errors.
  * **$R^2$ Score** — proportion of variance explained by the model.

---

## 📋 Expected Deliverables

1. **Jupyter Notebook:** [`projects/w4_tcdd_delay_prediction.ipynb`](file:///home/amirkia/Desktop/staj-2026-alper/projects/w4_tcdd_delay_prediction.ipynb) containing clean, commented code and visualization plots.
2. **Completed Internship Log:** Fill in your findings in the section below.

---

## 📝 Alper's Internship Log

*(Document your insights as you progress through the project)*

### 1. Data Audit & Schema Joining
* **Which columns did you keep, which did you drop as noise, and why?**
  * *Notes:*
* **How did you join the 3 database tables?**
  * *Notes:*

### 2. Data Cleaning Discoveries
* **What data quality issues (outliers, formatting, missing data) did you find, and how did you resolve them?**
  * *Notes:*

### 3. Feature Engineering & Key EDA Findings
* **What new features did you engineer?**
  * *Notes:*
* **What are the top 3 factors that cause train delays based on your EDA?**
  * *Notes:*

### 4. Model Benchmark Comparison

| Model Name | Hyperparameters | Test MAE (min) | Test RMSE (min) | Test $R^2$ |
|---|---|---|---|---|
| Linear Regression | Default | | | |
| Decision Tree | | | | |
| Random Forest / Gradient Boosting | | | | |

* **Which model performed best, and why?**
  * *Notes:*

### 5. Final Questions & Reflection
* 
