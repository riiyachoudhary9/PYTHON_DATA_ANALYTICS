import pandas as pd
df_csv=pd.read_csv("/Users/riiyachoudhary/Downloads/username.csv")
print("CSV Data:\n",df_csv.head())
df_xlsx=pd.read_excel("/Users/riiyachoudhary/Downloads/employs.xlsx")
print("nExcel Data:\n",df_xlsx.head())







