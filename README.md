# customer-order-management


# Simple Python Service

This is a simple Python service with REST API endpoints for managing customers and orders.

## Setup Instructions

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up database by running: `python app.py` (this will create the SQLite database).
4. Set OAuth/OpenID Connect credentials in `config.py`.
5. Set Africa's Talking credentials in `config.py`.
6. Run the application: `python app.py`

## API Endpoints

- `POST /add_customer`: Add a new customer.
  Request Body: `{ "name": "John Doe", "code": "JD001" }`

- `POST /add_order`: Add a new order.
  Request Body: `{ "item": "Item 1", "amount": 100.0, "time": "2024-06-15T10:00:00", "customer_id": 1 }`

## Testing

Run unit tests: `pytest --cov=app tests/`

## CI/CD

The project includes a GitHub Actions workflow for continuous integration.

## Licence

MIT License