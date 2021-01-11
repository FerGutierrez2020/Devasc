import requests

url = "https://10.10.20.70:9060/ers/config/endpointgroup"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Basic dXNlcjE6Y2lzY28xMjM=',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
