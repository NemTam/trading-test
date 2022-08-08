import logging
import time

from behave import given, then
from jsonschema import validate

from exchange.public_api import get_server_time, get_pricing_pair
from features.steps.schemas.public_api_schemas import TRADING_PAIRS, SERVER_TIME_SCHEMA


@given('I fetch the server time')
def step_impl(context):
    context.response = get_server_time()


@then('I get a response with 200 Status Code')
def step_impl(context):
    assert context.response.status_code == 200


@then('Response is valid and contains both unix ts and rfc1123 time')
def step_impl(context):
    body = context.response.json()
    assert not body["error"]
    validate(body["result"], schema=SERVER_TIME_SCHEMA)
    server_epoch = body["result"]["unixtime"]
    expected_time = time.strftime("%a, %d %b %y %H:%M:%S +0000", time.gmtime(server_epoch))
    assert expected_time == body["result"]["rfc1123"]


@given('I fetch "{crypto}" trading pair with "{param}" query param')
def step_impl(context, crypto, param):
    context.crypto = crypto
    context.param = param
    if param != "None":
        context.response = get_pricing_pair([crypto], info=param)
    else:
        context.response = get_pricing_pair([crypto])


@then('The response body is valid')
def step_impl(context):
    body = context.response.json()
    logging.info(body)
    assert not body["error"]
    # Leverage schema was the most compact, this is just an example schema validation for XXBTZUSD
    # For production code I would use a more generic approach
    if getattr(context, "param", None) == "leverage" and context.crypto == "XBTUSD":
        validate(body["result"], schema=TRADING_PAIRS[context.param])
