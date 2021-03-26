import requests
import json
import jsonpath

url="https://reqres.in/api/users"

#Read input json file

file = open("create_user.json")
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

response = requests.post(url,request_json)
print(response.status_code)

# Read response header information
print(response.headers.get("Date"))

# Read response body
response_json =  json.loads(response.text)
data = jsonpath.jsonpath(response_json,"createdAt")
print(data[0])