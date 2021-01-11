import requests

url = "https://management.api.umbrella.com/v1/organizations/3465066/roamingcomputers"

headers = {
    "Accept": "application/json",
    "Authorization": "Basic ODM4MGRjMzk3jNWE3OGZhNGIwM2I2Y2IzZWIxNjhkMTM5YmY="
}

response = requests.request("GET", url, headers=headers)

print(response.text)
