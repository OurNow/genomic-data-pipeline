import requests
import pandas as pd

def fetch_ensembl_data():
    url = "https://rest.ensembl.org/overlap/region/human/1:1-1000000?feature=gene;content-type=application/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)  # Converts API response directly to DataFrame
    else:
        raise Exception("Error fetching data from Ensembl API")

# Fetch the data and save it
df = fetch_ensembl_data()
df.to_csv('real_time_genomic_data.csv', index=False)
