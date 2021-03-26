import requests

url = "https://login.microsoftonline.com/e22f3d72-e156-44d8-a8b9-07c4cc0b3d87/oauth2/Token"

data = {
    'grant_type':'client_credentials',
    'client_id':'0bcdbb93-510c-47a8-841c-33a4f559bf4e',
    'client_secret':'nTKUjoqzU1pfhp4mO3zF4Q8eOpsZySWVF8KoF97/WBo=',
    'resouce':'https://productvaultservice.azurewebsites.net'
}
response = requests.post(url=url,data=data)

token= response.json()["access_token"]
#print(token)

url = "https://productvaultservice-pvstaging.azurewebsites.net/api/ProductType"
headers = {
    'Authorization' : 'Bearer ' + token,

}

response = requests.get(url=url,headers=headers)
print(type(response.status_code))
import json
import jsonpath
json_data = json.loads(response.text)
print(json_data)