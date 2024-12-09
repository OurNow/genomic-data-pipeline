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

# Process data and convert it into a DataFrame
df = pd.DataFrame(ensembl_data)

# Assuming 'GeneID' and 'ExpressionLevel' are keys in the data, adjust according to your API response
df_clean = df[['GeneID', 'SNP', 'ExpressionLevel']]  # Modify based on actual response keys

# Save the data
df_clean.to_csv('real_time_genomic_data.csv', index=False)
