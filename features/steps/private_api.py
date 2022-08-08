import logging

from behave import given, then

from exchange.private_api import get_open_orders


@given('I fetch open orders')
def step_impl(context):
    context.response = get_open_orders()


@then('Response is valid, with zero open positions')
def step_impl(context):
    response = context.response.json()
    logging.info(context.response.json())
    assert not response["error"]
    assert response["result"]["open"] == {}
