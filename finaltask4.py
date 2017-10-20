import re
import requests
import json

controller='https://sandboxapic.cisco.com/'

def getTicket():
url = "https://" + controller + "/api/v1/ticket"
payload ={'username = devnet','password = cisco123'}
response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
print(response)




