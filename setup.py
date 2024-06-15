import json
import os
from modules import Extra


def getUsername():
    retry = True
    while retry:
        username = input("Enter username\n")
        if input(f'Is {username} correct. If mistaken. Type "N" to retry. Hit enter to continue\n').upper() == "N":
            pass
        else:
            return username


def getPassword():
    retry = True
    while retry:
        password = input("Enter password\n")
        if input(f'Is {password} correct. If mistaken. Type "N" to retry. Hit enter to continue\n').upper() == "N":
            pass
        else:
            return password


def setup():
    users = []
    addAccount = True
    Extra.printYellow("{0:{1}^40}".format(' setup.py ', "="))
    skipPassword = input('Do all accounts share the same password? Type "Y" for Yes. Hit enter for no\n').upper()
    if skipPassword == "Y":
        password = getPassword()
    while addAccount:
        username = getUsername()
        if skipPassword == "Y":
            pass
        else:
            password = getPassword()

        userData = {"user": username, "pass": password}
        users.append(userData)
        with open("accounts.json", "w") as json_file:
            json.dump(users, json_file, indent=4)
        if input('Type "Y" to add another account, or enter to finish setup.\n').upper() == "Y":
            pass
        else:
            addAccount = False

if __name__ == "__main__":
    if os.path.exists(f"{os.getcwd()}/accounts.json"):
        if input('accounts.json exists. Continuing will reset the file. Type "Y" to continue.\n').upper() == "Y":
            setup()
        else:
            print("Exiting setup.py")
            exit()
    else:
        setup()
