Feature: Test the public API

Scenario: Fetch and validate live server time
    When I fetch the server time
    Then I get a response with 200 Status Code
    And  Response is valid and contains both unix ts and rfc1123 time

Scenario Outline: Fetch and validate trading pairs
    When I fetch "XBTUSD" trading pair with "<param>" query parameter
    Then I get a response with 200 Status Code
    And  The response body is valid
   Examples: Query params
    | param    |
    | None     |
    | info     |
    | leverage |
    | fees     |
    | margin   |
