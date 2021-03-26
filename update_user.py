import requests
import json
import jsonpath

url ="https://reqres.in/api/users/2"

file = open("create_user.json")
json_input = file.read()
request_json = json.loads(json_input)

response = requests.put(url,request_json)
print(response.status_code)

updatedAt = jsonpath.jsonpath(json.loads(response.content),"updatedAt")
print(updatedAt[0])




