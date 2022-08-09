import requests
from requests.models import Response

from exchange.constants import API_URL


def get_server_time() -> Response:
    response = requests.get(f"{API_URL}/0/public/Time")
    return response


def get_pricing_pair(pair: list[str], info: str = None) -> Response:
    param = {"pair": ",".join(pair)}
    if info:
        param["info"] = info
    response = requests.get(f"{API_URL}/0/public/AssetPairs", params=param)
    return response
