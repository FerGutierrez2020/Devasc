import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_PORT, DNAC_USER, DNAC_PASSWORD


def get_network_devices():
    """
    Building out function to retrieve network devices
    """
    token = get_auth_token() # Get Token
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    resp = requests.get(url, headers=hdr)  # Make the Get Request
    device_list = resp.json()
    print(resp.text)
    #print(f'response status code: {resp.status_code}')


def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to get a token from DNAC
    """
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'     # Token URL
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD))  # Make the POST Request
    token = resp.json()['Token']    # Retrieve the Token 
    print("Token generated for an hour is: "+token)
    return token    # Create a return statement for the Token
    

if __name__ == "__main__":
    get_network_devices()
