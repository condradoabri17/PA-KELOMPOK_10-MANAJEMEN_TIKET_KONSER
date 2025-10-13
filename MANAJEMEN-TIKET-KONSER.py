from prettytable import PrettyTable
import os
import pwinput

def login_user():
    print("Sudah punya akun? (Y/N)")
    jwb = input(">> ")

    if jwb == "Y":
        username = input("Username : ")
        password = input("Password : ")

        if username == user["username"] and user["password"] == password:
            print("-" * 90)
            print("Login Berhasil")
            print("-" * 90)