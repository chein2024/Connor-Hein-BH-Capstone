
import requests
import pandas as pd

# Import your API key from config.py
from config import API_KEY

# Define the base URL for accessing the MER/F1 table in JSON format
base_url = "https://data.nasdaq.com/api/v3/datatables/MER/F1.json"

# Define optional query parameters
parameters = {
    "api_key": API_KEY,
    "qopts.per_page": 10,
    "ticker": "SPY",
    "qopts.columns": "ticker,date,shares_outstanding"
}

# Fetch data using requests.get, passing parameters, and convert the response to JSON
response = requests.get(base_url, params=parameters)
json_data = response.json()

# Convert JSON data to a pandas DataFrame for easier manipulation and analysis
df = pd.DataFrame(json_data['datatable']['data'], columns=json_data['datatable']['columns'])

# Print the DataFrame to check the output
print(df)
