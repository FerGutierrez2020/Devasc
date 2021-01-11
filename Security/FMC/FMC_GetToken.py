""" Generate the session token for FMC """ 
import requests 
import urllib3 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 
url = "https://10.10.20.40/api/fmc_platform/v1/auth/generatetoken" 
headers = { 'Content-Type': "application/xml", 'Authorization': "Basic YWRtaW46Q2lzY28xMjM0", } 
response = requests.request("POST", url, headers=headers, verify=False) 
print(response.headers)
print(response.status_code)