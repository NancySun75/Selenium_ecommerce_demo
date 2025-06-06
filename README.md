# Ecommerce Automation Project

This project demonstrates end-to-end automated testing of an e-commerce platform using Selenium WebDriver.

## Features Tested:
- **User Login**: Verifies login functionality with valid and invalid credentials.
- **Product Browsing**: Ensures products are displayed correctly and available for browsing.
- **Shopping Cart**: Automates adding products to the cart and verifying item counts and prices.
- **Checkout Process**: Simulates the checkout flow, verifying product selection and order confirmation.

## Technologies Used:
- **Python**: Programming language used for test automation scripts.
- **Selenium WebDriver**: Automated browser interactions.
- **unittest**: Python unit testing framework for organizing tests and assertions.

## Getting Started:
1. Clone this repository.
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run tests:
    ```bash
    python -m unittest discover tests/
    ```

## Project Structure:
- `/tests`: Contains the test scripts for different functionalities.
- `/pages`: Implements Page Object Model to interact with web pages.
- `/utils`: Common utilities and helper functions.
- `/screenshots`: Stores screenshots for failed tests (optional).

## How to Contribute:
Feel free to fork this repository, create a new branch, and submit a pull request for any improvements.
