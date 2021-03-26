import requests
import json
import jsonpath

url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)
# response status code
print(response.status_code)
# response content/body as byte
print(response.content)
# response content/body as text/string
print(response.text)
# response header
print(response.headers)
# response get specific header
print(response.headers.get('Date'))
# cookies
print(response.cookies)
# encoding
print(response.encoding)


json_response = json.loads(response.text)

pages = jsonpath.jsonpath(json_response,'total_pages')
print("pages:",pages[0])

email = jsonpath.jsonpath(json_response,'data[0].email')
print("email: ",email[0])
