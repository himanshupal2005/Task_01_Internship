import pandas as pd

# Load the dataset
df = pd.read_csv("Mall_customers.csv")

# Clean column names first (lowercase and remove spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Check and handle missing values
# Example: Fill missing age with median
df['age'] = df['age'].fillna(df['age'].median())
df['annual_income_(k$)'] = df['annual_income_(k$)'].fillna(df['annual_income_(k$)'].median())
df['spending_score'] = df['spending_score'].fillna(df['spending_score'].median())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Standardize gender values
df['gender'] = df['gender'].str.strip().str.lower()

# Convert joining date to datetime
df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')

# Ensure correct data types
if df['age'].dtype != 'int64':
    df['age'] = df['age'].astype(int)

# Preview cleaned dataset
print(df.head())

# Export cleaned dataset
df.to_csv("mall_customers_cleaned.csv", index=False)

''' 
1. Standardized all column names to lowercase and replaced spaces with underscores.

2. Filled missing values in age, annual_income_(k$), and spending_score using the median of each column.

3. Duplicate rows were identified and removed using drop_duplicates().

4. Cleaned the gender column by stripping spaces and converting all entries to lowercase (male, female).

5. Converted joining_date to proper datetime format using pd.to_datetime() with error handling.

6. Ensured age was stored as an integer type after filling missing values.

7. The cleaned dataset was saved as mall_customers_cleaned.csv.'''

