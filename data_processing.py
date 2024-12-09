import pandas as pd

# Load the real-time genomic data
df = pd.read_csv('real_time_genomic_data.csv')

# Clean the data (e.g., handle missing values, correct data types)
df_clean = df.dropna()  # Or apply other cleaning steps

# If you want to process data without 'ExpressionLevel', just remove this step:
# df_clean['ExpressionLevel'] = df_clean['ExpressionLevel'].astype(float)

# Save the cleaned data
df_clean.to_csv('cleaned_real_time_genomic_data.csv', index=False)

# Optionally, print the first few rows to verify
print(df_clean.head())
