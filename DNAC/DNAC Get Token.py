import requests

url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print(f"Response status code: {response.status_code}")