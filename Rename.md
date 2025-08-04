# Data Cleaning – Mall Customers Dataset

This project focuses on **data cleaning and preprocessing** of the Mall Customers dataset. It includes removal of duplicates, handling missing values, and feature standardization, all using **Python and Pandas**. Clean data is essential for building accurate and reliable data models, especially in customer segmentation, behavior analysis, and marketing strategies.

---

## Dataset Overview

- **Original Dataset Name:** `Mall_Customers.csv`
- **Source:** [Kaggle - Mall Customers Dataset](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial)
- **Attributes:**
  - `CustomerID`: Unique identifier
  - `Gender`: Male or Female
  - `Age`: Age of the customer
  - `Annual Income (k$)`: Annual income in $1000s
  - `Spending Score (1-100)`: Score assigned based on customer behavior and spending nature


## Tasks Performed

The script `data_cleaning.py` performs the following steps:

1. **Loading Dataset**
   - Reads the original CSV file using `pandas`.

2. **Initial Data Inspection**
   - Displays shape, data types, and a snapshot of the dataset.
   - Checks for missing values and duplicates.

3. **Duplicate Removal**
   - Identifies and removes duplicate records using `df.drop_duplicates()`.

4. **Missing Value Handling**
   - Detects and fills or drops missing values depending on the context.

5. **Data Type Corrections**
   - Converts data types where appropriate (e.g., categorical encoding).

6. **Outlier Detection (Optional)**
   - Can be extended to visualize and handle outliers using IQR or Z-score.

7. **Final Verification**
   - Prints the cleaned dataset shape and sample data.

8. **Export Cleaned Data**
   - Saves the cleaned data as `Mall_Customers_Final_Cleaned.csv`.

