import requests
import json

# TODO: should be secret env var
auth = {"X-CMC_PRO_API_KEY": "273104b2-dced-4bae-8c80-acb7c079f27b"}

url = "https://pro-api.coinmarketcap.com/v1/"


def ping():
    """Checks if API provider is online"""
    endpoint = "cryptocurrency/listings/latest"
    response = requests.get(url + endpoint, headers=auth)
    return response.status_code


def get_data(coin_ticker):
    """Returns current price of coin and other metadata"""
    endpoint = f"cryptocurrency/quotes/latest?slug={coin_ticker}&convert=EUR"
    response = requests.get(url + endpoint, headers=auth)
    return response.json()


def extract_price(json):
    """Given a JSON response, extracts the price field"""
    return int(json["data"]["1"]["quote"]["EUR"]["price"])
