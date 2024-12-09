import boto3
import pandas as pd
import os

# Load the cleaned genomic data
df = pd.read_csv('cleaned_real_time_genomic_data.csv')

# Define your AWS S3 bucket and file path
bucket_name = 'your-bucket-name'  # Replace with your S3 bucket name
file_name = 'cleaned_real_time_genomic_data.csv'  # Name of the file in the S3 bucket
local_file_path = './cleaned_real_time_genomic_data.csv'  # Local path to the file

# Ensure the file exists locally before uploading
if not os.path.exists(local_file_path):
    df.to_csv(local_file_path, index=False)
    print(f"File {local_file_path} created locally.")

# Set up AWS S3 client
s3_client = boto3.client('s3')

# Upload the file to S3
try:
    s3_client.upload_file(local_file_path, bucket_name, file_name)
    print(f"File successfully uploaded to s3://{bucket_name}/{file_name}")
except Exception as e:
    print(f"Error uploading file to S3: {e}")
