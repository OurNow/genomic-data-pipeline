import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ensure the directory exists
os.makedirs('./visualizations', exist_ok=True)

# Load the cleaned genomic data
df = pd.read_csv('cleaned_real_time_genomic_data.csv')

# Check if the necessary columns exist
required_columns = ['GeneID', 'SNP', 'GeneDescription', 'StartPosition', 'EndPosition', 'Strand', 'GeneBiotype']
for col in required_columns:
    if col not in df.columns:
        print(f"Error: '{col}' column is missing.")
    else:
        print(f"'{col}' column found.")

# 1. SNP Frequency by Gene
plt.figure(figsize=(14, 8))
sns.countplot(x="GeneID", data=df[df['SNP'] == 1], palette="coolwarm", order=df['GeneID'].value_counts().head(20).index)
plt.title("SNP Frequency by Gene")
plt.xlabel("Gene ID")
plt.ylabel("SNP Count")
plt.xticks(rotation=45)
plt.text(0.95, 0.95, "This plot shows the frequency of SNPs across genes.",
         transform=plt.gca().transAxes, fontsize=10, va='top', ha='right',
         bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))
plt.savefig('./visualizations/snp_frequency_by_gene.png')

# 2. Start vs. End Position of Genes
plt.figure(figsize=(12, 8))
sns.scatterplot(x="StartPosition", y="EndPosition", hue="Strand", data=df, palette="coolwarm")
plt.title("Start vs. End Position of Genes")
plt.xlabel("Start Position")
plt.ylabel("End Position")
plt.legend(title="Strand")

# Add explanation
plt.text(0.95, 0.95, "Each point represents a gene, with colors indicating strands (+/-).",
         transform=plt.gca().transAxes, fontsize=10, va='top', ha='right',
         bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))
plt.savefig('./visualizations/start_vs_end_positions.png')  # Save as another PNG

# 3. Distribution of Gene Biotypes
plt.figure(figsize=(12, 8))
sns.countplot(y="GeneBiotype", data=df, palette="viridis", order=df['GeneBiotype'].value_counts().index)
plt.title("Distribution of Gene Biotypes")
plt.xlabel("Count")
plt.ylabel("Gene Biotype")

# Add explanation
plt.text(0.95, 0.95, "This plot shows the distribution of gene biotypes in the dataset.",
         transform=plt.gca().transAxes, fontsize=10, va='top', ha='right',
         bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))
plt.savefig('./visualizations/gene_biotype_distribution.png')  # Save as PNG

# 4. SNP Distribution Across Gene Biotypes
plt.figure(figsize=(14, 8))
sns.countplot(x="GeneBiotype", hue="SNP", data=df, palette="muted")
plt.title("SNP Distribution Across Gene Biotypes")
plt.xlabel("Gene Biotype")
plt.ylabel("SNP Count")
plt.xticks(rotation=45)
plt.text(0.95, 0.95, "This plot shows the distribution of SNPs across different gene biotypes.",
         transform=plt.gca().transAxes, fontsize=10, va='top', ha='right',
         bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))
plt.savefig('./visualizations/snp_by_gene_biotype.png')

# 5. Distribution of Gene Biotypes with SNPs
plt.figure(figsize=(12, 8))
sns.countplot(x="GeneBiotype", data=df[df['SNP'] == 1], palette="Set2")
plt.title("SNPs in Different Gene Biotypes")
plt.xlabel("Gene Biotype")
plt.ylabel("Count of SNPs")
plt.xticks(rotation=45)
plt.text(0.95, 0.95, "This plot shows the number of SNPs across different gene biotypes.",
         transform=plt.gca().transAxes, fontsize=10, va='top', ha='right',
         bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))
plt.savefig('./visualizations/snp_in_gene_biotypes.png')

# 6. GeneID vs. Strand - Distribution of Genes Across Strands
plt.figure(figsize=(14, 8))
sns.countplot(x="GeneID", hue="Strand", data=df, palette="coolwarm", order=df['GeneID'].value_counts().head(20).index)
plt.title("GeneID vs Strand Distribution")
plt.xlabel("Gene ID")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.text(0.95, 0.95, "This plot shows the distribution of genes across strands (+/-).",
         transform=plt.gca().transAxes, fontsize=10, va='top', ha='right',
         bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))
plt.savefig('./visualizations/geneid_vs_strand.png')

# Ensure that all visualizations are saved in the 'visualizations' folder
print("Visualizations saved successfully.")
