from pyspark.sql import SparkSession
from pyspark.sql.functions import count

# Initialize Spark session
spark = SparkSession.builder.appName("GenomicDataAnalysis").getOrCreate()

# Load cleaned data
df = spark.read.csv('./cleaned_real_time_genomic_data.csv', header=True, inferSchema=True)

# Group by SNP and count occurrences
snp_count = df.groupBy("SNP").agg(count("*").alias("Occurrences")).orderBy("Occurrences", ascending=False)
snp_count.show()

# Group by GeneID and count occurrences
gene_count = df.groupBy("GeneID").agg(count("*").alias("Occurrences")).orderBy("Occurrences", ascending=False)
gene_count.show()

# Save results to CSV (optional)
snp_count.write.csv('./snp_analysis_results.csv', header=True, mode='overwrite')
gene_count.write.csv('./gene_analysis_results.csv', header=True, mode='overwrite')
