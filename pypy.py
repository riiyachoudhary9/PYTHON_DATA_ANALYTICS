#Exp. 7 Write a program in Python to perform basic exploratory data analysis
(EDA).
Aim: To conduct basic EDA for understanding the structure and summary of a dataset.
Objectives:
●
●
●
●
Summarize data using .describe() and .info().
Check data types, unique values, and distributions.
Identify patterns, outliers, or trends.
Build foundational insights for advanced analysis.



import pandas as pd
df = pd.read_csv("/Users/riiyachoudhary/Downloads/student_data.csv")
print("First 5 rows:\n", df.head())
print("\nShape of dataset:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nSummary statistics:\n", df.describe())
print("\nMissing values:\n", df.isnull().sum())
