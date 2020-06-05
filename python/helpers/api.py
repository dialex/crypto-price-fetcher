import requests
import json
import helpers.log as log
import helpers.env as env
from jsonpath_ng import jsonpath, parse

auth = {"X-CMC_PRO_API_KEY": env.get_var("API_KEY")}
url = "https://pro-api.coinmarketcap.com/v1/"


def ping():
    """Checks if API provider is online"""
    endpoint = "cryptocurrency/listings/latest"
    response = requests.get(url + endpoint, headers=auth)
    return response.status_code


def get_data(coin_ticker):
    """Returns metadata of a given coin"""
    endpoint = f"cryptocurrency/quotes/latest?slug={coin_ticker}&convert=EUR"
    response = requests.get(url + endpoint, headers=auth)
    response_json = response.json()

    if(response.status_code != 200):
        log.err("Unknown coin")
        error_msg = f'API returned {response.status_code}, {response_json["status"]["error_message"]}'
        raise Exception(error_msg)
    else:
        return response_json


def get_price(coin_ticker):
    """Returns the current price of a given coin"""
    return extract_price(get_data(coin_ticker))


def extract_price(json):
    """Given a JSON response, extracts the price field"""
    jsonpath = parse("$..EUR.price")
    match = jsonpath.find(json)
    return float(match[0].value)
