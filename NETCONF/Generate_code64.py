""" Generate Base64 encoding using the base64 library """ 
import base64 
encoded = base64.b64encode('user1:cisco123'.encode('UTF-8')).decode('ASCII')
print(encoded)