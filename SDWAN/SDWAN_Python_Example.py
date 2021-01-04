import requests

url = "https://sandboxsdwan.cisco.com:8443/dataservice/device"

payload={}
headers = {
  'Cookie': 'JSESSIONID=dDUF79PsFpAjuBnESg1E43hzrp0_iyEJS-KDTO-j.4854266f-a8ad-4068-9651-d4e834384f51'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)
