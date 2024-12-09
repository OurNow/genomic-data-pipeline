import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ensure the directory exists
os.makedirs('./visualizations', exist_ok=True)

# Load the cleaned genomic data
df = pd.read_csv('cleaned_real_time_genomic_data.csv')

# Check if the necessary columns exist
if 'GeneID' not in df.columns:
    print("Error: 'GeneID' column is missing.")
else:
    print("'GeneID' column found.")

# Visualization 1: Countplot of Genes
plt.figure(figsize=(12, 8))
sns.countplot(x="GeneID", data=df, palette="muted", order=df['GeneID'].value_counts().index)
plt.title("Countplot of Genes")
plt.xlabel("Gene ID")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('./visualizations/gene_countplot.png')  # Save the plot as a PNG

# Visualization 2: Start vs. End Position of Genes
plt.figure(figsize=(12, 8))
sns.scatterplot(x="StartPosition", y="EndPosition", hue="Strand", data=df, palette="coolwarm")
plt.title("Start vs. End Position of Genes")
plt.xlabel("Start Position")
plt.ylabel("End Position")
plt.legend(title="Strand")
plt.savefig('./visualizations/start_vs_end_positions.png')  # Save as another PNG

# Visualization 3: Distribution of Gene Biotypes
if 'GeneBiotype' in df.columns:
    plt.figure(figsize=(12, 8))
    sns.countplot(y="GeneBiotype", data=df, palette="viridis", order=df['GeneBiotype'].value_counts().index)
    plt.title("Distribution of Gene Biotypes")
    plt.xlabel("Count")
    plt.ylabel("Gene Biotype")
    plt.savefig('./visualizations/gene_biotype_distribution.png')  # Save as PNG

# Ensure that all visualizations are saved in the 'visualizations' folder
print("Visualizations saved successfully.")
