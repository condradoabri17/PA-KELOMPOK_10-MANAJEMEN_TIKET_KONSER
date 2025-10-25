# Sistem Manajemen Tiket Konser

Program ini adalah sistem manajemen tiket konser yang dibuat dengan bahasa pemrograman Python.  

Terdapat dua role pengguna yaitu **Admin** dan **User (pembeli tiket)**.  
Admin dapat menambah, melihat, mengedit, dan menghapus tiket konser, sedangkan user bisa membeli tiket secara online maupun offline, mengisi saldo, dan mengecek saldo mereka.
## Akun

### Role Admin

- Melihat daftar tiket konser
    
- Menambahkan tiket baru (tanggal, harga, dan stok)
    
- Mengedit data tiket
    
- Menghapus tiket
    
- Logout
    
### Role Pembeli

- Melihat tiket konser yang tersedia
    
- Mengecek saldo
    
- Mengisi saldo (maksimal 25 juta)
    
- Membeli tiket secara online atau offline
    
- Logout
    
## Persiapan Awal
    
1. Instal library yang dibutuhkan, yaitu pw input dan prettytable:
    
    ```bash
    pip install prettytable 
    pip install pwinput
    ```

2. Buat file json untuk awal yaitu untuk akun (akun.json) dan tiket (tiket.json):

**akun.json:**
```json
[

    {

            "username": "gina26",

            "password": "123",

            "role": "user",

            "saldo": 0

        },

        {

            "username": "admin26",

            "password": "admin123",

            "role": "admin",

            "saldo": 0

    }

]
```

**tiket.json:**
```json
[

    {

        "id_tiket": "T002",

        "nama_konser": "Konser tutup tahun",

        "tanggal": "31-12-2025",

        "lokasi": "Stadion Segiri",

        "kategori": "Reguler",

        "harga": 150000,

        "stok": 38,

        "terjual": 12

    }

]
```

3. Buat file python dengan nama `MANAJEMEN-TIKET-KONSER.py` Pastikan file python dan json berada dalam folder yang sama:

    ```
    MANAJEMEN-TIKET-KONSER.py
    akun.json
    tiket.json
    ```
    
    Kalau kita misal memindahkan file ke folder lain, pastikan kita menjalankan program dari folder baru itu itu.  
## Cara Menjalankan Program

1. Buka kode editor (misalnya visual studio code).
    
2. Masuk ke folder tempat file program berada.
    
3. masuk ke file python dan *run* programnya:

4. Di menu utama, pilih:
    
    - `1` untuk **Login**
        
    - `2` untuk **Keluar**

5. Jika memilih Login maka akan diarahkan di menu konfirmasi dengan konfirmasi "Sudah punya akun? (Y/N)"
6. Jika memilih 2 maka program akan berhenti
### Tutorial Login

- Jika belum punya akun, masukkan **N** saat ditanya “Sudah punya akun? (Y/N)” untuk membuat akun baru.

- Namun jika sudah punya akun maka masukkan **Y**
    
- Akun baru yang dibuat otomatis berperan sebagai **User**.
    
- Jika kita ingin login sebagai **Admin**, buat akun secara manual di `akun.json` seperti ini:


```json
[
  {
    "username": "admin",
    "password": "admin123",
    "role": "admin",
    "saldo": 0
  }
]
```

- Setelah login, program akan mengecek jika login dengan akun yang memiliki role "admin", maka akan masuk ke menu admin, jika login dengan akun yang memiliki role "user" maka akan masuk ke menu pembeli
  
  **Tampilan Menu Admin:**
![](asset/gambar(1).jpg)

**Tampilan Menu Pembeli (User):**
![](asset/gambar(2).jpg)
### Cara kerja dan cara menjalankan fitur

#### Lihat daftar tiket (admin dan user)

- Untuk menjalankan fitur ini pilih menu nomor `1` dan menu ini bisa diakses jika login sebagai admin maupun user.
    
- Jika belum ada data tiket, sistem akan menampilkan pesan  
    `"Belum ada tiket yang tersedia."`.
    
