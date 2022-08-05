Feature: Test the public API

Scenario: Fetch the live server time
   Given I call the public time API
    Then I get a response with 200 Status Code
    And  The response body is valid