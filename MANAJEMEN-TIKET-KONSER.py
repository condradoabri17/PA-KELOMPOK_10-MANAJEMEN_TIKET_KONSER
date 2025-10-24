from prettytable import PrettyTable
from datetime import datetime
import os
import pwinput
import random
import string
import json 

session = None

def login_user():
    while True:
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
            break
        elif jwb == "N":
            with open("akun.json") as f:
                data = json.load(f)
            while True:
                print("Buatkan akun baru")
                username = input("Username Baru: ").strip()
                password = pwinput.pwinput("Password Baru: ").strip()
                role = "user"
                saldo = 0

                if username == "" or password == "":
                    print("Anda tidak memasukkan apapun! Silakan coba lagi.\n")
                    continue

                elif any(a["username"] == username for a in data):
                    print("Username sudah digunakan! Coba nama lain.\n")
                    continue

                akun_baru = {
                    "username": username,
                    "password": password,
                    "role": role,
                    "saldo": saldo
                }
                data.append(akun_baru)
                break 

            with open("akun.json", "w") as f:
                json.dump(data, f, indent=4)

            print("Akun berhasil dibuat!")
            return akun_baru

        else:
            print("Inputan tidak tersedia, coba lagi!")
    


def read_tiket():
    print("Daftar Tiket Konser yang tersedia")

    with open("tiket.json", "r") as f:
        data =json.load(f)

    if not data:
        print("Belum ada tiket yang tersedia.")
        return
        
    if session and session.get("role") == "user":
        table = PrettyTable(["ID Tiket", "Nama Konser", "Tanggal", "Harga", "Stok"])
        for tiket in data:
            if tiket.get("stok", 0) > 0:
                table.add_row([
                    tiket.get("id_tiket", "-"),
                    tiket.get("nama_konser", "-"),
                    tiket.get("tanggal", "-"),
                    tiket.get("harga", "-"),
                    tiket.get("stok", "-")
                ])
        print(table)
    else:
        table = PrettyTable(["ID Tiket", "Nama Konser", "Tanggal", "Harga", "Stok", "Terjual"])
        for tiket in data:
            table.add_row([
                tiket.get("id_tiket", "-"),
                tiket.get("nama_konser", "-"),
                tiket.get("tanggal", "-"),
                tiket.get("harga", "-"),
                tiket.get("stok", "-"),
                tiket.get("terjual", "-")
            ])
        print(table)

def id_tiket_otomatis():
   
    with open("tiket.json", "r") as f:
        data = json.load(f)

    if not data:
        return "T001"
    else:
        last_id = data[-1]["id_tiket"]
        angka = int(last_id[1:]) + 1
        return f"T{angka:03d}"

