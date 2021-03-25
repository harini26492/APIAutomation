Feature: Create a user in go rest database
  Scenario: Create a User using valid data
    Given A user with valid access token
      And the user wants to create a record with first name as "John X"
      And the user record has a last name of "Rocket"
      When user submits the user data in "https://gorest.co.in/public-api/users"
      Then you should receive a "200" status code


