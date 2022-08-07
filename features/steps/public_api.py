import time

from behave import given, then
import logging

from exchange.pricing_api import get_server_time, get_pricing_pair


@given('I fetch the server time')
def step_impl(context):
    context.response = get_server_time()


@then('I get a response with 200 Status Code')
def step_impl(context):
    assert context.response.status_code == 200


@then('The response body is valid and contains both unix ts and rfc1123 time')
def step_impl(context):
    body = context.response.json()
    assert not body["error"]
    local_epoch = int(time.time())
    server_epoch = body["result"]["unixtime"]
    assert abs(local_epoch - server_epoch) < 5
    expected_time = time.strftime("%a, %d %b %y %H:%M:%S +0000", time.gmtime(server_epoch))
    assert expected_time == body["result"]["rfc1123"]


@given('I fetch "{crypto}" trading pair')
def step_impl(context, crypto):
    context.response = get_pricing_pair([crypto])


@then('The response body is valid')
def step_impl(context):
    body = context.response.json()
    logging.info(body)
    assert not body["error"]
