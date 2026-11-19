import json
import requests
from getpass import getpass
api_url = "http://localhost:58000/api/v1/ticket"

headers = {
    "content-type": "application/json"
}

body_json = {
    "username": input("Usuario del controlador [cisco]: ") or "cisco",
    "password": getpass("Clave del controlador: ")
}

resp = requests.post(api_url, json.dumps(body_json), headers=headers)

print("Ticket request status: ", resp.status_code)
response_json = resp.json()
print (response_json)
serviceTicket = response_json["response"]["serviceTicket"]

print("The service ticket number is: ", serviceTicket) 