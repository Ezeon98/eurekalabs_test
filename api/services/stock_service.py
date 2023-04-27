import os
import requests
from datetime import datetime, timedelta
from pytz import timezone

now_utc = datetime.now(timezone("UTC"))
today = now_utc.astimezone(timezone("America/Argentina/Buenos_Aires"))
yesterday = today - timedelta(days=1)
API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

def stock_service(symbol: str):
    
    """
    This function takes a stock symbol and returns the opening price, highest price, lowest price and variation of the
    closing price of the stock for the current day compared to the previous day.

    Args:
    - symbol (str): The stock symbol to retrieve information for.

    Returns:
    - dict: A dictionary containing the following keys and their corresponding values:
        - "Open price": The opening price of the stock for the current day.
        - "Higher price": The highest price of the stock for the current day.
        - "Lower price": The lowest price of the stock for the current day.
        - "Variation Close price": The variation of the closing price of the stock for the current day compared to the previous day.
    """

    params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": symbol,
    "outputsize": "compact",
    "apikey": API_KEY
}
    
    response = requests.get(URL, params=params)
    if response.ok:
        json_response_today = response.json()["Time Series (Daily)"][today.strftime('%Y-%m-%d')]
        json_response_yesterday = response.json()["Time Series (Daily)"][yesterday.strftime('%Y-%m-%d')]
        
        close_diff = (float(json_response_today['4. close']) - float(json_response_yesterday['4. close']))

        return {
            "Open price": json_response_today["1. open"],
            "Higher price": json_response_today["2. high"], 
            "Lower price": json_response_today["3. low"],
            "Variation Close price": round(close_diff, 3)
            }
    else:
        return response.json()


