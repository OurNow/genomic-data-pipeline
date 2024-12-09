from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

# Initialize Spark session
spark = SparkSession.builder.appName("GenomicDataAnalysis").getOrCreate()

# Load cleaned data
df = spark.read.csv('cleaned_genomic_data.csv', header=True, inferSchema=True)

# Group by SNP and calculate average ExpressionLevel
snp_avg = df.groupBy("SNP").agg(avg("ExpressionLevel").alias("AvgExpression"))
snp_avg.show()

# Count occurrences of each SNP
snp_count = df.groupBy("SNP").count().orderBy("count", ascending=False)
snp_count.show()
