import random
import pandas as pd
import numpy as np

# Define parameters
num_rows = 1000000  # Number of rows (1 million)
genes = ['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7', 'gene8', 'gene9', 'gene10']
snps = ['SNP1', 'SNP2', 'SNP3', 'SNP4', 'SNP5', 'SNP6', 'SNP7', 'SNP8', 'SNP9', 'SNP10']

# Create skewed data for ExpressionLevel
def generate_expression(gene):
    # Skewed distribution for gene1 and gene2
    if gene == "gene1":
        return np.random.exponential(scale=20)  # Exponentially distributed data
    elif gene == "gene2":
        return np.random.normal(loc=40, scale=15)  # Normal distribution, with some variation
    elif gene == "gene3":
        return np.random.lognormal(mean=1, sigma=0.5)  # Log-normal distribution
    elif gene == "gene4":
        return np.random.normal(loc=70, scale=5)  # A very narrow normal distribution
    elif gene == "gene5":
        return np.random.uniform(20, 80)  # Uniform distribution, random
    elif gene == "gene6":
        return np.random.beta(a=2, b=5) * 100  # Beta distribution scaled to 0-100
    else:
        return np.random.uniform(0, 100)  # For other genes, just uniform random data

# Generate synthetic data with skewed and varied distributions
data = []
for _ in range(num_rows):
    gene_id = random.choice(genes)
    snp = random.choice(snps)
    expression_level = generate_expression(gene_id)  # Use the function to generate varying expression levels
    data.append([gene_id, snp, expression_level])

# Create DataFrame
df = pd.DataFrame(data, columns=['GeneID', 'SNP', 'ExpressionLevel'])

# Introduce some outliers by adding extreme values to the ExpressionLevel of random samples
outlier_indices = np.random.choice(df.index, size=50, replace=False)
df.loc[outlier_indices, 'ExpressionLevel'] = np.random.uniform(150, 500, size=50)  # Add extreme outliers

# Save the DataFrame as a CSV file
df.to_csv('synthetic_genomic_data.csv', index=False)

# Display the first few rows to verify the data
print(df.head())
