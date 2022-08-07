Feature: Test the public API

Scenario: Fetch and validate live server time
   Given I fetch the server time
    Then I get a response with 200 Status Code
    And  The response body is valid and contains both unix ts and rfc1123 time

Scenario: Fetch and validate trading pairs
   Given I fetch "XBTUSD" trading pair
    Then I get a response with 200 Status Code
    And  The response body is valid