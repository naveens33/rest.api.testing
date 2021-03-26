import requests
import json
import jsonpath

endpoint = 'https://reqres.in/api/users?page=2'
response  = requests.get(endpoint)

print(response.status_code)

fname = jsonpath.jsonpath(response.json(),'data[*].first_name')
print(fname)
