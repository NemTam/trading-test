import logging

import requests
import os

EXCHANGE_URL = os.environ["EXCHANGE_URL"]


def get_server_time():
    response = requests.get(f"{EXCHANGE_URL}/public/Time")
    return response


def get_pricing_pair(pair: list[str], info: str = None):
    param = {"pair": ",".join(pair)}
    logging.error(param)
    if info:
        param["info"] = info
    resp = requests.get(f"{EXCHANGE_URL}/public/AssetPairs", params=param)
    return resp


