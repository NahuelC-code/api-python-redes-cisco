#Script propio - TP4 Grupo 10
#Inventario de los equipos de red y hosts que ve el controlador, exportado a un archivo CSV

#Módulos que se usarán
import requests #Para entender solicitudes
import json #Para reconocer el formato json
import csv #Para crear el archivo CSV
from getpass import getpass #Para pedir la clave sin mostrarla
from tabulate import * #Para crear tablas

baseUri = "http://localhost:58000/api/v1" #URL de PT

# Llamada al API por el ticket
headers = {"Content-Type": "application/json"} #Headers
usuario = input("Usuario del controlador [cisco]: ") or "cisco"
clave = getpass("Clave del controlador: ")
data = json.dumps({"username": usuario, "password": clave}) #Credenciales
resp = requests.post(baseUri+"/ticket", data=data, headers=headers) #URL específica

print("Status de Solicitud:")
print(resp.status_code)
result = resp.json()

ticket = result["response"]["serviceTicket"] #Printing ticket
print("\nEl Service Ticket es:")
print(ticket)


# Llamada al API para recibir los dispositivos de red
headers = {"X-Auth-Token": ticket}
resp = requests.get(baseUri+"/network-device", headers=headers) #URL específica
result = resp.json()

print("\nDispositivos de Red:")
device_list = [] #Filas para la tabla de pantalla
csv_list = [] #Filas para el archivo CSV
no_managed = [] #Equipos que el controlador no administra
for item in result["response"]:
    hostname = item.get("hostname") or "(sin acceso)" #El ISP no tiene hostname (Wrong credential)
    device_list.append([hostname, item.get("type", ""), item.get("productId", ""), item["managementIpAddress"], item["collectionStatus"]])
    csv_list.append(["Equipo de red", hostname, item.get("type", ""), item.get("productId", ""), item["managementIpAddress"], item.get("macAddress", ""), item["collectionStatus"], ""])
    if item["collectionStatus"] != "Managed":
        no_managed.append(item["managementIpAddress"] + " -> " + item["collectionStatus"])

print(tabulate(device_list, headers=["Hostname", "Tipo", "Modelo", "IP de gestión", "Estado"], tablefmt='rst')) #Tabla ordenada


# Llamada al API para recibir los host
headers = {"X-Auth-Token": ticket}
resp = requests.get(baseUri+"/host", headers=headers) #URL específica
result = resp.json()

print("\nHosts de la Red:")
host_list = []
for item in result["response"]:
    host_list.append([item["hostName"], item["hostType"], item["hostIp"], item["connectedInterfaceName"]])
    csv_list.append(["Host", item["hostName"], item["hostType"], "", item["hostIp"], item["hostMac"], "", item["connectedInterfaceName"]])

print(tabulate(host_list, headers=["Host", "Tipo", "IP", "Interfaz del switch"], tablefmt='rst')) #Tabla ordenada


# Resumen: cantidad de equipos administrados y los que no lo están
print("\nResumen:")
print("Equipos de red:", len(device_list), "- Managed:", len(device_list) - len(no_managed))
print("Hosts:", len(host_list))
for equipo in no_managed:
    print("No administrado:", equipo)


# Creación del archivo CSV (separado por ";" para abrirlo con Excel)
archivo = open("inventario.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(archivo, delimiter=";")
writer.writerow(["Categoria", "Nombre", "Tipo", "Modelo", "IP", "MAC", "Estado", "Interfaz"]) #Encabezado
writer.writerows(csv_list) #Una fila por equipo o host
archivo.close()
print("\nInventario guardado en inventario.csv")
