import csv
import os
from pathlib import Path
import pandas as pd
import time 
from datetime import datetime, timedelta, date
from  prettytable import  PrettyTable

def loading(text):
    for i in range(7):
        print("\r{0}  {1}".format(text,"."*i),end="")
        time.sleep(0.1)

def menu_regislogin():
    os.system('cls')
    print(35 * "==")
    print("De Laundry".center(70))
    print("1. Admin")
    print("2. Staff")
    pilihan = input("Admin/Staff[1/2] : ")
    if pilihan == "1":
        os.system('cls') 
        loading("Harap Tunggu")
        if not Path('data_adminD.csv').is_file():
            with open('data_adminD.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['username', 'password'], delimiter=',') 
                header.writeheader()
                writer = csv.writer(filecsv)
                writer.writerow(['admin', '123'])
                    
            if not Path('data_pesananD.csv').is_file():
                with open('data_pesananD.csv', 'w', newline='') as filecsv:
                    header = csv.DictWriter(filecsv, fieldnames=['Nama', 'Nomer Hp', 'Berat /Kg', 'Status', 'Total Biaya'], delimiter=',')
                    header.writeheader()

        if not Path('riwayat_transaksi.csv').is_file():
            with open('riwayat_transaksi.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['Nama', 'Nomer Hp', 'Berat /Kg', 'Status', 'Total Biaya'], delimiter=',')
                header.writeheader()

        os.system('cls')            
        print(35 * "==")
        print("Menuju Menu Login")
        print(35 * "\n==")
        loginadminD('data_adminD')
    elif pilihan == "2":
        loginstaff()
    else:
        menu_regislogin()
def loginadminD(data_adminD):
    os.system('cls')
    print("========================================")
    print("Silahkan Login")
    print("========================================")
    username= (input(" Masukkan username = "))
    password= (input(" Masukkan password = "))
    kondisi = False
    data = []
    
    with open('data_adminD.csv', 'r') as file:
        data_adminD = csv.reader(file, delimiter=',')
        for row in data_adminD:
            data.append({'username': row[0],'password': row[1]})
        print(data)

    for row in data:
        if row['username'] == username and row['password'] == password :
            kondisi = True
            break
    if kondisi == True:
        menu_adminD()    
        
    if not kondisi:
        os.system('cls')
        print("========================================")
        print("Kamu Bukan Admint")
        print("========================================")
        loading("Kembali ke menu login")
        loginadminD('data_adminD')
    else:
        os.system('cls')
        print("========================================")
        print("Login Berhasil")
        os.system('cls')
        loading("Selamat Datang Admint")
        os.system('cls')
        menu_adminD()


def menu_adminD():
    os.system('cls')
    print("========================================")
    print("Hallo Admin")
    print("========================================")
    print("1. Info Staff")
    print("2. Transaksi")
    print("3. Keluar") 
    print("========================================")
    
    pilihan = input("Pilih Menu [1/2/3]: ")
    if pilihan == "1":
        inpo_staf()
    if pilihan == "2":
        riwayat_transaksi()
    if pilihan == "3":
        menu_regislogin()
    else :
        loginadminD('data_adminD')

def inpo_staf():
    os.system('cls')
    loading("Harap Tunggu")
    os.system('cls')
    print("Halo Admin, Mau Ngapain nich")
    print("1. Tambah Staf") 
    print("2. Status Staff")#ini buat cek staf lagi ngerjain apa
    print("3. Kembali ke Menu Admin")
    pilihan = input("Pilih Menu [1/2/3/4]: ")
    if pilihan == "1":
        rekrut_staf()
    elif pilihan == "2":
        lihat_staf()
    elif pilihan == "3":
        aktivitas_staf()
    elif pilihan == "4":
        menu_adminD()
    else:
        menu_regislogin()

def rekrut_staf():
    os.system('cls')
    if not(Path('akun_staff.csv').is_file()):
         with open('akun_staff.csv', 'w', newline='') as filecsv:
            header = csv.DictWriter(filecsv, fieldnames=['Username','Password'],  delimiter=',') 
            header.writeheader()
    if not Path('data_staf.csv').is_file():
        with open('data_staf.csv', 'w', newline='') as filecsv:
            header = csv.DictWriter(filecsv, fieldnames=['Nama','Umur','Gender','NoTelp', 'Status' ], delimiter=',')
            header.writeheader()
    try:
        with open('data_staf.csv', 'a', newline='') as file:
            tambah = csv.writer(file, delimiter=',')

            nama = input("masukkan nama: ").strip()
            if not nama:
                print("Nama produk tidak boleh kosong!")
                return
            
            umur_input = input("masukkan umur: ").strip()
            if not umur_input:
                print("umur gaboleh kosong cuy!")
                input("Tekan Enter untuk kembali ke menu.")
                return menu_adminD()
            umur = int(umur_input)
            
            gender = input("Masukkan Jenis Kelamin (L/P): ").strip().upper()
            if not gender:
                print("Jenis kelamin tidak boleh kosong!")
                return
            
            notelp = input("Masukkan Nomor Telepon: ").strip()
            if not notelp:
                print("Nomor telepon tidak boleh kosong!")
                return
            status = "Aktif"

            tambah.writerow([nama, umur, gender, notelp, status])
        
        loading("Menambahkan Data")
        os.system('cls')
        print("Data berhasil ditambahkan!")
        print("Lesgo buat akun staff")
        buat_akun_staf()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        input("Tekan Enter untuk kembali ke menu.")
        menu_adminD()    

import pandas as pd
from prettytable import PrettyTable

def lihat_staf():
    print("\n=== Informasi Staf ===")
    try:
        stafD = pd.read_csv('data_staf.csv')
        if stafD.empty:
            print("Belum ada data staf.")
            return

        # Tampilkan semua data staf dalam tabel rapi
        table = PrettyTable()
        table.field_names = stafD.columns.tolist()
        for _, row in stafD.iterrows():
            table.add_row(row.tolist())
        print(table)

        nama_input = input("\nMasukkan nama staf yang ingin diedit/hapus (tekan Enter untuk kembali): ")
        if nama_input == "":
            return

        if nama_input in stafD['Nama'].values:
            print("\n1. Edit data")
            print("2. Hapus data")
            pilihan = input("Gas pilih min: ")

            index = stafD[stafD['Nama'] == nama_input].index[0]

            if pilihan == "1":
                print("\nData saat ini:")
                print(stafD.loc[index])

                # Edit field satu per satu
                new_nama = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
                umur = input("Masukkan umur baru (kosongkan jika tidak diubah): ")
                gender = input("Masukkan gender baru (kosongkan jika tidak diubah): ")
                notelp = input("Masukkan no telp baru (kosongkan jika tidak diubah): ")
                status = input("Masukkan status baru (A = Aktif, NA = Tidak Aktif, kosongkan jika tidak diubah): ").upper()

                if new_nama:
                    stafD.at[index, 'Nama'] = new_nama
                if umur:
                    stafD.at[index, 'Umur'] = umur
                if gender:
                    stafD.at[index, 'Gender'] = gender
                if notelp:
                    stafD.at[index, 'NoTelp'] = notelp
                if status in ['A', 'NA']:
                    stafD.at[index, 'Status'] = status
                elif status != "":
                    print("Status tidak valid. Gunakan 'A' untuk Aktif atau 'NA' untuk Tidak Aktif.")
                    return

                stafD.to_csv('data_staf.csv', index=False)
                print("Data staf berhasil diperbarui.")

            elif pilihan == "2":
                stafD.at[index, 'Status'] = "Nonaktif"
                stafD.to_csv('data_staf.csv', index=False)
                print("Status staf diubah menjadi Nonaktif.")
            else:
                print("Pilihan tidak valid.")
        else:
            print("Nama staf tidak ditemukan.")

    except FileNotFoundError:
        print("File data_staf.csv tidak ditemukan. Tambahkan staf terlebih dahulu.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def aktivitas_staf():
    print("\n=== Utus Staf untuk Mengurus Pesanan ===")
    try:
        df = pd.read_csv('data_pesananD.csv')

        df_display = df.copy()
        df_display.index = df_display.index + 1
        print(df_display[['Nama', 'Nomer Hp', 'Berat /Kg', 'Status', 'Total Biaya', 'Nama Staf']])

        try:
            nomor = int(input("\nMasukkan nomor pesanan yang akan diurus staf: "))
            if nomor < 1 or nomor > len(df):
                print("Nomor pesanan tidak valid.")
                return

            index = nomor - 1

            if df.loc[index, 'Status'].lower() != "menunggu":
                print("Pesanan ini sudah sedang/selesai diproses.")
                return

            nama_staf = input("Masukkan nama staf yang ditugaskan: ")

            df.at[index, 'Nama Staf'] = nama_staf
            df.at[index, 'Status'] = "Proses"
            df.to_csv('data_pesananD.csv', index=False)
            print(f"Staf '{nama_staf}' berhasil diutus untuk pesanan nomor {nomor}.")
        except ValueError:
            print("Masukkan angka yang valid untuk nomor pesanan.")
    except FileNotFoundError:
        print("File data_pesananD.csv tidak ditemukan.")

def menu_staf():
    os.system('cls')
    print("========================================")
    print("Hallo Staff")
    print("========================================")
    print("1. Cek data pesanan")
    print("2. Info Pesanan")
    print("3. Riwayat Transaksi") 
    print("4. Keluar")
    print("========================================")
    
    pilihan = input("Pilih Menu [1/2/3]: ")
    if pilihan == "1":
        data_pesanan()
    if pilihan == "2":
        info_pesanan()
    if pilihan == "3":
        riwayat_transaksi()
    if pilihan == "4":
        menu_regislogin()
    else :
        menu_staf()

def data_pesanan():
    print("\n=== Input Data Pesanan ===")
    try:
        nama = input("Masukkan nama pelanggan: ")
        nohp = input("Masukkan nomer HP: ")
        berat = float(input("Masukkan berat cucian (kg): "))

        harga_per_kg = 5000
        total_biaya = int(berat * harga_per_kg)
        status = "Menunggu"

        with open('data_pesananD.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nama", "Nomer Hp", "Berat /Kg", "Status", "Total Biaya", "Nama Staf"])
            writer.writerow([nama, nohp, berat, status, total_biaya, ""])
            print("✅ Pesanan berhasil dicatat.")

    except ValueError:
        print("❌ Input berat harus berupa angka.")

def buat_akun_pelanggan():
    os.system('cls')
    loading("Masuk ke menu Registrasi")
    os.system('cls')

    data = []
    with open('akun_pelanggan.csv', 'r') as file:
        csv_user = csv.reader(file, delimiter=',')
        for row in csv_user:
            data.append({'username': row[0]})  

    print("Contoh username = nyunyes@Dlaundry")
    username= (input("Masukkan username = "))
    for row in data:
        if row['username'] == username:
            os.system('cls')
            print("========================================")
            print("Username sudah terdaftar")
            print("Silahkan registrasi dengan username lain")
            print("\n========================================")
            input("Tekan Enter untuk kembali...")
            return buat_akun_staf()
        
    password= (input("Masukkan password = "))
    with open('akun_pelanggan.csv', 'a', newline='') as file:
        csv_user = csv.writer(file, delimiter=',')
        csv_user.writerow([username,password])

    print("========================================")
    loading("Registrasi Berhasil")
    os.system('cls')
    loading("Masuk ke menu admin")

    username= (input("Masukkan username = "))
    password= (input("Masukkan password = "))
    
    with open('akun_pelanggan.csv', 'a', newline='') as file:
        csv_user = csv.writer(file, delimiter=',')
        csv_user.writerow([username,password])

    print("========================================")
    loading("Registrasi Berhasil")
    os.system('cls')
    menu_staf()


def loginpelanggan():
    os.system('cls')
    print("========================================")
    print("Silahkan Login")
    print("========================================")
    username= (input(" Masukkan username = "))
    password= (input(" Masukkan password = "))
    kondisi = False
    data = []
    
    with open('akun_pelanggan.csv', 'r') as file:
        data_pelanggan = csv.reader(file, delimiter=',')
        for row in data_pelanggan:
            data.append({'username': row[0],'password': row[1]})
        print(data)

    for row in data:
        if row['username'] == username and row['password'] == password :
            kondisi = True
            break
    if kondisi == True:
        menu_pelanggan()    
        

def menu_pelanggan():
    os.system('cls')
    print("========================================")
    print("Hallo Pelanggan")
    print("========================================")
    print("1. Cek status pesanan")
    print("2. Metode pembayaran")
    if not kondisi:
        os.system('cls')
        print("========================================")
        print("Kamu Bukan Pelanggan")
        print("========================================")
        loading("Kembali ke menu login")
        loginpelanggan()

def loginstaff():
    os.system('cls')
    print("========================================")
    print("Silahkan Login")
    print("========================================")
    username= (input(" Masukkan username = "))
    password= (input(" Masukkan password = "))
    kondisi = False
    data = []
    
    with open('akun_staff.csv', 'r') as file:
        data_staff = csv.reader(file, delimiter=',')
        for row in data_staff:
            data.append({'username': row[0],'password': row[1]})

    for row in data:
        if row['username'] == username and row['password'] == password :
            kondisi = True
            break
    if kondisi == True:
        os.system('cls')
        loading("Selamat Datang Staff")
        menu_staf()

def data_pesanan():
    print("\n=== Input Data Pesanan ===")
    try:
        username = input("Masukkan username pelanggan: ")
        nama = input("Masukkan nama pelanggan: ")
        nohp = input("Masukkan nomer HP: ")
        berat = float(input("Masukkan berat cucian (kg): "))
        metodecucian = input("Masukkan metode cucian (Reguler/Express): ").strip().lower()

        if metodecucian == "reguler":
            harga_per_kg = 5000
            estimasi_hari = 3
        elif metodecucian == "express":
            harga_per_kg = 10000
            estimasi_hari = 1
        else:
            print("❌ Metode cucian tidak valid. Harus Reguler atau Express.")
            return

        total_biaya = int(berat * harga_per_kg)

        print("Pilih metode pembayaran:")
        print("1. Tunai")
        print("2. Transfer")
        metode_input = input("Masukkan pilihan (1/2): ")

        if metode_input == "1":
            metode_pembayaran = "Tunai"
        elif metode_input == "2":
            metode_pembayaran = "Transfer"
        else:
            print("❌ Pilihan tidak valid. Gunakan 1 untuk Tunai atau 2 untuk Transfer.")
            return

        status = "Dijemput"
        waktu_sekarang = datetime.now()
        tanggal_pesanan = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")
        tanggal_estimasi = (waktu_sekarang + timedelta(days=estimasi_hari)).strftime("%Y-%m-%d %H:%M:%S")

        file_exists = os.path.exists('data_pesananD.csv')

        with open('data_pesananD.csv', 'a', newline='') as file:
            fieldnames = [
                "Username", "Nama", "Nomer Hp", "Berat /Kg", "Metode cucian",
                "Status", "Total Biaya", "Metode Pembayaran",
                "Tanggal pesanan dibuat", "Tanggal estimasi selesai"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "Username": username,
                "Nama": nama,
                "Nomer Hp": nohp,
                "Berat /Kg": berat,
                "Metode cucian": metodecucian.capitalize(),
                "Status": status,
                "Total Biaya": total_biaya,
                "Metode Pembayaran": metode_pembayaran,
                "Tanggal pesanan dibuat": tanggal_pesanan,
                "Tanggal estimasi selesai": tanggal_estimasi
            })

        print("✅ Pesanan berhasil dicatat.")
        print(f"🗓 Estimasi selesai: {tanggal_estimasi}")

    except ValueError:
        print("❌ Input berat harus berupa angka.")

if __name__ == "__main__":
    menu_regislogin()