Feature: Amazon Purchase Process
  As a user, I want to search for a product, add it to the cart, and complete the purchase.

  Scenario: Search and add a product to the cart
    Given I open the Amazon homepage
    When I search for "S24 ultra"
    When I click on the product
    Then I add the product to the cart
    When I click on proceed to checkout
    When I add the card information
    Then I confirm the card details
    Then the payment should be processed successfully


