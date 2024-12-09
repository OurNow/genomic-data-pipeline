import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import plotly.express as px

# Ensure the directory for saving visualizations exists
os.makedirs('./visualizations', exist_ok=True)

# Load the cleaned data (replace with correct path if needed)
df = pd.read_csv('cleaned_genomic_data.csv')

# 1. Histogram of Expression Levels by Gene
plt.figure(figsize=(12, 8))
sns.histplot(data=df, x="ExpressionLevel", hue="GeneID", multiple="stack", palette="Set1", kde=True)
plt.title("Histogram of Expression Levels by Gene")
plt.xlabel("Expression Level")
plt.ylabel("Frequency")
plt.legend(title="GeneID")
plt.savefig('./visualizations/histogram_by_gene.png')
plt.close()

# 2. Pairplot for SNP Index vs Expression Level
sns.pairplot(df, hue="SNP_Index", vars=["ExpressionLevel", "SNP_Index"])
plt.suptitle("Pairplot of SNP Index vs Expression Level", y=1.02)
plt.savefig('./visualizations/pairplot_snp_expression.png')
plt.close()

# 3. Violin Plot by SNP Index
plt.figure(figsize=(12, 8))
sns.violinplot(x="SNP_Index", y="ExpressionLevel", data=df, palette="muted")
plt.title("Violin Plot of Expression Level by SNP Index")
plt.xlabel("SNP Index")
plt.ylabel("Expression Level")
plt.savefig('./visualizations/violin_plot_snp_index.png')
plt.close()

# 4. Correlation Heatmap
corr_matrix = df[["ExpressionLevel", "SNP_Index"]].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.savefig('./visualizations/correlation_heatmap.png')
plt.close()

# 5. Bar Plot of SNP Count
snp_count = df["SNP"].value_counts().reset_index()
snp_count.columns = ["SNP", "count"]

plt.figure(figsize=(12, 6))
sns.barplot(x="SNP", y="count", data=snp_count, palette="viridis")
plt.title("SNP Count Across Dataset")
plt.xlabel("SNP")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('./visualizations/snp_count_barplot.png')
plt.close()

# 6. Boxplot of Expression Level by SNP Type
plt.figure(figsize=(12, 8))
sns.boxplot(x="SNP_Index", y="ExpressionLevel", data=df, palette="Set2")
plt.title("Boxplot of Expression Level by SNP Type")
plt.xlabel("SNP Type (Index)")
plt.ylabel("Expression Level")
plt.savefig('./visualizations/boxplot_expression_by_snp.png')
plt.close()

# 7. Heatmap for Gene-SNP Occurrences
snp_gene_count = df.groupby(["GeneID", "SNP"]).size().reset_index(name="count")
heatmap_data = snp_gene_count.pivot("GeneID", "SNP", "count").fillna(0)

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt="d", cbar_kws={'label': 'Count'})
plt.title("Gene-SNP Occurrences Heatmap")
plt.xlabel("SNP")
plt.ylabel("GeneID")
plt.savefig('./visualizations/gene_snp_heatmap.png')
plt.close()

# 8. Interactive Plot of Expression Level vs SNP Index (Plotly)
fig = px.scatter(df, x="SNP_Index", y="ExpressionLevel", color="GeneID", title="Interactive Scatter Plot of Expression Level vs SNP Index")
fig.write_html("./visualizations/interactive_snp_expression.html")

# Ensure the visualizations folder has the right files
print("Visualizations saved in './visualizations'.")
