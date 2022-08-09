Feature: Test the private API

Scenario: Fetch and validate open orders with OTP enabled
 When I fetch open orders
  Then I get a response with 200 Status Code
  And  Response is valid, with zero open positions
