# data_generation.py

import random
import pandas as pd

# Define parameters
num_rows = 1000000  # Number of rows (1 million)
genes = ['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7', 'gene8', 'gene9', 'gene10']
snps = ['SNP1', 'SNP2', 'SNP3', 'SNP4', 'SNP5', 'SNP6', 'SNP7', 'SNP8', 'SNP9', 'SNP10']

# Generate synthetic data
data = []
for _ in range(num_rows):
    gene_id = random.choice(genes)
    snp = random.choice(snps)
    expression_level = round(random.uniform(0, 100), 2)  # Random float between 0 and 100
    data.append([gene_id, snp, expression_level])

# Create a DataFrame
df = pd.DataFrame(data, columns=['GeneID', 'SNP', 'ExpressionLevel'])

# Save the DataFrame as a CSV file
df.to_csv('synthetic_genomic_data.csv', index=False)

# Optionally, show a preview of the generated data
print(df.head())
