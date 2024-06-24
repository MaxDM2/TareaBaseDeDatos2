import requests
import time

base_url = "http://localhost:3000"


#Para editar los prints
class color:
    reset = '\033[0m'
    stylish = '\033[96;1m'
    underline = '\033[4m'
    error = '\033[91;1m'


#endpoints
def registrar_usuario(nombre, email, clave, descripcion):
    url=f"{base_url}/api/registrar"
    payload = {     #Crea el formato de json
        "nombre": nombre,
        "direccion_correo": email,
        "clave": clave,
        "descripcion": descripcion,
    }
    response = requests.post(url,json=payload)
    if response.status_code == 201:
        data = response.json()  #guarda lo que se ingresa al json
        print("Usuario registrado con exito")
        print(data)
    else:
        print("Error en la solicitud")
        print(color.error + response.text)
    return

def bloquear_usuario(email, clave, correo_bloquear):
    url=f"{base_url}/api/bloquear"
    payload = {           #Crea el formato de json
        "email": email,
        "clave": clave,
        "correo_bloquear": correo_bloquear,
    }
    response = requests.post(url,json=payload)
    return response.json

def informacion_usuario(correo_info):
    url=f"{base_url}/api/{correo_info}" #completa la url con el correo ingresado
    response = requests.get(url)        #hace un get a esa url

    if response.status_code == 200:   #chequea que no haya ningun error e imprime la info.
        data = response.json()
        print("Solicitud exitosa")
        print("Data", data)
    else:
        print("Error en la solicitud") #si hay error lo printea
        print(color.error + "ERROR: " + response.text)
    return

#Interfaz
print("[--]     " + color.underline + "Bienvenido a CommuniKen" + color.reset +    "     [--]")
print("[--]                                 [--]")
print("[--]    Seleccione una opcion        [--]")
print("[--]    para continuar:              [--]")
print("[--]_________________________________[--]")
print("")

opcion = 0
while opcion != 5:
    time.sleep(1)
    print(color.stylish + "  [1]  " + color.reset +  "Enviar un correo")
    print(color.stylish + "  [2]  " + color.reset +  "Ver informacion de un correo electronico")
    print(color.stylish + "  [3]  " + color.reset +  "Ver correos marcados como favoritos")
    print(color.stylish + "  [4]  " + color.reset +  "Marcar correo como favorito")
    print(color.stylish + "  [5]  " + color.reset +  "Terminar la ejecucion del cliente")
    print("")
    opcion = int(input("Ingrese su opcion: "))

    if opcion == 1:
        print(color.error + "Error: Funcion no disponible\n")
    elif opcion == 2:
        correo = input("Ingrese el correo: ")
        informacion_usuario(correo)
    elif opcion == 3:
        print("No tiene correos marcados como favoritos\n")
    elif opcion == 4:
        correo = input("Ingrese el correo a marcar como favorito ")