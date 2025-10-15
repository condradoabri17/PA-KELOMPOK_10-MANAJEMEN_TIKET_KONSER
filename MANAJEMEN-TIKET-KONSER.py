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
    print("Daftar Tiket Konser yang tersedia")

    with open("tiket.json", "r") as r:
        isi_data = r.read().strip()
        if not isi_data:
            print("Data Tiket yang tersedia belum ada. silahkan tambah atau buat!!")
            return
        data = json.loads(isi_data)

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

        
def admin(): 
    while True: 
        print("\nSelamat datang admin di sistem manajemen tiket konser\nSilahkan pilih menu dibawah ini:") 
        print("1. Lihat tiket konser") 
        print("2. Tambah tiket konser") 
        print("3. Update tiket konser") 
        print("4. Delete tiket konser") 
        print("5. logout") 
        
        try: 
            menu = int(input("Masukkan pilihan (wajib angka pilihan): ").strip()) 
            if menu == 1: 
                read_tiket() 
            elif menu == 2: 
                create_tiket() 
            elif menu == 3:
                update_tiket() 
            elif menu == 4: 
                delete_tiket()
            elif menu == 5: 
                print("anda logout") 
                break 
            else: 
                print("input tidak ada di daftar menu! coba lagi")
        except ValueError: 
            print("Inputan harus angka!")

def pembeli():
    while True:
        print("\nSilahkan pilih menu dibawah ini:")
        print("1. Lihat Tiket Yang dijual")
        print("2. Cek Saldo")
        print("3. Beli tiket konser")
        print("4. logout")
        print("5. logout")

        try:
            pilihan = input(int("Masukkan pilihan (wajib angka pilihan): "))
            if pilihan == 1:
                print("menu lihat tiket")
            elif pilihan == 2:
                print("menu Tambah tiket")
            elif pilihan == 3:
                print("menu update tiket")
            elif pilihan == 4:
                print("menu hapus tiket")
            elif pilihan == 5:
                print("anda logout")
                break
            else:
                print("input tidak ada di daftar menu! coba lagi")
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


    

            
            
            
