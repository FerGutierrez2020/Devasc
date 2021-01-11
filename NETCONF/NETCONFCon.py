from ncclient import manager

if __name__ == '__main__':
    csr1= manager.connect(host="172.16.98.128",
                      port=830,
                      username='cisco',
                      password="cisco123!",
                      hostkey_verify=False)
for csr1_capability in csr1.server_capabilities:
        print(csr1_capability)