#!/usr/bin/env python3
import os
import sys
import json

script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
config_path = os.path.expanduser("~/.gitid-users.json")

config = {}

####################### Command Functions ##########################

# Command: gitid
def print_current_gitid():
    print("Git id actual:")
    os.system("git config --global user.name")

# Command: gitid list
def print_users():
    print("----------------------------[ Usuarios ]-----------------------------")
    print("ID Nombre                           E-Mail               ")
    print("---------------------------------------------------------------------")
    for i, user in enumerate(config["users"]):
        #print(f"{i}: {user["git_username"]}")
        print("%-2i %-32s %-32s" % (i, user["git_username"], user["git_email"]))
    print("---------------------------------------------------------------------")

# Command: gitid auth
def gitid_auth():
    print_users()
    
    try:
        quien = int(input(":"))
    except ValueError:
        print("Usuario invalido. Ingrese un usuario valido")
        return
    
    if quien >= len(config["users"]) or quien < 0:
        print("Usuario invalido. Ingrese un usuario valido")
        return
    
    os.system(f"git config --global user.name \"{config["users"][quien]["git_username"]}\"")
    os.system(f"git config --global user.email {config["users"][quien]["git_email"]}")
    os.system("gh auth logout")
    print(f"Seleccione la cuenta de Github correspondiente a {config["users"][quien]["git_username"]}")
    os.system("gh auth login -w -p \"HTTPS\"")
    print(f"LOGGEADO COMO USUARIO: {config["users"][quien]["git_username"]}")

# Command: gitid add
def gitid_add():
    new_user = {}
    new_user["git_username"] = input("git user.name: ")
    new_user["git_email"] = input("git user.email: ")
    
    config["users"].append(new_user)
    
    save_config()
    
    print("Añadido usuario", new_user["git_username"])

# Command: gitid remove
def gitid_remove():
    print_users()
    
    try:
        quien = int(input("Usuario a remover: "))
    except ValueError:
        print("Usuario invalido. Ingrese un usuario valido")
        return
    
    if quien >= len(config["users"]) or quien < 0:
        print("Usuario invalido. Ingrese un usuario valido")
        return
    
    config["users"].pop(quien)
    
    save_config()
    print("Usuario removido.")

def gitid_help():
    print(
"""Comandos de gitid
  gitid: Imprimir el usuario logeado
  gitid list: Listar los usuarios disponibles
  gitid add: Agregar un usuario
  gitid remove: Remover un usuario
  gitid auth: Autenticarse como un usuario (configurar git y logearse en gh)

                            Este gitid tiene poderes de super """
)

############################# Save/Load Functions #################################

def load_config():
    if not os.path.exists(config_path):
        f = open(config_path, "w")
        f.write('{"users": []}')
        f.close()

    configfile = open(config_path, "r")
    configjson = configfile.read()
    return json.loads(configjson)
   
def save_config():
    f = open(config_path, "w")
    f.write(json.dumps(config))
    f.close()


if __name__ == "__main__":
    #Si esta corriendo como root, el login falla. Bloquea esta posibilidad
    if os.name == "posix" and os.getuid() == 0:
        print("Error: Gitid no debe correrse como root.")
        sys.exit()

    config = load_config()

    if len(sys.argv) == 1:
        print_current_gitid()
    else:
        if sys.argv[1] == "auth":
            gitid_auth()
        elif sys.argv[1] == "add":
            gitid_add()
        elif sys.argv[1] == "remove":
            gitid_remove()
        elif sys.argv[1] == "list":
            print_users()
        elif sys.argv[1] == "help":
            gitid_help()
        else:
            print("Comando invalido. Use \"gitid help\" para obtener una lista de comandos.")