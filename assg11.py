


#Aim: To compute measures of dispersion in numeric datasets.
#Objectives:

#Calculate range (max – min).

#Use numpy or statistics to compute variance and standard deviation.

#Understand the spread of data points around the mean.

#Interpret dataset variability.













import pandas as pd
df = pd.read_csv("/Users/riiyachoudhary/Downloads/scores.csv") # Assume 'Score' column exists
range_val = df["Score"].max() - df["Score"].min()
variance_val = df["Score"].var()
std_dev_val = df["Score"].std()
print("Range:",range_val)
print("Variance:", variance_val)
print("Standard Deviation:", std_dev_val)
