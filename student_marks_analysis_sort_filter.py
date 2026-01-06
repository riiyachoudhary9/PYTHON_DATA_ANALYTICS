import pandas as pd

data = {
    'Name': ['Aman', 'Riya', 'Karan', 'Neha'],
    'Marks': [78, 92, 65, 88],
    'Age': [20, 19, 21, 20]
}

df = pd.DataFrame(data)

# Sorting
sorted_df = df.sort_values(by='Marks', ascending=False)

# Filtering (students with marks > 80)
filtered_df = df[df['Marks'] > 80]

# Simple formula (add 5 bonus marks)
df['Updated_Marks'] = df['Marks'] + 5

print(df)
print(sorted_df)
print(filtered_df)
