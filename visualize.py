import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load cleaned data into Pandas for visualization
df = pd.read_csv('cleaned_genomic_data.csv')

# Histogram of Expression Levels
plt.hist(df['ExpressionLevel'], bins=30, color='skyblue', edgecolor='black')
plt.title("Distribution of Expression Levels")
plt.xlabel("Expression Level")
plt.ylabel("Frequency")
plt.savefig('histogram.png')

# Boxplot of Expression Level by SNP
sns.boxplot(x="SNP", y="ExpressionLevel", data=df, palette="Set2")
plt.title("Box Plot of Expression Level by SNP")
plt.xlabel("SNP")
plt.ylabel("Expression Level")
plt.savefig('boxplot.png')
