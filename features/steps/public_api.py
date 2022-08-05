import time

from behave import given, then
import logging

from exchange.pricing_api import get_server_time


@given('I call the public time API')
def step_impl(context):
    context.server_time = get_server_time()


@then('I get a response with 200 Status Code')
def step_impl(context):
    assert context.server_time.status_code == 200


@then('The response body is valid')
def step_impl(context):
    body = context.server_time.json()
    assert not body["error"]
    local_epoch = int(time.time())
    server_epoch = body["result"]["unixtime"]
    assert abs(local_epoch - server_epoch) < 5
    expected_time = time.strftime("%a, %d %b %y %H:%M:%S +0000", time.gmtime(server_epoch))
    assert expected_time == body["result"]["rfc1123"]