def create_tiket():
    print("Tambah Tiket Konser")
    
    id_tiket =  id_tiket_otomatis()
    print(f"ID Tiket Otomatis: {id_tiket}")
    
    nama_konser = input("Masukkan Nama Konser: ")
    while True:
        try:
            tanggal_input = input("Masukkan Tanggal (dd-mm-yyyy): ")
            tanggal = datetime.strptime(tanggal_input, "%d-%m-%Y")
            sekarang = datetime.now()
            
            if tanggal < sekarang:
                print("Tanggal tidak boleh lebih lama dari hari ini!")
            else:
                break
        except ValueError:
            print("Inputan tidak valid silahkan coba lagi")
            
    lokasi = input("Masukkan Lokasi: ")
    
    while True:
        kategori_input = input("Masukkan Kategori (VIP/Reguler): ").strip().lower()
        if kategori_input == "vip" or kategori_input == "reguler":
            kategori = "VIP" if kategori_input == "vip" else "Reguler"
            break
        else:
            print("Kategori harus VIP atau Reguler. Silahkan coba lagi!")
    while True:
        try:
            harga = int(input("Masukkan harga (maks: 2000000): "))
            if harga <= 0:
                print("Harga yang diinput tidak boleh 0 atau mines") 
            elif harga > 20000000:
                print("Nominal maksimal adalah 20000000")
            else:
                break
        except ValueError:
            print("inputan harus berupa angka!")
            
    while True:
        try:
            stok = int(input("Masukkan stok: "))
            if stok <= 0:
                print("Stok tidak boleh 0 atau minus!")
            elif stok > 100000:
                print("stok Tidak boleh melebihi 100.000 tiket")
            else:
                break
        except ValueError:
            print("inputan harus berupa angka!")

    tiket_terbaru = {
        "id_tiket" : id_tiket,
        "nama_konser" : nama_konser,
        "tanggal": tanggal.strftime("%d-%m-%Y"),
        "lokasi" : lokasi,
        "kategori" : kategori,
        "harga" : harga,
        "stok" : stok,
        "terjual" : 0
    }

    try:
        with open("tiket.json", "r") as f:
            isi_data = f.read().strip()
            if not isi_data:
                data = []
            else : 
                data = json.loads(isi_data)

    except FileNotFoundError:
        data = []  

    data.append(tiket_terbaru)

    with open("tiket.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"tiket dengan ID {tiket_terbaru['id_tiket']} berhasil ditambahkan ")

def update_tiket():
    print("Update data Tiket")

    with open("tiket.json", "r") as f:
        cek_data = f.read().strip()
        if not cek_data:
            print("Belum ada data tiket yang tersedia untuk diupdate.")
            return
        data = json.loads(cek_data)
    
    read_tiket()

    tiket_ditemukan = None

    while tiket_ditemukan == None:

        id_tiket_edit = input("Masukkan ID Tiket yang mau diedit: ")

        for tiket in data:
            if tiket["id_tiket"] == id_tiket_edit:
                tiket_ditemukan = tiket
                break

        if tiket_ditemukan is None:
            print(f"Tiket dengan ID {id_tiket_edit} tidak ditemukan")
            

    tabel_edit = PrettyTable()
    tabel_edit.field_names = ["Id Tiket", "Nama Konser", "Tanggal", "Lokasi", "Kategori", "Harga", "Stok", "Terjual"]
    tabel_edit.add_row([
        tiket_ditemukan["id_tiket"],
        tiket_ditemukan["nama_konser"],
        tiket_ditemukan["tanggal"],
        tiket_ditemukan["lokasi"],
        tiket_ditemukan["kategori"],
        tiket_ditemukan["harga"],
        tiket_ditemukan["stok"],
        tiket_ditemukan["terjual"]
    ])
    print("\nData Tiket Yang Dipilih: ")
    print(tabel_edit)

    nama_baru = input(f"Nama Konser [{tiket_ditemukan['nama_konser']}]: ").strip()
    tanggal_baru = input(f"Tanggal [{tiket_ditemukan['tanggal']}]: ").strip()
    lokasi_baru = input(f"Lokasi [{tiket_ditemukan['lokasi']}]: ").strip()
    kategori_baru = input(f"Kategori [{tiket_ditemukan['kategori']}]: ").strip()

    while True:
    
        harga_baru = input(f"Harga [{tiket_ditemukan['harga']}]: ").strip()
        if not harga_baru:
            break
        try:
            tiket_ditemukan['harga'] = int(harga_baru)
            break
        except:
            print("Input harga harus berupa angka!!")
        
    while True:

        stok_baru = input(f"Stok [{tiket_ditemukan['stok']}]: ").strip()
        if not stok_baru:
            break
        try:
            tiket_ditemukan["stok"] = int(stok_baru)
            break
        except:
            print("Input stok harus angka")

    if nama_baru: tiket_ditemukan['nama_konser'] = nama_baru
    if tanggal_baru: tiket_ditemukan['tanggal'] = tanggal_baru
    if lokasi_baru: tiket_ditemukan['lokasi'] = lokasi_baru
    if kategori_baru: tiket_ditemukan['kategori'] = kategori_baru


    with open("tiket.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Tiket dengan ID {id_tiket_edit} berhasil diperbarui!")

def delete_tiket():
    print("Hapus Tiket")

    with open("tiket.json", "r") as f:
        cek_data = f.read().strip()
        if not cek_data:
            print("Belum ada data tiket yang tersedia untuk dihapus.")
            return
        data = json.loads(cek_data)

    print("Berikut tiket yang tersedia:")
    read_tiket()

    tiket_ditemukan = None

    while tiket_ditemukan is None:
        id_tiket_hapus = input("Masukkan ID Tiket yang mau dihapus: ")
        
        for tiket in data:
            if tiket["id_tiket"] == id_tiket_hapus:
                tiket_ditemukan = tiket
                break
        
        if tiket_ditemukan is None:
            print(f"Tiket dengan ID {id_tiket_hapus} tidak ditemukan. Silahkan coba lagi.\n")

    print("\nData yang akan dihapus:")
    print(tiket_ditemukan)

    data = [t for t in data if t["id_tiket"] != id_tiket_hapus]

    with open("tiket.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"\nData dengan ID {id_tiket_hapus} berhasil dihapus!")

# def lihat_tiket():
#     print("Daftar Tiket Konser yang tersedia")

#     with open("tiket.json", "r") as r:
#         isi_data = r.read().strip()
#         if not isi_data:
#             print("Data Tiket yang tersedia belum ada. silahkan tambah atau buat!!")
#             return
#         data = json.loads(isi_data)

#     tabel_tiket = PrettyTable()
#     tabel_tiket.field_names = ["No", "Id Tiket", "Nama Konser", "Tanggal", "Lokasi", "Kategori", "Harga", "Stok"]

#     for i, tiket in enumerate(data, start=1):
#         tabel_tiket.add_row([
#             i,
#             tiket["id_tiket"],
#             tiket["nama_konser"],
#             tiket["tanggal"],
#             tiket["lokasi"],
#             tiket["kategori"],
#             tiket["harga"],
#             tiket["stok"],
#         ])

#     print(tabel_tiket)

#     input("Tekan Enter untuk kembali ke menu...")


def admin(): 
    while True: 
        print("\nSelamat datang admin di sistem manajemen tiket konser\nSilahkan pilih menu dibawah ini:") 
        print("1. Lihat tiket konser") 
        print("2. Tambah tiket konser") 
        print("3. Update tiket konser") 
        print("4. Delete tiket konser") 
        print("5. logout") 

        menu = int(input("Masukkan pilihan (wajib angka pilihan): ")) 
        if menu == 1: 
            read_tiket() 
        elif menu == 2: 
            create_tiket() 
        elif menu == 3:
            update_tiket() 
        elif menu == 4: 
            delete_tiket()
        elif menu == 5:
            global session
            session = None
            print("Anda logout")
            break
        else: 
            print("input tidak ada di daftar menu! coba lagi")


def generate_kode_unik(prefix):
    random_tiket = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}{random_tiket}"

  
def beli_tiket():
    global session
    if session is None:
        print("Kamu belum login!")
        return

    read_tiket()

    with open("tiket.json", "r") as f:
        data_tiket = json.load(f)

    id_tiket = input("\nMasukkan ID Tiket yang ingin dibeli: ").strip()
    tiket_ditemukan = None
    for tiket in data_tiket:
        if tiket["id_tiket"].lower() == id_tiket.lower():
            tiket_ditemukan = tiket
            break

    if tiket_ditemukan is None:
        print("Tiket tidak ditemukan! Pastikan ID benar.")
        return

    while True:
        metode = input("Pilih metode pembelian (online/offline): ").strip().lower()
        if metode == "online" or metode == "offline":
            break
        else:
            print("Pilihan tidak valid! Pilih antara 'online' atau 'offline'.")

    try:
        jumlah_beli = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
        if jumlah_beli <= 0:
            print("Jumlah tiket harus lebih dari 0.")
            return
        elif jumlah_beli > tiket_ditemukan["stok"]:
            print("Jumlah pembelian melebihi stok yang tersedia.")
            return
        elif jumlah_beli > 10 :
            print("Jumlah pembelian maksimal 10 Tiket.")
            return
    except ValueError:
        print("Input jumlah tiket harus berupa angka!")
        return

    total_harga = tiket_ditemukan["harga"] * jumlah_beli

    if metode == "online":
        if session["saldo"] < total_harga:
            print("Saldo Anda tidak cukup untuk melakukan pembelian ini.")
            return

        with open("akun.json", "r") as f:
            data_akun = json.load(f)

        for akun in data_akun:
            if akun["username"] == session["username"]:
                akun["saldo"] -= total_harga
                session["saldo"] = akun["saldo"]
                break

        with open("akun.json", "w") as f:
            json.dump(data_akun, f, indent=4)

        kode_unik = generate_kode_unik("ONL-")
        print("\nTransaksi Online Berhasil")
        print(f"Tiket: {tiket_ditemukan['nama_konser']}")
        print(f"Jumlah dibeli: {jumlah_beli}")
        print(f"Total harga: Rp{total_harga:,}")
        print(f"Sisa saldo Anda: Rp{session['saldo']:,}")
        print(f"Kode Tiket Masuk Anda: {kode_unik}")
        print("Harap simpan kode ini untuk masuk ke konser!\n")

    else:
        kode_unik = generate_kode_unik("OFF-")
        print("\nPembelian Offline Diterima")
        print(f"Tiket: {tiket_ditemukan['nama_konser']}")
        print(f"Jumlah dibeli: {jumlah_beli}")
        print(f"Total harga: Rp{total_harga:,}")
        print(f"Kode Pembayaran Offline: {kode_unik}")
        print("Gunakan kode ini untuk membayar di lokasi konser.\n")

    tiket_ditemukan["stok"] -= jumlah_beli
    tiket_ditemukan["terjual"] += jumlah_beli

    with open("tiket.json", "w") as f:
        json.dump(data_tiket, f, indent=4)

def cek_saldo():
    global session
    if session is None:
        print("Kamu belum login")
        return
    
    print("Cek Saldo Anda")

    with open("akun.json", "r") as f:
        data = json.load(f)

    for akun in data:
        if akun["username"] == session["username"]:
            print(f"Saldo anda saat ini: Rp{akun['saldo']:,}")
            return

    print("Akun tidak ditemukan dalam database.")

def isi_saldo():
    global session
    if session is None:
        print("Kamu belum login!")
        return

    print("\nIsi Saldo")

    while True:
        try:
            tambah_saldo = int(input("Masukkan jumlah saldo yang ingin ditambahkan: "))
            if tambah_saldo <= 0:
                print("Jumlah saldo harus lebih dari 0!")
                continue
            elif tambah_saldo > 25000000:
                print("Jumlah saldo yang diisi tidak boleh lebih dari 25.000.000!!")
                continue
            else:
                break 
        except ValueError:
            print("Inputan harus berupa angka!")
            continue  

    with open("akun.json", "r") as f:
        data = json.load(f)


    for akun in data:
        if akun["username"] == session["username"]:
            akun["saldo"] += tambah_saldo
            session["saldo"] = akun["saldo"]
            break

    with open("akun.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Saldo berhasil ditambahkan sebesar Rp{tambah_saldo:,}")
    print(f"Saldo Anda sekarang: Rp{session['saldo']:,}")

        
def pembeli():
    while True:
        print("\nSilahkan pilih menu dibawah ini:")
        print("1. Lihat Tiket Yang dijual")
        print("2. Cek Saldo")
        print("3. Isi Saldo")
        print("4. Beli tiket konser")
        print("5. Logout")

        menu_input = input("masukkan menu (angka menu): ").strip()
        if not menu_input.isdigit():
            print("Inputan harus berupa angka!")
            continue
        menu = int(menu_input)

        if menu == 1:
            read_tiket()
        elif menu == 2:
            cek_saldo()
        elif menu == 3:
            isi_saldo()
        elif menu == 4:
            beli_tiket()
        elif menu == 5:
            global session
            session = None
            print("Anda logout")
            break
        else:
            print("Input tidak ada di daftar menu! Coba lagi.")

# menu utama
while True:
    print("\nSelamat datang di sistem manajemen tiket konser")
    print("1. Login")
    print("2. Keluar")


    menu = int(input("Masukkan menu (angka menu): "))
    
    if menu == 1:
        akun = login_user()
        if akun:
            session = akun
            if session['role'] == "admin":
                admin()
            elif session["role"] == "user":
                pembeli()
            session = None  # setelah logout dari submenu, pastikan sesi dikosongkan
        else:
            print("Login gagal, silahkan coba lagi.")
    
    elif menu == 2:
        print("Terimakasih dan sampai jumpa ^^")
        break
    
    else:
        print("Menu tidak ada, silahkan coba lagi.")


            
 