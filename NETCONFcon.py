
from ncclient import manager

m = manager.connect(host="172.16.98,128", port=830, username="cisco", password="cisco123!", hostkey_verify=False)