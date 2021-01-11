""" generate a session token and create a new network object """ 

import json 
import requests 

## Globals used in this file 
url = "https://10.10.20.40/api/fmc_platform/v1/auth/generatetoken" 
server = "https://fmcrestapisandbox.cisco.com" 
username = "johnsmith" 
password = "pwgDvQt3" 
domain = "Global" 
token = "" 
headers = { 'Content-Type': "application/json", } 

## Definition of Lab Network (10.10.10.0)