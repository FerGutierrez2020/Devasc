import requests
import json

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'X-Auth-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZjhlYjhhZDc1MTYxMjRlODczYTg0YmYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTYwOTM5MzM2NywiaWF0IjoxNjA5Mzg5NzY3LCJqdGkiOiI5MmEyMjJiYi00NTQ2LTRhNTMtYWY4ZC0wZTA3MjUxMDgzYzkiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.Kf_Lxuk3ucTiny9kr0KE8KH_sA5T1YkNHs4_r8XG0n4Vthu6fD6IwZyRqoVaSdxsK9F-wbDL_0ylATpkqRZWdwy-nkZjftI_h5CrOmz89VkAaHN_voQNbHwrpcxI_jf6R7k4g5x0X5p9ANzz2I06KyZ5tzy6r32yenLd-VOAU706S7V7uAVqMnOjyu_qZlmAiQa04qpL6DhLiiInA6dJMwY7veeKFLcQQuceD_pLDckiiBkWgKx9akp7ljGCDMyUxj_my0xdI61GMQ3DOBrxCtfdXnM92OPNXWbZMdCI0nV826Yh8lSbqEYT33WPBQ7ARglPklRDq72jBULCJgfq5w'
}

##ENVIAR LAS VARIABLES EN UN REQUEST Y GUARDAR EL RESULTADO EN RESPONSE
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)

"""raw_output = json.loads(response.text)

devices = raw_output["response"]

 
# ITERAR POR LA LISTA E IMPRIMIR LOS HOSTNAMES DE LOS DISPOSITIVOS
for device in devices:
   #devices.add_row([device["hostname"],device["platformId"],device["softwareType"],device["softwareVersion"],device["upTime"]])
   print("Hostname: {}".format(device["hostname"]),)"""


