Feature: validation of orange hrm module
  Scenario: login with valid creds
    Given open browser
    When enter username "Admin" password "admin123"
    Then click login button


  Scenario: search
    Given click search button
