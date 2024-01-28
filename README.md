# Delivery fee app backend for Wolt Internships 2024

### Installation

1. Have **Python 3.10** or newer installed
2. Install required dependencies with `pip install -r requirements.txt`

### Usage

- Unit tests can be run with `pytest`
- Main server can be started with `uvicorn main:app`

### Design Choices

I chose to use FastAPI library as it provides good performance and a streamlined development process.

The route `/api/calculate_fee` accepts POST request with the correct payload and returns a JSON with the calculated delivery fee.
With incorrect payload an error will be raised.

The route has been tested both manually and automatically with pytest, to account for:

- Invalid request payload
- Very low order price
- Rush hour multiplier
- Varying distances
- Bulk orders
- Max fee of 15€
- Free delivery on orders above 200€
