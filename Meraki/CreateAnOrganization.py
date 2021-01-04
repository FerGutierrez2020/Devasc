import requests

url = "https://api.meraki.com/api/v0/organizations/549236/networks"

payload = '''{
    "name": "US 123 Office",
    "timeZone": "America/Seattle",
    "tags": " tag1 tag2 ",
    "disableMyMerakiCom": false,
    "type": "appliance switch camera"
}'''

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "15da0c6ffff295f16267f88f98694cf29a86ed87"
}

response = requests.request('POST', url, headers=headers, data = payload)

print(response.text.encode('utf8'))