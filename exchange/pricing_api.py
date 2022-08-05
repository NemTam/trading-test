import requests
import os

EXCHANGE_URL = os.environ["EXCHANGE_URL"]


def get_server_time():
    response = requests.get(f"{EXCHANGE_URL}/public/Time")
    return response


def get_pricing_pair(pair: str):
    param = {"pair": pair}
    resp = requests.get(f"{EXCHANGE_URL}/public/Trades", params=param)
    return resp
