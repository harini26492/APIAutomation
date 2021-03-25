from behave import *
import requests
import json
import jsonpath

@given('i created a get req')
def get(context):

    url = "https://reqres.in/api/users?page=2"
    context.response = requests.get(url)

   #print(context.requests.content)
    # print(response.headers)

@when('i see response')
def abc(context):

    print(context.response.content)
    print(context.response.headers)
    #debug_write(context.response)

    #json_response = json.loads(response.text)
    # print(json_response)

   # pages = jsonpath.jsonpath(json_response, 'total_pages')
   # print(pages[0])

    #assert pages[0] == 2
