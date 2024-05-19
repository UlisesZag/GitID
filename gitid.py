import os
import sys
import json

script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
config_path = script_dir + "gitid-users.json"

config = {}

def print_users():
    print("Usuarios:")
    print("---------------------------------------------")
    for i, user in enumerate(config["users"]):
        print(f"{i}: {user["git_username"]}")
    print("---------------------------------------------")

def load_config():
    if not os.path.exists("gitid-users.json"):
        f = open(config_path, "w")
        f.write('{"users": []}')
        f.close()

    configfile = open(config_path, "r")
    configjson = configfile.read()
    return json.loads(configjson)
   

def print_current_gitid():
    print("Current git id:")
    os.system("git config --global user.name")

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

def gitid_add():
    new_user = {}
    new_user["git_username"] = input("git user.name: ")
    new_user["git_email"] = input("git user.email: ")
    
    config["users"].append(new_user)
    
    save_config()
    
    print("Added user", new_user["git_username"])

def save_config():
    f = open(config_path, "w")
    f.write(json.dumps(config))
    f.close()

def gitid_remove():
    print_users()
    
    try:
        quien = int(input(":"))
    except ValueError:
        print("Usuario invalido. Ingrese un usuario valido")
        return
    
    if quien >= len(config["users"]) or quien < 0:
        print("Usuario invalido. Ingrese un usuario valido")
        return
    
    config["users"].pop(quien)
    
    save_config()
    print("Usuario removido.")

if __name__ == "__main__":
    config = load_config()

    if len(sys.argv) == 1:
        print_current_gitid()
    else:
        if sys.argv[1] == "auth":
            gitid_auth()
        if sys.argv[1] == "add":
            gitid_add()
        if sys.argv[1] == "remove":
            gitid_remove()
        if sys.argv[1] == "list":
            print_users()