Feature: Register and shop on Demo Webshop
  As a user,
  I want to register, log in, and purchase a product on Demo Webshop.

  Scenario: Register, login, and add a notebook to the shopping cart
    Given I navigate to the Demo Webshop registration page
    When I fill out the registration form and register
    Then I should be able to log in with my registered credentials
    When I add a notebook to the shopping cart
    Then I verify the shopping cart contains the item
