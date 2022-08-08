import base64
import hashlib
import hmac
import time
import urllib.parse

import pyotp
import requests
from requests.models import Response

from exchange.constants import API_URL, API_KEY, PRIVATE_KEY, OTP_SEED


def get_api_signature(urlpath: str, data: dict, secret: str) -> str:
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()
    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()


def send_post_request(uri_path: str, data: dict) -> Response:
    headers = {'API-Key': API_KEY, 'API-Sign': get_api_signature(uri_path, data, PRIVATE_KEY)}
    req = requests.post((API_URL + uri_path), headers=headers, data=data)
    return req


def generate_otp() -> str:
    totp = pyotp.TOTP(OTP_SEED)
    return totp.now()


def get_open_orders() -> Response:
    resp = send_post_request('/0/private/OpenOrders', {
        "nonce": str(int(1000 * time.time())),
        "otp": generate_otp(),
        "trades": True
    })
    return resp
