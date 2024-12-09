import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ensure the directory exists to save visualizations
os.makedirs('./visualizations', exist_ok=True)

# Load the cleaned genomic data
df = pd.read_csv('cleaned_real_time_genomic_data.csv')

# Check if the necessary columns exist
if 'GeneID' not in df.columns:
    print("Error: 'GeneID' column is missing.")
else:
    print("'GeneID' column found.")

# Visualization 1: Countplot of Top 20 Genes
top_n_genes = 20  # Number of top genes to display based on occurrence frequency
top_genes = df['GeneID'].value_counts().head(top_n_genes).index

plt.figure(figsize=(14, 8))
sns.countplot(x="GeneID", data=df[df['GeneID'].isin(top_genes)], palette="muted", order=top_genes)
plt.title("Countplot of Top 20 Genes Based on Frequency")
plt.xlabel("Gene ID")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")

# Add explanation text on the plot
plt.text(0.95, 0.95, "This plot shows the top 20 genes based on their occurrence frequency.",
         transform=plt.gca().transAxes, fontsize=10, va='top', ha='right',
         bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))

# Save the plot as a PNG file in the 'visualizations' folder
plt.savefig('./visualizations/top_gene_countplot.png')  

# Visualization 2: Start vs. End Position of Genes (for strand orientation)
plt.figure(figsize=(12, 8))
sns.scatterplot(x="StartPosition", y="EndPosition", hue="Strand", data=df, palette="coolwarm")
plt.title("Start vs. End Position of Genes by Strand Orientation")
plt.xlabel("Start Position")
plt.ylabel("End Position")
plt.legend(title="Strand", loc="upper right")

# Add explanation text on the plot
plt.text(0.95, 0.95, "Each point represents a gene, with colors indicating strands (+/-).",
         transform=plt.gca().transAxes, fontsize=10, va='top', ha='right',
         bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))

# Save the plot as a PNG file
plt.savefig('./visualizations/start_vs_end_positions.png')

# Visualization 3: Distribution of Gene Biotypes (if available)
if 'GeneBiotype' in df.columns:
    plt.figure(figsize=(12, 8))
    sns.countplot(y="GeneBiotype", data=df, palette="viridis", order=df['GeneBiotype'].value_counts().index)
    plt.title("Distribution of Gene Biotypes in the Dataset")
    plt.xlabel("Count")
    plt.ylabel("Gene Biotype")

    # Add explanation text on the plot
    plt.text(0.95, 0.95, "This plot shows the distribution of different gene biotypes.",
             transform=plt.gca().transAxes, fontsize=10, va='top', ha='right',
             bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))

    # Save the plot as a PNG file
    plt.savefig('./visualizations/gene_biotype_distribution.png')

# Ensure that all visualizations are saved in the 'visualizations' folder
print("Visualizations saved successfully.")
