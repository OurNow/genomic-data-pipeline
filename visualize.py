import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ensure the directory exists
os.makedirs('./visualizations', exist_ok=True)

# Load the cleaned genomic data
df = pd.read_csv('cleaned_real_time_genomic_data.csv')

# Check if the 'GeneID' and 'ExpressionLevel' columns exist
if 'GeneID' not in df.columns or 'ExpressionLevel' not in df.columns:
    print("Error: 'GeneID' or 'ExpressionLevel' column is missing.")
else:
    print("Both 'GeneID' and 'ExpressionLevel' columns found.")

# Visualization 1: Boxplot of Expression Level Across Genes
plt.figure(figsize=(12, 8))
sns.boxplot(x="GeneID", y="ExpressionLevel", data=df, palette="muted")
plt.title("Box Plot of Expression Level Across Genes")
plt.xlabel("Gene ID")
plt.ylabel("Expression Level")
plt.xticks(rotation=90)
plt.savefig('./visualizations/expression_boxplot.png')  # Save the plot as a PNG

# Visualization 2: Histogram of Expression Levels
plt.figure(figsize=(12, 8))
sns.histplot(df['ExpressionLevel'], kde=True, color='skyblue')
plt.title("Distribution of Expression Levels")
plt.xlabel("Expression Level")
plt.ylabel("Frequency")
plt.savefig('./visualizations/expression_histogram.png')  # Save as another PNG

# Visualization 3: Violin Plot of Expression Level Across Genes
plt.figure(figsize=(12, 8))
sns.violinplot(x="GeneID", y="ExpressionLevel", data=df, palette="muted")
plt.title("Violin Plot of Expression Level Across Genes")
plt.xlabel("Gene ID")
plt.ylabel("Expression Level")
plt.xticks(rotation=90)
plt.savefig('./visualizations/expression_violinplot.png')  # Save as PNG

# Visualization 4: Pairplot (ExpressionLevel vs GeneID)
# Since SNP_Index is not needed, let's pair 'ExpressionLevel' with 'GeneID'
# 'GeneID' is categorical, but we'll treat it as a factor for visualization purposes
plt.figure(figsize=(12, 8))
sns.pairplot(df, hue="GeneID", vars=["ExpressionLevel"])
plt.savefig('./visualizations/expression_pairplot.png')  # Save pairplot as PNG

# Additional visualizations can be added in a similar way
# Example: Countplot of SNP occurrences (optional if SNP column exists)
if 'SNP' in df.columns:
    plt.figure(figsize=(12, 8))
    sns.countplot(x="SNP", data=df, palette="viridis")
    plt.title("Countplot of SNP Occurrences")
    plt.xlabel("SNP")
    plt.ylabel("Count")
    plt.xticks(rotation=90)
    plt.savefig('./visualizations/snp_countplot.png')  # Save as PNG

# Ensure that all visualizations are saved in the 'visualizations' folder
print("Visualizations saved successfully.")
