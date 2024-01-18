# main.py
import os
import json
import argparse
from amazon_sp_api import AmazonSPAPI

def load_product_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        raise FileNotFoundError(f"Could not load or parse the JSON file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Amazon SP-API Product Listing Tool")
    parser.add_argument('json_file', help="Path to the JSON file with product data")
    args = parser.parse_args()

    # Load credentials from environment variables
    client_id = os.getenv("AMAZON_CLIENT_ID")
    client_secret = os.getenv("AMAZON_CLIENT_SECRET")
    refresh_token = os.getenv("AMAZON_REFRESH_TOKEN")

    # Load product data from JSON file
    product_data = load_product_data(args.json_file)

    # Instantiate the AmazonSPAPI class
    api = AmazonSPAPI(client_id, client_secret, refresh_token)

    # Make an API call to create a listing
    response = api.create_listing(product_data)
    print(response)

if __name__ == "__main__":
    main()

