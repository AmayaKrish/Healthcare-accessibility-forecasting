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


# Progress Update – August 4, 2026

## Overview

Today's work focused on expanding the healthcare dataset and conducting the initial exploratory data analysis (EDA) for Germany and India. Two additional healthcare expenditure indicators were integrated into the master dataset, and comparative trend visualizations were created to begin exploring changes in healthcare accessibility and health outcomes over time.

---

## Completed Tasks

### Data Integration

- Added **Current Health Expenditure (% of GDP)** from the World Bank.
- Added **Out-of-Pocket Health Expenditure (% of Current Health Expenditure)** from the World Bank.
- Filtered both datasets to include only **Germany** and **India**.
- Selected data covering the period **1990–2024**.
- Filled missing values using **Linear Regression**.
- Merged the new variables into the master dataset.
- Saved the updated dataset as `master_dataset_updated.csv`.

---

### Exploratory Data Analysis (EDA)

Created comparative line charts for the following indicators:

#### Healthcare Accessibility

- Physician Density (per 1,000 population)
- Hospital Beds (per 1,000 population)
- Current Health Expenditure (% of GDP)
- Out-of-Pocket Health Expenditure (% of Current Health Expenditure)

#### Health Outcomes

- Life Expectancy at Birth
- Diabetes Prevalence
- Probability of Dying from Non-Communicable Diseases (NCDs)

---

### Figures

All visualizations were exported to the `figures/` directory as high-resolution PNG files.

```text
figures/
│
├── physician_density_trend.png
├── hospital_beds_trend.png
├── health_expenditure_trend.png
├── out_of_pocket_trend.png
├── life_expectancy_trend.png
├── diabetes_prevalence_trend.png
└── ncd_mortality_trend.png
```

---

## Skills Applied

- Data Cleaning
- Data Transformation
- Data Integration
- Missing Value Imputation (Linear Regression)
- Exploratory Data Analysis (EDA)
- Time Series Visualization
- Python (Pandas & Matplotlib)

---

## Next Steps

- Interpret trends observed in each visualization.
- Perform correlation analysis between healthcare accessibility indicators and health outcomes.
- Generate correlation heatmaps and scatterplots.
- Begin drafting the Results and Discussion sections based on the exploratory findings.

---

## Git Commit

```bash
git add .
git commit -m "Completed exploratory data analysis and integrated healthcare expenditure datasets"
git push origin main
```

# Progress Update – August 4, 2026

## Overview

Today's work focused on expanding the healthcare dataset and conducting the initial exploratory data analysis (EDA) for Germany and India. Two additional healthcare expenditure indicators were integrated into the master dataset, and comparative trend visualizations were created to begin exploring changes in healthcare accessibility and health outcomes over time.

---

## Completed Tasks

### Data Integration

- Added **Current Health Expenditure (% of GDP)** from the World Bank.
- Added **Out-of-Pocket Health Expenditure (% of Current Health Expenditure)** from the World Bank.
- Filtered both datasets to include only **Germany** and **India**.
- Selected data covering the period **1990–2024**.
- Filled missing values using **Linear Regression**.
- Merged the new variables into the master dataset.
- Saved the updated dataset as `master_dataset_updated.csv`.

---

### Exploratory Data Analysis (EDA)

Created comparative line charts for the following indicators:

#### Healthcare Accessibility

- Physician Density (per 1,000 population)
- Hospital Beds (per 1,000 population)
- Current Health Expenditure (% of GDP)
- Out-of-Pocket Health Expenditure (% of Current Health Expenditure)

#### Health Outcomes

- Life Expectancy at Birth
- Diabetes Prevalence
- Probability of Dying from Non-Communicable Diseases (NCDs)

---

### Figures

All visualizations were exported to the `figures/` directory as high-resolution PNG files.

```text
figures/
│
├── physician_density_trend.png
├── hospital_beds_trend.png
├── health_expenditure_trend.png
├── out_of_pocket_trend.png
├── life_expectancy_trend.png
├── diabetes_prevalence_trend.png
└── ncd_mortality_trend.png
```

---

## Skills Applied

- Data Cleaning
- Data Transformation
- Data Integration
- Missing Value Imputation (Linear Regression)
- Exploratory Data Analysis (EDA)
- Time Series Visualization
- Python (Pandas & Matplotlib)

---

## Next Steps

- Interpret trends observed in each visualization.
- Perform correlation analysis between healthcare accessibility indicators and health outcomes.
- Generate correlation heatmaps and scatterplots.
- Begin drafting the Results and Discussion sections based on the exploratory findings.

---

## Git Commit

```bash
git add .
git commit -m "Completed exploratory data analysis and integrated healthcare expenditure datasets"
git push origin main
```
