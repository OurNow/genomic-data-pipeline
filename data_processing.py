from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder.appName("GenomicDataProcessing").getOrCreate()

# Load the dataset
df = spark.read.csv('synthetic_genomic_data.csv', header=True, inferSchema=True)

# Clean data (drop rows with missing values and ensure correct data types)
df_clean = df.dropna()
df_clean = df_clean.withColumn("ExpressionLevel", col("ExpressionLevel").cast("float"))

# Save the cleaned data for further analysis
df_clean.write.csv('cleaned_genomic_data.csv', header=True)
