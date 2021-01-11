import requests

ipaddress = input("What is the ip address to be analyzed? ")

url = "https://investigate.api.umbrella.com/ips/"+ ipaddress +"/latest_domains"

querystring = {"limit":"100"}

headers = {
    "accept": "application/json",
    "authorization": "Bearer 2d24b6b2e1eb520fc"
}

response = requests.request("GET", url, headers=headers,params=querystring)

print(response.text)
