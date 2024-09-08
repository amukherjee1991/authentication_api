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
