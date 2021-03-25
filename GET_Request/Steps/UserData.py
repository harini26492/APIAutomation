from behave import *
import requests

@given('A user with valid access token')
def set_access_token_in_header(context):
    context.header = {"Authorization": "Bearer" + "<YOUR_ACCESS_TOKEN>"}


@given('the user wants to create a record with first name as "John X"')
def set_first_name(context):
    context.request_body = {"first_name": "John X"}


@given('the user record has a last name of "Rocket"')
def set_last_name(context):
    context.request_body['last_name'] = "Rocket"


@when('user submits the user data in "https://gorest.co.in/public-api/users"')
def execute_post_request_for_user_creation(context):
    response = requests.post('https://gorest.co.in/public-api/users', headers=context.header, json=context.request_body)
    context.response_body = response.json()
    context.status_code = response.status_code


@then('you should receive a "200" status code')
def check_status_code(context):
    assert context.status_code == 200

