import pandas as pd
from statistics import mode

df = pd.read_csv("data.csv")

mean_val = df['Marks'].mean()
median_val = df['Marks'].median()
mode_val = df['Marks'].mode()[0]

print("Mean =", mean_val)
print("Median =", median_val)
print("Mode =", mode_val)


import pandas as pd

df = pd.read_csv("data.csv")

data = df['Marks']

range_val = data.max() - data.min()
variance_val = data.var()
std_dev_val = data.std()

print("Range =", range_val)
print("Variance =", variance_val)
print("Standard Deviation =", std_dev_val)
