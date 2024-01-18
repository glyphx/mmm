import logging
from requests.exceptions import RequestException
from amazon_oauth_client import AmazonOAuthClient

class AmazonSPAPI:
    def __init__(self, client_id, client_secret, refresh_token):
        self.oauth_client = AmazonOAuthClient(
            client_id, client_secret, refresh_token,
            'https://api.amazon.com/auth/o2/token'
        )
        self.oauth_client.initialize_session()
        self.base_url = 'https://sellingpartnerapi-na.amazon.com'

    def create_listing(self, product_data):
        if not self.oauth_client.session:
            return {"success": False, "error": "OAuth session not established"}

        self.oauth_client.refresh_access_token()

        url = f'{self.base_url}/listings/2021-08-01/product'
        headers = {'Content-Type': 'application/json'}
        try:
            response = self.oauth_client.session.post(url, json=product_data, headers=headers)
            response.raise_for_status()
            return {"success": True, "data": response.json()}

        except RequestException as e:
            error_message = f"HTTP Status Code: {e.response.status_code}, Error: {e.response.text}" if e.response else str(e)
            return {"success": False, "error": error_message}

    def list_all_products(self):
        url = f'{self.base_url}/products/list'  # Update with the correct endpoint
        self.oauth_client.refresh_access_token()
        try:
            response = self.oauth_client.session.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            error_message = f"Error in listing products: {e.response.status_code} {e.response.text}" if e.response else str(e)
            logger.error(error_message)
            return {"success": False, "error": error_message}

    def get_product_by_gtin_or_sku(self, identifier):
        url = f'{self.base_url}/products/{identifier}'  # Update with the correct endpoint
        self.oauth_client.refresh_access_token()
        try:
            response = self.oauth_client.session.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            error_message = f"Error in fetching product data: {e.response.status_code} {e.response.text}" if e.response else str(e)
            logger.error(error_message)
            return {"success": False, "error": error_message}
