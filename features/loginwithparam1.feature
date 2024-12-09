Feature: Validation of Orange HRM module
  Scenario Outline: login with valid credentials
    Given I open the chrome browser
    When I enter username <username> and password <password>
    Then I click the login buttons
    Examples:
    | username | password |
    | Admin | admin123 |
    | Admi | admin12 |