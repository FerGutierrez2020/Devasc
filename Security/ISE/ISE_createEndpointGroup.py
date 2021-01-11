""" create a new endpointgroup on ISE """ 

import json 
import requests 

url = "https://10.10.20.70:9060/ers/config/endpointgroup" 
payload = { "EndPointGroup": { "name": "DevNet_Associate_Group", "description": "DevNet Associate Group" } } 
headers = { 'content-type': "application/json", 'accept': "application/json", 'authorization': "Basic dXNlcjE6Y2lzY28xMjM=", 'cache-control': "no-cache", } 
response = requests.request( "POST", url, data=json.dumps(payload), headers=headers, verify=False ) 
print(response.text)