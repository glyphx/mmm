# main.py
import argparse
import json
from amazon_sp_api import AmazonSPAPI

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    parser = argparse.ArgumentParser(description="Amazon SP-API Test Utility")
    parser.add_argument('--method', help="Method to test (create_listing, list_all_products, get_product_by_gtin_or_sku)", required=True)
    args = parser.parse_args()

    api = AmazonSPAPI(client_id='your_client_id', client_secret='your_client_secret', refresh_token='your_refresh_token')

    if args.method == 'create_listing':
        json_file = input("Enter the path to the JSON file with product data: ")
        product_data = load_json_data(json_file)
        response = api.create_listing(product_data)
        print(response)
    elif args.method == 'list_all_products':
        response = api.list_all_products()
        print(response)
    elif args.method == 'get_product_by_gtin_or_sku':
        identifier = input("Enter the product GTIN or SKU: ")
        response = api.get_product_by_gtin_or_sku(identifier)
        print(response)
    else:
        print("Invalid method specified.")

if __name__ == "__main__":
    main()
