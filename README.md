# Entorno de virtualización Python

# Pasos de instalación en Linux:

## 1. Clonación del proyecto

Desde la terminal ejecutar:

**git clone** <URL_del_repositorio> <nombre_de_la_carpeta_de_destino>

Luego ejecutar **cd** <nombre_de_la_carpeta_de_destino>. Esta carpeta será la raíz de nuestro proyecto en Python.

## 2. Creación del entorno virtual

Supongamos que el nombre que le damos al entorno virtual es **cisco**, entonces se creará una carpeta **cisco** con todas las librerías y dependencias necesarias paea nuestro proyecto. 

La manera de realizarlo es la siguiente:

# python3 -m venv <nombre_del_entorno>
Ejemplo: python3 -m venv cisco

Para activar el entorno escribimos **source cisco/bin/activate**, en la carpeta raíz del proyecto. El nombre del entorno virtual aparecerá entre paréntesis ().

## 3. Instalación de las dependencias, en este caso las librerías requests y tabulate

En la carpeta raíz de nuestro proyecto y dentro del entorno virtual escribimos: **pip install -r requirements.txt**

## 4. Selección del intérprete Python para nuestro entorno virtual

<img width="881" height="118" alt="image" src="https://github.com/user-attachments/assets/18c41d8e-d338-48b6-953c-b2499c57319f" />

<img width="736" height="412" alt="image" src="https://github.com/user-attachments/assets/2a795fcd-2cf8-47ef-a5a6-d21e09ce967f" />

Tal como se ve en la figura seleccionamos Python 3.10.12 (cisco) que se mostrará como entorno recomendado.

## 5. Desactivación del entorno virtual

Simplemente escribimos en la línea de comandos: **deactivate**



## Antes de ejecutar los scripts

> En esta copia del grupo ya no aplica: los scripts piden usuario, clave y ticket al ejecutarse (ver la sección TP4 – Grupo 10).
- **Credenciales del controlador:** los scripts usan el usuario `cisco` y la clave `cisco123!`. Si en tu Network Controller creaste otro usuario, cambialos en `01_get-ticket.py` y en `04_tabulate.py`.
- **Ticket (X-Auth-Token):** `02_get-network-device.py` y `03_get-host.py` traen escrito un ticket de ejemplo que **no va a funcionar** en tu Packet Tracer, porque el controlador genera uno nuevo en cada sesión y vence. Ejecutá primero `01_get-ticket.py`, copiá el ticket que muestra y reemplazalo en el header `X-Auth-Token` de esos dos scripts. `04_tabulate.py` no necesita este paso: pide el ticket solo.

---

# TP4 – Grupo 10 (Redes de Computadoras 3643, UNLaM)

Copia del repositorio de la cátedra usada para la actividad 4 del TP N° 4 (Integrador). La API es la del Network Controller de Packet Tracer, expuesta en `http://localhost:58000/api/v1` (Options → Preferences → Miscellaneous → *Enable External Access for Network Controller REST API*, y en el controlador Config → Real World → Controller → *Access Enabled*).

## Qué hace cada script

| Script | Qué hace |
|---|---|
| `src/01_get-ticket.py` | Pide usuario y clave del controlador y obtiene un ticket con `POST /ticket`. |
| `src/02_get-network-device.py` | Pide el ticket y lista los equipos de red (`GET /network-device`): hostname, plataforma e IP de gestión. |
| `src/03_get-host.py` | Pide el ticket y lista los hosts (`GET /host`): nombre, IP, MAC e interfaz a la que se conectan. |
| `src/04_tabulate.py` | Pide usuario y clave, obtiene el ticket solo y muestra equipos y hosts en tablas. |
| `src/05_inventario_csv.py` | **Script propio.** Pide usuario y clave, muestra los equipos de red y los hosts en tablas, indica cuáles equipos no están en *Managed* y guarda el inventario en `inventario.csv`. |

## Cambios respecto de los scripts de la cátedra

- **Sin credenciales en el código:** como el repositorio es público, los scripts piden el usuario y la clave al ejecutarse (la clave con `getpass`, sin mostrarla) en lugar de tenerlos escritos. `02` y `03` piden el ticket que muestra `01`.
- **Equipos sin hostname:** en nuestra topología el ISP aparece en el inventario con *Wrong credential* y sin `hostname`; `02` y `04` usan `.get()` para que esa entrada no corte la ejecución.

## Uso (Windows)

```
python -m venv cisco
cisco\Scripts\activate
pip install -r requirements.txt
python src\05_inventario_csv.py
```

Con Packet Tracer abierto y el archivo del TP cargado. El CSV generado queda excluido del repositorio por el `.gitignore`.
