
#calculate and visualize correlation between two variables.



import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

correlation = df['Age'].corr(df['Marks'])
print("Correlation =", correlation)

plt.scatter(df['Age'], df['Marks'])
plt.title("Correlation Plot: Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()
