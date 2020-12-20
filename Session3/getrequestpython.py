import requests 
url = "https://postman-echo.com/get" 
querystring = {"test":"123"} 
headers = {} 
response = requests.request("GET", url, headers=headers, params=querystring) 
print(response.text)