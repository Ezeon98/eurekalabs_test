# Stock Market API Service
This is a RESTful API service that allows users to sign up for an API key and use it to retrieve stock market information from Alpha Vantage web service.

### Installation
Clone this repository to your local machine:

`git clone https://github.com/Ezeon98/stock-market-api.git`

Navigate to the project directory:

`cd stock-market-api`

Build the Docker image:

`docker-compose build`

### Usage

Start the Docker containers:

`docker-compose up`

The API will be available at http://localhost:8080/. You can test it using a tool like cURL or Postman.

### Sign Up for an API Key
To sign up for an API key, make a POST request to /signup with a JSON payload containing your name, last name, and email:

```bash
curl -X POST \
http://localhost:8080/signup \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}'
```

The response will contain your API key:

```json
{
    "api_key": "57d5a5f5d48b1c09b2ab59d78c0c96d0c716f99d8e5d6527a96a19664c5b5bb8"
}
```

### Get Stock Market Information
To get stock market information, make a GET request to /stock/{symbol} with the X-API-Key header set to your API key:

```bash 
  curl -X GET \
  http://localhost:8000/stock/META \
  -H 'X-API-Key: 57d5a5f5d48b1c09b2ab59d78c0c96d0c716f99d8e5d6527a96a19664c5b5bb8'
  ```

The response will contain the open price, high price, low price, and variation between the last 2 closing price values for the specified stock symbol:

```json
{
    "symbol": "META",
    "open": "296.5100",
    "high": "296.8800",
    "low": "293.4400",
    "variation": "-1.1300"
}
```
### API Throttling
The API is throttled using the following rules:

**/signup**: 7 requests per minute.
**/stock**: 5 requests per minute.

### Logging
Every API call received is logged with the following format:

`INFO:     2023-05-02 08:30:00,000 - GET http://localhost:8080/stock/META (Status: 200)`

### Demo
https://eureka-test-1k2t.onrender.com/