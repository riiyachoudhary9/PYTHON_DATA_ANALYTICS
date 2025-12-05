#identify and handle missing values
import pandas as pd

df = pd.read_csv("data.csv")

# Identify missing values
print(df.isnull().sum())

# Fill missing values
df_filled = df.fillna(df.mean(numeric_only=True))

# Drop missing rows
df_dropped = df.dropna()

print(df_filled)
print(df_dropped)

#EDA

import pandas as pd

df = pd.read_csv("data.csv")

print(df.info())#basic info of data
print(df.describe())#statistical summary like std deviavtion , mean,count etc
print(df.corr())#see correlations
print(df.nunique())#telll how many unique value category exists


