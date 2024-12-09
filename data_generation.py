import requests
import pandas as pd

# Function to fetch data from Ensembl API
def fetch_ensembl_data():
    url = "https://rest.ensembl.org/overlap/region/human/1:1-1000000?feature=gene;content-type=application/json"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching data from Ensembl API")

# Fetch data from Ensembl
ensembl_data = fetch_ensembl_data()

# Inspect the structure of the response (for debugging)
print(ensembl_data)

# Convert the response into a DataFrame
df = pd.DataFrame(ensembl_data)

# Check the column names in the response
print(df.columns)

# Select relevant columns (e.g., gene_id, seq_region_name, description)
# Adjust based on the actual data you're interested in
df_clean = df[['gene_id', 'seq_region_name', 'description', 'start', 'end', 'strand', 'biotype']]

# Optionally, you can rename columns if needed (for clarity)
df_clean.rename(columns={
    'gene_id': 'GeneID',
    'seq_region_name': 'SNP',
    'description': 'GeneDescription',
    'start': 'StartPosition',
    'end': 'EndPosition',
    'strand': 'Strand',
    'biotype': 'GeneBiotype'
}, inplace=True)

# Save the cleaned data to a CSV file
df_clean.to_csv('real_time_genomic_data.csv', index=False)

# Optionally, print the cleaned DataFrame for verification
print(df_clean.head())
