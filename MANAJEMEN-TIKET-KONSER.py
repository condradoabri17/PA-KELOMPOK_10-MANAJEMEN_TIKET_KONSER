from prettytable import PrettyTable
import os
import pwinput
import json 


def login_user():
    print("Sudah punya akun? (Y/N)")
    jwb = input(">> ")

    if jwb == "Y":
        with open("akun.json") as f:
            data = json.load(f)

        username = input("Username : ")
        password = pwinput.pwinput("Password : ")

        ditemukan = False
        for akun in data:
            if username == akun['username'] and password == akun['password']:
                ditemukan = True
                break 
        
        if ditemukan == True:
            print("Login Berhasil")
            print("-" * 90)