- Data yang ada ditampilkan dalam bentuk tabel menggunakan `PrettyTable`.
    
- Tampilan tabel akan berbeda tergantung role pengguna (user atau admin):
    
    - **User:** hanya melihat kolom penting seperti `ID Tiket`, `Nama Konser`, `Tanggal`, `Lokasi`, `Kategori`, `Harga`, dan `Stok`.
        
    - **Admin:** mendapat tampilan lengkap termasuk kolom `Terjual` untuk melihat  penjualan tiket.
#### Tambah Tiket (Admin)

- Untuk mengakses fitur ini ada di menu nomor `2` namun hanya bisa diakses jika login sebagai admin

- Format tanggal yang digunakan adalah `dd-mm-yyyy`
    
- Tanggal tidak boleh sesudah hari ini (tanggal lebih lama dari hari ini)
    
- Harga maksimal: **20.000.000**
    
- Stok maksimal: **100.000**
    
- Kategori hanya bisa “VIP” atau “Reguler”
    
#### Update Tiket (Admin)

- Diakses jika memilih menu nomor `3` saat login sebagai admin

- Bisa ubah hanya sebagian data tiket (tinggal tekan Enter atau kosong jika tidak mau ubah data tertentu)
    
- Untuk aturan tiap data sama seperti tambah tiket (format tanggal, harga maksimal, stok maksima, dan kategori)

#### **Delete Tiket**

- Untuk mengakses fitur ini, masukkan menu `4` dan hanya saat login sebagai admin

- Program menampilkan semua data tiket dengan memanggil function `read_tiket()`.
    
-  Kita diminta memasukkan `ID Tiket` yang ingin dihapus.
    
-  Program memeriksa apakah ID tersebut ada dalam data.
    
-  Jika tiket ditemukan, sistem menampilkan data tiket yang akan dihapus dan meminta konfirmasi dengan menjawab `Y/N`.
    
-  Jika dikonfirmasi untuk dihapus maka tiket dihapus dari daftar tiket
    
-  Jika tiket tidak ditemukan, sistem akan meminta ulang input hingga ID_Tiket yang ada di database ditemukan.

#### Lihat Saldo (User)

- Fitur bisa diakses jika memilih menu nomor `2` saat login sebagai user
    
-  Saldo ditampilkan dalam format rupiah (`Rp` dengan tanda ada tambahan koma untuk ribuan).
#### Isi Saldo (User)

-  Fitur bisa diakses jika memilih menu `3` saat login sebagai user

- Minimal > 0
    
- Maksimal **25.000.000** per isi saldo
    
#### Beli Tiket

- Fitur diakses jika memilih menu `4` saat login sebagai user

- User bisa memilih pembayaran secara **online** atau **offline**
    
- Maksimal pembelian adalah 10 tiket per transaksi
    
- Sistem akan otomatis mengurangi stok dan menambah jumlah terjual
    
- Jika online, saldo akan otomatis terpotong dan user akan diberikan kode unik yang nantinya akan digunakan sebagai tiket masuk konsernya

- Jika offline, saldo tidak akan terpotong dan user akan diberikan kode unik yang berfungsi sebagai kode pembayaran dilokasi konser agar kemudian user bisa masuk ke konsernya
#### Logout

- Jika ingin logout dan misal ingin login ke akun lain bisa menginput `5` dari di input menu
## Struktur File

```
main_program
│
├── MANAJEMEN-TIKET-KONSER.py
├── akun.json
└── tiket.json
```

## Catatan

- Kalau muncul error `FileNotFoundError: 'akun.json'`, artinya file json-nya tidak terdeteksi. Pastikan kita menjalankan Python dari folder yang sama dengan file json-nya.
    
- Gunakan `Ctrl + C` untuk keluar dari program kapan saja (darurat).
    
## Tujuan Program

Program ini dibuat sebagai syarat kelulusan proyek akhir mata kuliah Dasar-Dasar Pemrograman dan sebagai latihan logika serta pengelolaan database menggunakan JSON dan Python. Latihan ini cocok untuk latihan pembelajaran dasar CRUD dan dasar untuk memahami dasar cara kerja login.
