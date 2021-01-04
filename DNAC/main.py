###Este Script en Python obtiene un token de DNAC 
# y obtiene la lista de los dispositivos de la red
#By Sage IT
import requests

url="https://sandboxdnac2.cisco.com"
username = 'devnetuser'
password = 'Cisco123!'

def get_auth_token():
    #Funcion para obtener el token

    auth_url= url + "/dna/system/api/v1/auth/token"
    auth_header = {
        "content-type:application/json"
    }

    response= requests.request("POST",auth_url,auth=(username, password),headers=auth_header,verify=False)
    print(f"Response status code{response.status_code}")
    print(f"Response text{response.text}")

    if response.status_code==requests.codes.ok:
        token=response.json()["token"]
        return token
    print (token)

if __name__ == "__main__":
    token = get_auth_token()
    print (token)
