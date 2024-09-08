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

## Check Requests Endpoint
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