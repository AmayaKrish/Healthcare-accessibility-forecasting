# Healthcare-accessibility-forecasting
Master's thesis project analyzing healthcare accessibility and health outcomes in Germany and India using World Bank and WHO datasets. The project includes data cleaning, exploratory data analysis, regression modeling, and forecasting to evaluate long-term healthcare trends and future outcomes through 2050.
# 📊 Project Progress Update – Session 1

**Date:** 03 August 2026

## ✅ Tasks Completed

### 1. Validation of Master Dataset

Validated the `master_dataset.csv` to ensure data quality before analysis.

The following validation checks were completed:

* Reviewed the dataset structure using `head()` and `info()`.
* Checked for missing values across all variables.
* Identified and removed duplicate records where necessary.
* Verified data types:

  * `Year` stored as an integer.
  * All healthcare indicators stored as numeric (`int`/`float`).
* Confirmed that the dataset contains only:

  * Germany
  * India
* Verified that both countries cover the same year range.
* Saved the cleaned dataset as `master_dataset_final.csv`.

---

### 2. Exploratory Data Analysis (EDA)

Performed Exploratory Data Analysis (EDA) separately for the Germany and India datasets.

The following checks were completed for each dataset:

* Dataset structure (`head()` and `info()`).
* Missing value analysis.
* Duplicate record detection.
* Data type verification.
* Year range validation.

---

### 3. Descriptive Statistics

Generated descriptive statistics separately for the Germany and India datasets.

For each numeric healthcare variable, calculated:

* Mean
* Median
* Standard Deviation
* Minimum
* Maximum

The results were exported as:

* `Germany_Descriptive_Statistics.csv`
* `India_Descriptive_Statistics.csv`

---

### 4. Variable Comparison Summary

Created a comparison table using the mean values from both datasets.

The table includes:

* Variable
* Germany Mean
* India Mean
* Initial Observation

The comparison table was exported as:

* `Variable_Summary_Table.csv`

This table will be incorporated into the **Results** chapter of the dissertation.

---

## 📁 Files Generated

* `master_dataset_final.csv`
* `Germany_Descriptive_Statistics.csv`
* `India_Descriptive_Statistics.csv`
* `Variable_Summary_Table.csv`

---

## 🛠️ Tools Used

* Python
* Jupyter Notebook
* Pandas

---

## 🚀 Next Steps

* Create visualizations (histograms, box plots, line charts, and correlation heatmaps).
* Perform comparative analysis between Germany and India.
* Conduct statistical testing and predictive modelling.
* Integrate tables and figures into the dissertation's Results chapter.
