""" GET list of all vulnerabilities via API """ 
import requests 
url = "https://api.amp.cisco.com/v1/policies" 
querystring = {"offset":"0","limit":"1"} 
headers = { 'authorization': "Basic OWJhZGEyYmZlZc3NTYtNDljMi00OllYTgtMzFhZDY4OTVmMjAz", 'cache-control': "no-cache", } 
response = requests.request("GET", url, headers=headers, params=querystring) 
print(response.text)
