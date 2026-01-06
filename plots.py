import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
#bar
plt.bar(df['Product'], df['Sales'])
plt.title("Bar Chart")
plt.show()
#line
plt.plot(df['Product'], df['Sales'])
plt.title("Line Chart")
plt.show()
#pie
plt.pie(df['Sales'], labels=df['Product'])
plt.title("Pie Chart")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Histogram
plt.hist(df['Age'])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.scatter(df['Age'], df['Marks'])
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Age vs Marks")
plt.show()
