# Amazon Selling Partner API Integration

This project provides a Python interface for interacting with the Amazon Selling Partner API (SP-API). It includes functionality for OAuth authentication and creating product listings on Amazon.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

Set the following environment variables with your Amazon SP-API credentials:

- `AMAZON_CLIENT_ID`: Your Amazon SP-API client ID.
- `AMAZON_CLIENT_SECRET`: Your Amazon SP-API client secret.
- `AMAZON_REFRESH_TOKEN`: Your Amazon SP-API refresh token.

These can be set in your environment or through a `.env` file.

### Usage

To use the script to create a product listing, run `main.py` with the path to a JSON file containing the product data:

```bash
python main.py /path/to/product_data.json

```

###Example JSON
```json
{
    "sku": "YOUR_SKU",
    "productTitle": "YOUR_PRODUCT_TITLE",
    "description": "YOUR_DESCRIPTION",
    "standardPrice": YOUR_PRICE,
    "quantity": YOUR_QUANTITY,
    "productCategory": "YOUR_PRODUCT_CATEGORY",
    "GTIN": "YOUR_GTIN"
}
{
    "sku": "FRENCHVAN-SQUEEZE-001",
    "productTitle": "French Vanilla Squeeze Soy Wax Melt",
    "description": "Experience the soothing and luxurious aroma of French Vanilla with our premium soy wax melts. Perfect for creating a warm and inviting atmosphere in your home.",
    "bulletPoints": [
        "Made with 100% natural soy wax for a cleaner, longer-lasting burn.",
        "Infused with the rich and comforting scent of French Vanilla.",
        "Ideal for use in any standard wax warmer, spreading a delightful fragrance without smoke or soot.",
        "Eco-friendly and sustainable product, perfect for creating a cozy and inviting home environment.",
        "Each pack contains a generous amount of wax melts, offering hours of aromatic pleasure."
    ],
    "standardPrice": 19.99,
    "quantity": 100,
    "productCategory": "Home & Kitchen > Home Décor > Candles & Holders > Wax Melts",
    "GTIN": "1234567890123"
}

```

