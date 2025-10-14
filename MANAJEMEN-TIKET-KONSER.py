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

        for akun in data:
            if username == akun['username'] and password == akun['password']:
                print("Login Berhasil")
                return akun
            
        print("Username atau Password salah")
        return None
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

def admin():
    print("\nSelamat datang admin di sistem manajemen tiket konser\nSilahkan pilih menu dibawah ini:")
    print("1. Lihat tiket-tiket yang sudah terjual")
    print("2. Tambah tiket konser")
    print("3. Update tiket konser")
    print("4. logout")
    
    pilihan = int(input("Masukkan Pilihan Menu: "))
    if pilihan == 1:
        print("menu lihat tiket")
    elif pilihan == 2:
        print("menu Tambah tiket")
    elif pilihan == 3:
        print("menu update tiket")
    else:
        print("anda logout")
    

# menu utama
print("\nSelamat datang di sistem manajemen tiket konser\nMasukkan pilihan menu")
print("1. Login")
print("2. Keluar")

menu = int(input("masukkan menu: "))

if menu == 1:
    akun_login = None

    while akun_login is None:
        akun_login = login_user()

        if akun_login is None:
            print ("silahkan coba lagi\n")
        else:
            if akun_login['role'] == "admin":
                admin()
            elif akun_login["role"] == "user":
                print("menu pembeli")

else:
    print("terimakasih, program selesai!!")


        
        
        