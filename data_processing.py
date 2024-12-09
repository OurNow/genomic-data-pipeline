# data_processing.py

import pandas as pd

# Load the synthetic genomic data
df = pd.read_csv('synthetic_genomic_data.csv')

# Data Preprocessing: Remove rows with missing values (if any)
df_clean = df.dropna()

# Alternatively, you can fill missing values if you expect any
# df_clean = df.fillna({'ExpressionLevel': 0})

# Ensure ExpressionLevel is a float
df_clean['ExpressionLevel'] = df_clean['ExpressionLevel'].astype(float)

# Save the cleaned data to a new CSV file
df_clean.to_csv('cleaned_genomic_data.csv', index=False)

# Optionally, show a preview of the cleaned data
print(df_clean.head())
