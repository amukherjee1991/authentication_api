# Authentication API Project

This project is a Flask-based API that provides user authentication, request management, and payment handling for upgrading user packages. The API supports different user categories such as **Free**, **Prime**, and **Ultra**, each with different request limits.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [1. Login Endpoint](#1-login-endpoint)
  - [2. Check Requests Endpoint](#2-check-requests-endpoint)
  - [3. Payment Page Endpoint](#3-payment-page-endpoint)
  - [4. Upgrade Package Endpoint](#4-upgrade-package-endpoint)
- [Testing the API](#testing-the-api)
  - [Using Curl](#using-curl)
  - [Using Postman](#using-postman)
- [Additional Notes](#additional-notes)

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/authentication-api.git
   cd authentication-api
   ```
2. **Create virtual environment**
    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3. **Executing: First create a dummy database**
    ```
    python database_setup.py
    ```
4. **Running the application**
    ```
    python app.py
    ```
    The application will start on http://127.0.0.1:5000.

## API Endpoints

### 1. Login Endpoint

- **URL**: `/auth/login`
- **Method**: `POST`
- **Description**: Authenticates a user and returns a JWT token.
- **Request Body**:

  ```json
  {
    "username": "user1",
    "password": "password123"
  }
### Sample Response
```json
{
  "access_token": "your_generated_jwt_token"
}
```

## 2. Check Requests Endpoint
- **URL: /requests/check**
- **Method: GET**
- **Description: Checks the user's current request count and limits.**
- **Headers: Requires Authorization: Bearer <token> header with JWT token.**

Sample Response:

```json

{
  "msg": "Request successful",
  "requests_remaining": 2
}
```
## 3. Payment Page Endpoint
- **URL: /payment/payment_page**
- **Method: GET**
- **Description: Prompts users to upgrade their plan if they reach their request limit.**
- **Sample Response:**
```json
{
  "msg": "You've reached your request limit. Please upgrade your plan."
}
```
##4. Upgrade Package Endpoint
- **URL: /payment/upgrade**
- **Method: POST**
- **Description: Upgrades the user's package (e.g., from Free to Prime).**
- **Headers: Requires Authorization: Bearer <token> header with JWT token.**
- **Request Body:**
```json
{
  "new_package": "Prime"
}
```

### Testing the API
you can test the API using tools like curl or Postman.

## Using Curl
### Login to Get Token:

```bash
curl -X POST http://127.0.0.1:5000/auth/login -H "Content-Type: application/json" -d "{\"username\": \"user1\", \"password\": \"password123\"}"
```
### Check Requests:
```bash
curl -X GET http://127.0.0.1:5000/requests/check -H "Authorization: Bearer <your_token>"
```
### Access Payment Page:
```bash
curl -X GET http://127.0.0.1:5000/payment/payment_page
```
### Upgrade Package:
```bash
curl -X POST http://127.0.0.1:5000/payment/upgrade -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json" -d "{\"new_package\": \"Prime\"}"
```

### Using Postman
### Login to Get Token:
```
Method: POST
URL: http://127.0.0.1:5000/auth/login
Body: { "username": "user1", "password": "password123" }
Click Send to get the token.
```
### Check Requests:
```
Method: GET
URL: http://127.0.0.1:5000/requests/check
Go to the Authorization tab, select Bearer Token, and paste the token.
Click Send.
```

### Access Payment Page:

```
Method: GET
URL: http://127.0.0.1:5000/payment/payment_page
Click Send.
```
Upgrade Package:
```
Method: POST
URL: http://127.0.0.1:5000/payment/upgrade
Go to the Authorization tab, select Bearer Token, and paste the token.
Go to the Body tab, select raw and JSON, and enter { "new_package": "Prime" }.
Click Send.
```

### Additional Notes
- ** Check Logs: Monitor the terminal for any errors or log messages.
- ** Token Expiration: If a JWT token expires, log in again to obtain a new one.
- ** Database Reset: To reset the database, re-run the database_setup.py script.

### Dependencies
- **Flask
- **Flask-JWT-Extended
- **Flask-SQLAlchemy
- **APScheduler

### Install dependencies via 
```bash
pip install -r requirements.txt
```
### License
This project is licensed under the MIT License.

