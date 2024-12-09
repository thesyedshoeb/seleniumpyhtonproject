Feature: Validation of Orange HRM module

  Scenario: login with valid credentials
    Given I open the browser
    When I enter username "Admin" and password "admin123"
    Then I click the login button

  Scenario: login with invalid credentials
    Given I open the browser
    When I enter username "InvalidUser" and password "wrongpassword"
    Then I click the login button
