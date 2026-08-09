# Week 4 – Mini-Project: TCDD Train Delay Prediction & Enterprise Data Pipeline

## 📖 Background & Context

In large national railway organizations like TCDD (*Türkiye Cumhuriyeti Devlet Demiryolları*), train arrival delays ripple across thousands of kilometers of track, impacting logistics, passenger satisfaction, and operating margins. Accurately predicting delays allows centralized dispatching teams to adjust schedules, optimize track bottlenecks, and notify passengers dynamically.

In previous weeks, you worked with clean, single-file educational datasets (like Iris or Diabetes) containing fewer than 500 rows and pre-selected features.

**In enterprise engineering projects, data is vastly larger, wider, and messier.** Data is stored across relational database dumps containing tens of thousands of records and dozens of administrative columns (staff IDs, equipment serial numbers, maintenance budget files) that have zero predictive value for ML. 

This week, you will take on the role of an ML Engineer at Intellica building a production-grade data processing and prediction pipeline on an enterprise dataset dump from TCDD.

---

## 🎯 Project Goal

Your goal is to build an **end-to-end machine learning pipeline** in a Jupyter Notebook ([`projects/w4_tcdd_delay_prediction.ipynb`](file:///home/amirkia/Desktop/staj-2026-alper/projects/w4_tcdd_delay_prediction.ipynb)) that:
1. Inspects and merges **3 large enterprise database tables** (~12,000 trip logs, 250 locomotives, 40 routes, 48 total columns) from [`projects/tcdd_data/`](file:///home/amirkia/Desktop/staj-2026-alper/projects/tcdd_data).
2. Performs a schema audit to drop administrative metadata noise and isolate true predictive signals.
3. Resolves real-world data quality issues (missing technical metrics, negative sensor values, corrupt error codes, mixed date strings, and station name variations).
4. Engineers domain features (temporal patterns, weather severity, technical wear factors).
5. Trains, tunes, and compares multiple ML models to predict arrival delays in minutes (`gecikme_suresi_dk`).

---

## 🗄️ Scenario & Data Overview

You are provided with 3 raw database dumps in [`projects/tcdd_data/`](file:///home/amirkia/Desktop/staj-2026-alper/projects/tcdd_data):

1. **`seferler_log.csv`** (12,000 trip records, 21 columns): Operational logs for train journeys across 2025–2026.
2. **`tren_bakim_gecmisi.csv`** (250 locomotives, 14 columns): Fleet specs, cumulative mileage, brake/wheel wear metrics, and maintenance logs.
3. **`hat_bilgileri.csv`** (40 railway routes, 13 columns): Infrastructure parameters, track types, elevation changes, bends, and speed limits.

### 💡 Hints for Your Data Investigation
* **Separate Signal from Administrative Noise:** Enterprise tables contain many non-predictive metadata fields (e.g., ticket scanner firmware versions, driver staff IDs, depot manager names, supplier codes, budget numbers). Audit all 48 columns and drop the noise.
* **Discover Relational Joins:** Find key identifier columns shared across `seferler_log`, `tren_bakim_gecmisi`, and `hat_bilgileri` to join them into a single consolidated dataset.
* **Audit Data Hygiene:** Scale creates more data anomalies. Look out for:
  * Missing (`NaN`) technical scores or environmental readings.
  * Invalid records or corrupt system error codes (e.g. negative values where impossible).
  * Inconsistent string casing and typos in weather and station names.
  * Mixed ISO (`YYYY-MM-DD`) and European (`DD.MM.YYYY`) date string formats.

---

## 🛠️ Project Phases & Workflow

### Phase 1: Schema Audit & Relational Joining (Day 1)
* Load all 3 CSV files into pandas DataFrames and inspect schemas (`info()`, `shape`, `head()`).
* Document which of the 48 columns are useful feature candidates vs. administrative noise.
* Discover primary/foreign keys and merge the 3 tables into a unified master DataFrame (12,000 rows).

### Phase 2: Data Cleaning & Preprocessing (Day 2)
* Check summary statistics (`describe()`, `isna().sum()`) across all numerical and categorical fields.
* Handle missing values (`NaN`) using appropriate imputation strategies.
* Clean corrupted system entries (e.g. invalid negative passenger counts or error codes).
* Parse date strings into datetime objects and resolve text/station string variations.

### Phase 3: Exploratory Data Analysis & Feature Engineering (Day 3)
* Engineer temporal features (departure hour, day of week, seasonal flags).
* Create physical domain ratios (e.g., estimated journey duration, wear-to-age ratios).
* Produce visualizations (correlation heatmaps, box plots, scatter plots) to uncover the top drivers of delay.

### Phase 4: Model Training, Selection & Fine-Tuning (Day 4)
* Split the dataset into 80% Training and 20% Testing sets.
* Train and compare **at least 3 different regression algorithms**:
  * **Linear Models:** e.g., `LinearRegression`, `Ridge`, or `Lasso`.
  * **Tree-Based Models:** e.g., `DecisionTreeRegressor`.
  * **Ensemble Models:** e.g., `RandomForestRegressor` or `GradientBoostingRegressor` / `HistGradientBoostingRegressor`.
* Tune key hyperparameters (`max_depth`, `n_estimators`, `learning_rate`) to prevent overfitting.
* Benchmark model performance using **MAE**, **RMSE**, and **$R^2$ Score**.

---

## 📋 Expected Deliverables

1. **Jupyter Notebook:** [`projects/w4_tcdd_delay_prediction.ipynb`](file:///home/amirkia/Desktop/staj-2026-alper/projects/w4_tcdd_delay_prediction.ipynb) with clean code, comments, and plots.
2. **Completed Internship Log:** Fill in your findings in the section below.

---

## 📝 Alper's Internship Log

*(Document your insights as you progress through the project)*

### 1. Data Audit & Schema Joining
* **Out of 48 total columns across the 3 tables, which columns did you keep as features, which did you drop as administrative noise, and why?**
  * *Notes:*
* **How did you join the 3 database tables?**
  * *Notes:*

### 2. Data Cleaning Discoveries
* **What data quality issues (outliers, formatting, missing data) did you discover in the 12,000 records, and how did you fix them?**
  * *Notes:*

### 3. Feature Engineering & Key EDA Findings
* **What new features did you engineer?**
  * *Notes:*
* **What are the top factors that cause train delays based on your EDA?**
  * *Notes:*

### 4. Model Benchmark Comparison

| Model Name | Key Hyperparameters | Test MAE (min) | Test RMSE (min) | Test $R^2$ |
|---|---|---|---|---|
| Linear Regression | Default | | | |
| Decision Tree | | | | |
| Random Forest / Gradient Boosting | | | | |

* **Which model performed best, and why?**
  * *Notes:*

### 5. Final Reflection & Questions
* 
