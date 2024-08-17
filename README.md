# MoneyGram Liberia Python Integration

![MoneyGram Logo](https://corporate.moneygram.com/images/MGI2_Corporate/MG_Logo_About_Page.png)

## Overview

**MoneyGram Liberia Python Integration** is a Python package designed to simplify the process of integrating the MoneyGram API into your Python project for seamless payment processing. Whether you're developing an e-commerce platform, a mobile app, or any system that requires payment services, this package provides an easy-to-use interface for working with MoneyGram's API.

## Features

- **Simple API Integration**: Streamline the integration process with easy-to-follow methods and examples.
- **Secure Transactions**: Ensure safe and secure money transfers and payment processing.
- **Extensive Documentation**: Comprehensive guides and documentation to help you get started quickly.
- **Error Handling**: Robust error handling mechanisms for dealing with API responses and exceptions.
- **Customizable**: Flexible design to adapt to various project requirements.

## Getting Started

### Prerequisites

- Python 3.6+
- An active MoneyGram account with API access
- `requests` library (for making API calls)

### Installation

To install the package, use `pip`:

```bash
pip install moneygram-liberia-python
```

### Configuration

Before making API calls, you need to configure your API credentials. You can do this by setting up environment variables or passing them directly in your code.

```python
# Example: Configuring API credentials
MONEYGRAM_API_KEY = "your_api_key"
MONEYGRAM_API_SECRET = "your_api_secret"
```

### Usage

Here's a simple example of how to use the package to initiate a payment:

```python
from moneygram_liberia import MoneyGramAPI

# Initialize the MoneyGram API client
mg_client = MoneyGramAPI(api_key=MONEYGRAM_API_KEY, api_secret=MONEYGRAM_API_SECRET)

# Example: Initiating a payment
response = mg_client.initiate_payment(
    sender_name="John Doe",
    sender_country="Liberia",
    receiver_name="Jane Smith",
    receiver_country="USA",
    amount=100.00,
    currency="USD"
)

# Check the response
if response['status'] == 'success':
    print("Payment initiated successfully!")
else:
    print(f"Error: {response['error_message']}")
```

### Available Methods

- `initiate_payment(sender_name, sender_country, receiver_name, receiver_country, amount, currency)`: Initiates a payment transaction.
- `check_transaction_status(transaction_id)`: Checks the status of a specific transaction.
- `cancel_transaction(transaction_id)`: Cancels a transaction if it hasn't been processed yet.

### Handling Errors

The package provides detailed error messages for failed API calls. Ensure you handle these errors properly in your application:

```python
try:
    response = mg_client.initiate_payment(...)
    if response['status'] != 'success':
        raise Exception(response['error_message'])
except Exception as e:
    print(f"Payment failed: {e}")
```

## Documentation

For detailed documentation and advanced usage, please refer to the [MoneyGram API Documentation](https://developer.moneygram.com/).

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact [support@yourcompany.com](mailto:support@yourcompany.com).

---

This README provides an overview and instructions on how to use the MoneyGram Liberia Python Integration package. It simplifies the integration process, enabling developers to quickly implement payment processing with MoneyGram in their Python projects.
