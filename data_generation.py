import random
import pandas as pd

# Parameters for data generation
num_rows = 1000000  # Number of rows
genes = ['gene1', 'gene2', 'gene3', 'gene4', 'gene5']
snps = ['SNP1', 'SNP2', 'SNP3', 'SNP4', 'SNP5']

# Generate synthetic data
data = []
for _ in range(num_rows):
    gene_id = random.choice(genes)
    snp = random.choice(snps)
    expression_level = round(random.uniform(0, 100), 2)  # Random float between 0 and 100
    data.append([gene_id, snp, expression_level])

# Create DataFrame and save as CSV
df = pd.DataFrame(data, columns=['GeneID', 'SNP', 'ExpressionLevel'])
df.to_csv('synthetic_genomic_data.csv', index=False)
