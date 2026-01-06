#Exp. 6 Write a program in Python to identify and handle missing values in dataset.
import pandas as pd
df = pd.read_csv("/Users/riiyachoudhary/Downloads/student_data_missing.csv")
print("original data:\n",df)
# Handling missing values
df_filled = df.fillna(df.mean(numeric_only=True)) # Fill numeric NaN with mean
df_filled.fillna("Unknown") # Fill non-numeric NaN with 'Unknown'
print("\nAfter Handling Missing Values:\n",df_filled)
