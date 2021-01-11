""" Get Server Version """ 
import requests 
url = "https://10.10.20.40/api/fmc_platform/v1/info/serverversion" 
headers = { 'X-auth-access-token': "9866f5dd-8791-4839-990f-f6de037478fa", } 
response = requests.request("GET", url, headers=headers, verify=False) 
print(response.text)

