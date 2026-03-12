import pandas as pd
import csv

# Create a Series
s = pd.Series([1, 2, 3, 4, 5])
print(s)

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
df = pd.DataFrame(data)
# print(df)

# Save DataFrame to CSV file
# df.to_csv('01_fileControl\\testfold1\\testfold1_data_output.csv', index=False, encoding='utf-8-sig') 
# print("DataFrame saved to CSV file.")
# print("=" * 50)

# Read CSV file into a DataFrame
# df_csv = pd.read_csv('01_fileControl\\testfold1\\testfold1_data.csv', encoding='utf-8-sig')
# print(df_csv)


