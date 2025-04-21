# Task_01_Internship
# Task 1: Data Cleaning and Preprocessing

## Objective:
To clean and prepare a raw customer dataset using Python and Pandas. This includes handling missing values, removing duplicates, standardizing formats, and preparing the data for analysis.

## What I Did:
- Take a Raw data set in file `Mall_customers.csv`
- Renamed columns to lowercase with underscores for consistency
- Handled missing values in:
  - `age`, `annual_income_(k$)`, `spending_score` using **median**
- Removed duplicate rows
- Standardized the `gender` column (e.g., 'MALE', ' female ' → 'male', 'female')
- Converted `joining_date` to proper datetime format
- Ensured `age` column was converted to integer
- Exported the cleaned dataset as `mall_customers_cleaned.csv`

## Files Included:

- `01_task.py` – Python script for the full cleaning process
- `Mall_customers.csv` – Raw input data
- `mall_customers_cleaned.csv` – Final cleaned dataset

## Tools Used:
- Python
- Pandas
- Google - Reference for taking a raw dataset
- Excel - to put dataset in it, then copy it into csv

## Note:
This task helped me gain hands-on experience in real-world data cleaning using Python — a vital step before any data analysis or modeling.

