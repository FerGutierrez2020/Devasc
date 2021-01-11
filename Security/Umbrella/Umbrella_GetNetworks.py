import requests

url = "https://management.api.umbrella.com/v1/organizations/3465066/networks"

headers = {
    "accept": "application/json",
    "authorization": "Basic ODM4MGRjMzk3ZTllNDI0OTghNGIwM2I2Y2IzZWIxNjhkMTM5YmY="
}

response = requests.request("GET", url, headers=headers)

print(response.text)
