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

            return True
        else :
            print("Username atau Password salah")
            return False
    else:
        print("Buatkan akun baru")
        username = input("Username Baru: ")
        password = input("password Baru: ")
        role = "user"
        saldo = 0

        akun_baru = {"username" : username, "password" : password, "role" : role, "saldo" : saldo}
        data.append(akun_baru)
        with open("akun.json", "w") as f:
            json.dump(data, f, indent=4)
        print("akun berhasil dibuat")
        return akun_baru


# print("\nmenu utama")
# while True:

#     print("\nSelamat datang di sistem manajemen tiket konser\nSilahkan Login!!")

#     konfirmasi = 'Y'
#     while konfirmasi == "Y":
#         akun = login_user()
#         if akun["role"] == "admin":
#             print("masuk men")
#         elif:
#             print("akun pembeli")
        
#         input("Ingin Melanjutkan? =")
