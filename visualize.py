import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ensure the directory exists
os.makedirs('./visualizations', exist_ok=True)

# Load the cleaned genomic data
df = pd.read_csv('cleaned_genomic_data.csv')

# Visualization 1: Boxplot
plt.figure(figsize=(12, 8))
sns.boxplot(x="GeneID", y="ExpressionLevel", data=df, palette="muted")
plt.title("Box Plot of Expression Level Across Genes")
plt.xlabel("Gene ID")
plt.ylabel("Expression Level")
plt.xticks(rotation=90)
plt.savefig('./visualizations/expression_boxplot.png')  # Save the plot as a PNG

# Additional visualizations can be added in a similar way
# Example: Histogram of Expression Levels
plt.figure(figsize=(12, 8))
sns.histplot(df['ExpressionLevel'], kde=True, color='skyblue')
plt.title("Distribution of Expression Levels")
plt.xlabel("Expression Level")
plt.ylabel("Frequency")
plt.savefig('./visualizations/expression_histogram.png')  # Save as another PNG

# Add any other visualizations you'd like to save here
