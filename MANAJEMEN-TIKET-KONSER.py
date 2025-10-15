from prettytable import PrettyTable
import os
import pwinput
import json 


def login_user():
    print("Sudah punya akun? (Y/N)")
    jwb = input(">> ")
    jwb = jwb.upper().strip()

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
    
def read_tiket():
    print("Daftar Tiket")

    with open("tiket.json", "r") as r:
        data = json.load(r)

    tabel_tiket = PrettyTable()
    tabel_tiket.field_names = ["No", "Id Tiket", "Nama Konser", "Tanggal", "Lokasi", "Kategori", "Harga", "Stok", "Terjual"]

    for i, tiket in enumerate(data, start=1):
        tabel_tiket.add_row([
            i,
            tiket["id_tiket"],
            tiket["nama_konser"],
            tiket["tanggal"],
            tiket["lokasi"],
            tiket["kategori"],
            tiket["harga"],
            tiket["stok"],
            tiket["terjual"]
        ])

    print(tabel_tiket)

    return tabel_tiket

def create_tiket():
    print("Tambah Tiket Konser")

    id_tiket = input("Masukkan Id Tiket: ")
    nama_konser = input("Masukkan Nama Konser: ")
    tanggal = input("Masukkan Tanggal: ")
    lokasi = input("Masukkan Lokasi: ")
    while True:
        kategori = input("Masukkan Kategori (VIP/Reguler): ").strip()
        if kategori == "VIP" or kategori == "Reguler":
            break
        else:
            print("Kategori harus VIP atau Reguler. Silahkan coba lagi!")
    while True:
        try:
            harga = int(input("Masukkan harga (cth: 200000): "))
            break
        except ValueError:
            print("inputan harus berupa angka!!")
            
    while True:
        try:
            stok = int(input("Masukkan stok: "))
            break
        except ValueError:
            print("inputan harus berupa angka!!")

    tiket_terbaru = {
        "id_tiket" : id_tiket,
        "nama_konser" : nama_konser,
        "tanggal" : tanggal,
        "lokasi" : lokasi,
        "kategori" : kategori,
        "harga" : harga,
        "stok" : stok,
        "terjual" : 0
    }

    # data.append(tiket_terbaru)
    try:
        with open("tiket.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []  

    data.append(tiket_terbaru)

    with open("tiket.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"tiket dengan ID {tiket_terbaru['id_tiket']} berhasil ditambahkan ")


def admin():
    while True: 
        print("\nSelamat datang admin di sistem manajemen tiket konser\nSilahkan pilih menu dibawah ini:")
        print("1. Lihat tiket konser")
        print("2. Tambah tiket konser")
        print("3. Update tiket konser")
        print("4. Delete tiket konser")
        print("4. logout")

        try:    
            pilihan = int(input("Masukkan pilihan (wajib angka pilihan): ").strip())
        except ValueError:
            print("Input harus berupa angka")

        if pilihan == 1:
            read_tiket()
        elif pilihan == 2:
            create_tiket()
        elif pilihan == 3:
            print("menu update tiket")
        elif pilihan == 4:
            print("anda logout")
            break
        else:
            print("input tidak ada di daftar menu! coba lagi")

def pembeli():
    while True:
        print("\nSilahkan pilih menu dibawah ini:")
        print("1. Lihat Tiket Yang dijual")
        print("2. Cek Saldo")
        print("3. Beli tiket konser")
        print("4. logout")

        try:
            pilihan = input(int("Masukkan pilihan (wajib angka pilihan): "))
        except ValueError:
            print("Inputan berupa angka!")

        if pilihan == 1:
            print("menu lihat tiket")
        elif pilihan == 2:
            print("menu Tambah tiket")
        elif pilihan == 3:
            print("menu update tiket")
        elif pilihan == 4:
            print("anda logout")
            break
        else:
            print("input tidak ada di daftar menu! coba lagi")
    


# menu utama
while True:
    print("\nSelamat datang di sistem manajemen tiket konser\nMasukkan pilihan menu")
    print("1. Login")
    print("2. Keluar")

    try:
        menu = int(input("masukkan menu (angka menu): "))
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
        elif menu == 2:
            print("terimakasih, program selesai!!")
            break
        else:
            print("\nmenu tidak ada. ulang!!!")
    except ValueError:
        print("\ninputan harus angka")


    

            
            
            
