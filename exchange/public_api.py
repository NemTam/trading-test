import requests

from exchange.constants import API_URL


def get_server_time():
    response = requests.get(f"{API_URL}/0/public/Time")
    return response


def get_pricing_pair(pair: list[str], info: str = None):
    param = {"pair": ",".join(pair)}
    if info:
        param["info"] = info
    resp = requests.get(f"{API_URL}/0/public/AssetPairs", params=param)
    return resp


