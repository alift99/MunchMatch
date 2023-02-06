import pandas as pd

df = pd.read_csv('Restaurant_data_filtered.csv')
df = df.sort_values(by='name', axis=0)
print(len(df))
print(df['name'].nunique())
df.to_csv('Restaurant_data_filtered_sorted.csv', index=False)