import json
import os

baseDeDatos = []

def crearArchivoJson():
    if not os.path.isfile("baseDeDatos.json"):
        with open("baseDeDatos.json", "w") as archivo:
            json.dump([], archivo)

def registroDeUsuario():
    print("Bienvenido al registro de usuario".center(30, "-"))
    print("Completa los siguientes campos para poder registrarte")

    mail = input("Mail: ")
    password = input("Contraseña: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")

    user = {
        "mail": mail,
        "password": password,
        "nombre": nombre,
        "apellido": apellido

    }

    with open("baseDeDatos.json", "r") as archivo:
         baseDeDatos = json.load(archivo)

    baseDeDatos.append(user)

    with open("baseDeDatos.json", "w") as archivo:
        json.dump(baseDeDatos, archivo)

def iniciarSesion():
    print("Iniciar sesión".center(30, "-"))
    mail = input("Ingrese su mail: ")
    password = input("ingrese su contraseña: ")
    with open("baseDeDatos.json","r") as archivo:
        usuariosCargados = json.load(archivo)

    for e in usuariosCargados:
        if e["mail"] == mail and e["password"] == password:
           return print("Inicio de sesion exitoso".center(40,"-"))

    return print("Mail o contraseña incorrectos".center(40,"-"))


def menu():
    print("CoderHouse".center(30, "-"))
    opcion = int(input("Seleccione una de las siguientes opciones: \n1)Iniciar sesion\n2)Registrarse\n3)Salir\n"))
    if opcion == 3:
        print("Adios".center(30,"-"))

    elif opcion == 2:
        registroDeUsuario()
        menu()

    elif opcion == 1:
        iniciarSesion()

crearArchivoJson()
menu()