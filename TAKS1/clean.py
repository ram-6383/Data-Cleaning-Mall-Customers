import pandas as pd

# Load the dataset
df = pd.read_csv("TAKS1\Mall_Customers (1).csv")

# 1. Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# 2. Check for duplicate rows
duplicate_count = df.duplicated().sum()
print("\nDuplicate Rows Found:", duplicate_count)

# 3. Standardize 'Gender' values
print("\nUnique Genders Before Standardization:", df["Gender"].unique())

# 4. Rename columns for clarity and consistency
df.rename(columns={
    "CustomerID": "customer_id",
    "Gender": "gender",
    "Age": "age",
    "Annual Income (k$)": "annual_income_k",
    "Spending Score (1-100)": "spending_score"
}, inplace=True)

# 5. Drop duplicate rows
df.drop_duplicates(inplace=True)

# 6. Confirm correct data types
print("\nData Types:\n", df.dtypes)

# 7. Save the cleaned dataset
df.to_csv("Mall_Customers_Final_Cleaned.csv", index=False)
print("\n Cleaned dataset saved as 'Mall_Customers_Final_Cleaned.csv'")
