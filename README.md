# customer-order-management

## Overview
This project is a Flask-based web application for managing customer orders. It includes features for user authentication, customer management, and order processing.


## Setup Instructions

1. Clone the repository
2. Install dependencies
3. Run the application


## Features
User authentication (login and account creation)
CRUD operations for customers and orders
Integration with Africa's Talking API for SMS notifications

## Creating the Database
1. Initialize the Database- run (flask db init)
2. Generate Migration Scripts (if using SQLAlchemy Migrate)- run 'flask db migrate -m "Initial migration'
3. Apply Migrations to the Database - run 'flask db upgrade'
4. Seed Initial Data- run 'python3 seed.py'


## Technologies Used

Flask
SQLAlchemy
Flask OIDC for OpenID Connect integration
Flask CORS for Cross-Origin Resource Sharing
Africa's Talking API for SMS notifications


## CI/CD

The project includes a GitHub Actions workflow for continuous integration.

## Licence

MIT License