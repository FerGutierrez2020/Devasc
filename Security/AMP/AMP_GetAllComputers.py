""" GET list of all computers via API """ 
import requests 

##Script Guia###
#url = "https://api.amp.cisco.com/v1/computers" 
#headers = { 'authorization': "Basic ZGVhZGJlZWYxMjM0NDhjY2MwMGQ6WFhYWFhYWFgtWVlZWS1aWlpaL TAwMDAtZTM4NGVmMmR4eHh4", 'cache-control': "no-cache", } 
#response = requests.request("GET", url, headers=headers)

amp_client_id = 'KEY'

amp_api_key = 'KEY'

url = 'https://api.amp.cisco.com/v1/computers'

request = requests.get(url, auth=(amp_client_id, amp_api_key))

print(request.json())