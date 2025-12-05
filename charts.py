#Exp. 8 Write a program in Python to create a bar chart, line chart, and pie chart
#from a given dataset.
#Aim: To visualize dataset information using different chart types.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/riiyachoudhary/Downloads/sales.csv")  # Assume 'Month' and 'Sales' columns exist


# Pie chart
plt.pie(df["Sales"], labels=df["Month"], autopct='%1.1f%%')
plt.title("Sales Distribution - Pie Chart")
plt.show()

# Line chart
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Pie chart
plt.pie(df["Sales"], labels=df["Month"], autopct='%1.1f%%')
plt.title("Sales Distribution - Pie Chart")
plt.show()
