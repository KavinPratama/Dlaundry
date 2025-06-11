import csv
import os
from pathlib import Path
import pandas as pd
import time
from prettytable import PrettyTable
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def loading(text):
    for i in range(7):
        print("\r{0}  {1}".format(text,"."*i),end="")
        time.sleep(0.1)

#================================================= INI BUAT LOGIN =============================================

def menu_regislogin():
    os.system('cls')
    print(35 * "==")
    print("De Laundry".center(70))
    print("1. Admin")
    print("2. Staff")
    print("3. Pelanggan")
    pilihan = input("Admin/Staff[1/2/3] : ")
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
                    header = csv.DictWriter(filecsv, fieldnames=['username', 'Nama', 'No Hp', 'Berat /Kg', 'Metode cuci', 'Total', 'Metode Pembayaran', 'Pesanan Dibuat', 'Estimasi Selesai', 'Status', 'Ditugaskan ke'], delimiter=',')
                    header.writeheader()

        os.system('cls')            
        print(35 * "==")
        print("Menuju Menu Login")
        print(35 * "\n==")
        loginadminD('data_adminD')
    elif pilihan == "2":
        loginstaff()
    elif pilihan == "3":
        if not Path('akun_pelanggan.csv').is_file():
            with open('akun_pelanggan.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['username', 'password'], delimiter=',') 
                header.writeheader()
                writer = csv.writer(filecsv)
        loginpelanggan()
    else:
        menu_regislogin()

#=============================================== HALAMAN PUNYA ADMIND ===================================================

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
    elif pilihan == "2":
        forstaff_cek_riwayat()
    elif pilihan == "3":
        menu_regislogin()
    else :
        menu_adminD()

def inpo_staf():
    os.system('cls')
    loading("Harap Tunggu")
    os.system('cls')
    print("Halo Admin, Mau Ngapain nich")
    print("1. Tambah Staf") 
    print("2. Status Staff")
    print("3. Tugaskan Staff")
    print("4. Urutan Pesanan Per-Staff")
    print("5. Kembali ke Menu Admin")
    pilihan = input("Pilih Menu [1/2/3/4/5]: ")
    if pilihan == "1":
        rekrut_staf()
    elif pilihan == "2":
        lihat_staf()
    elif pilihan == "3":
        aktivitas_staf()    
    elif pilihan == "4":
        urutan_pesanan_perstaf()
    elif pilihan == "5":
        menu_adminD()
    else:
        menu_adminD()

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
                print("Nama tidak boleh kosong!")
                return rekrut_staf()
            
            umur_input = input("Masukkan umur berupa 2 digit angka: ").strip()

            if not umur_input or not umur_input.isdigit():
                print("Umur gaboleh kosong cuy dan harus berupa 2 digit angka!")
                input("Tekan Enter untuk kembali ke menu.")
                return rekrut_staf()

            umur = int(umur_input)

            if len(umur_input) != 2:
                print("Umur harus berupa 2 digit angka!")
                input("Tekan Enter untuk kembali ke menu.")
                return rekrut_staf()
            if umur < 17:
                print("Masih kecil dek, sekolah dulu sana.")
                input("Tekan Enter untuk kembali ke menu.")
                return rekrut_staf()
            elif umur > 70:
                print("Udah waktunya pensiun.")
                input("Tekan Enter untuk kembali ke menu.")
                return rekrut_staf()

            print(f"Umur diterima: {umur}")

            
            gender = input("Masukkan Jenis Kelamin (L/P): ").strip().upper()
            if gender not in ['L', 'P']:
                print("Jenis kelamin harus 'L' atau 'P' saja ya")
                input("Tekan Enter untuk kembali ke menu.")
                return rekrut_staf()
            
            notelp = input("Masukkan Nomor Telepon: ").strip()
            if notelp.isdigit() and 12 <= len(notelp) <= 13:
                print("Nomor telepon harus angka dan maksimal 13 digit")
                input("Tekan Enter untuk kembali ke menu")
                return menu_adminD()
            
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

def lihat_staf():
    print("\n=== Informasi Staf ===")
    try:
        stafD = pd.read_csv('data_staf.csv', dtype={"NoTelp": str}) #buat maksa biar notelp jd str, klo pake int nnti 0 didepan itu hilang
        if stafD.empty:
            print("Belum ada data staf.")
            return
        print(stafD)

        nama = input("\nMasukkan nama staf yang ingin diedit/hapus (tekan Enter untuk kembali): ")
        if nama == "":
            loading("Kembali ke lihat staf...")
            return inpo_staf()
        
        nama = nama.strip().lower()
        stafD['Nama'] = stafD['Nama'].str.strip().str.lower()

        if nama in stafD['Nama'].values:
            print("\n1. Edit data")
            print("2. Hapus data")
            pilihan = input("Gas pilih min (1/2): ")

            index = stafD[stafD['Nama'] == nama].index[0]

            if pilihan == "1":
                print("\nData saat ini:")
                tabel = PrettyTable()
                tabel.field_names = ["Nama", "Umur", "Gender", "NoTelp", "Status"]

                row = stafD.loc[index]
                tabel.add_row([
                    row["Nama"], row["Umur"], row["Gender"],
                    row["NoTelp"], row["Status"]
                ])
                print(tabel)

                umur = input("Masukkan umur baru (kosongkan jika tidak diubah): ")
                gender = input("Masukkan gender baru (kosongkan jika tidak diubah): ")
                notelp = input("Masukkan no telp baru (kosongkan jika tidak diubah): ")
                status = input("Masukkan status baru (A = Aktif, NA = Tidak Aktif, kosongkan jika tidak diubah): ")

                if umur:
                    stafD.at[index, 'Umur'] = int(umur)
                if gender:
                    stafD.at[index, 'Gender'] = gender
                if notelp:
                    stafD.at[index, 'NoTelp'] = str(notelp)
                if status:
                    stafD.at[index, 'Status'] = status

                stafD['Nama'] = stafD['Nama'].str.title()
                stafD.to_csv('data_staf.csv', index=False)
                print("Data staf berhasil diperbarui.")
                input("\nTekan Enter untuk kembali ke menu...")
                inpo_staf()

            elif pilihan == "2":
                stafD.at[index, 'Status'] = "Nonaktif"
                stafD['Nama'] = stafD['Nama'].str.title()
                stafD.to_csv('data_staf.csv', index=False)
                print("Status staf diubah menjadi Nonaktif.")
                input("\nTekan Enter untuk kembali ke menu...")
                inpo_staf()  
            else:
                print("Pilihan tidak valid.")
                input("\nTekan Enter untuk kembali ke menu...")
                inpo_staf
        else:
            print("Nama staf tidak ditemukan.")
            input("\nTekan Enter untuk kembali ke menu...")
            inpo_staf

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        input("\nTekan Enter untuk kembali ke menu...")

    except FileNotFoundError:
        print("File data_staf.csv tidak ditemukan. Tambahkan staf terlebih dahulu.")
        input("\nTekan Enter untuk kembali ke menu...")

def buat_akun_staf():
    os.system('cls')
    loading("Masuk ke menu Registrasi.")
    os.system('cls')

    data = []
    with open('akun_staff.csv', 'r') as file:
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
    with open('akun_staff.csv', 'a', newline='') as file:
        csv_user = csv.writer(file, delimiter=',')
        csv_user.writerow([username,password])

    print("========================================")
    loading("Registrasi Berhasil")
    os.system('cls')
    loading("Kembali ke menu admin")
    menu_adminD()
        
def aktivitas_staf():
    print("\n=== Utus Staf untuk Mengurus Pesanan ===")
    try:
        df = pd.read_csv('data_pesananD.csv')

        df_display = df[df['Status'].str.lower() == 'diterima'].copy()
        df_display['indexasli'] = df_display.index
        df_display.index = range(1, len(df_display) + 1)

        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama", "No Hp", "Berat /Kg", "Metode cucian", "Total", "Metode Pembayaran", "Ditugaskan ke", "Pesanan Dibuat", "Estimasi Selesai", "Status"]

        for i, row in df_display.iterrows():
            tabel.add_row([
                i,
                row['Nama'], row['No Hp'], row['Berat /Kg'], row['Metode cucian'], row['Total'],
                row['Metode Pembayaran'], row['Ditugaskan ke'], row['Pesanan Dibuat'],
                row['Estimasi Selesai'], row['Status']
            ])
        print(tabel)

        try:
            nomor = int(input("\nMasukkan nomor pesanan yang akan diurus staf: "))
            if nomor < 1 or nomor > len(df_display):
                print("Nomor pesanan tidak valid.")
                aktivitas_staf()
                return


            index_asli = df_display.loc[nomor, 'indexasli']
            if df.loc[index_asli, 'Status'].lower() != "diterima":
                print("Pesanan ini sudah sedang/selesai diproses.")
                aktivitas_staf()
                return

            if not os.path.exists('data_staf.csv'):
                print("File data_staf.csv tidak ditemukan.")
                aktivitas_staf()
                return

            df_staf = pd.read_csv('data_staf.csv')
            df_staf_aktif = df_staf[df_staf['Status'].str.lower() == 'aktif']

            daftar_staf = []
            for nama in df_staf_aktif['Nama']:
                if isinstance(nama, str) and nama.strip() != "":
                    daftar_staf.append(nama)

            if not daftar_staf:
                print("Tidak ada staf yang tersedia.")
                return

            pesanan_per_staf = {nama: 0 for nama in daftar_staf}
            for i, row in df.iterrows():
                staf = row.get("Ditugaskan ke", "").strip()
                status = row.get("Status", "").strip().lower()
                if staf in pesanan_per_staf and status != "selesai":
                    pesanan_per_staf[staf] += 1

            print("\nJumlah pesanan aktif per staf:")
            for i, staf in enumerate(daftar_staf, 1):
                jumlah = pesanan_per_staf[staf]
                print(f"{i}. {staf} : {jumlah} pesanan")

            try:
                nomor_staf = int(input("\nMasukkan nomor staf yang akan ditugaskan: "))
                if nomor_staf < 1 or nomor_staf > len(daftar_staf):
                    print("Nomor staf tidak valid.")
                    return
                staf_terpilih = daftar_staf[nomor_staf - 1]
            except ValueError:
                print("Masukkan angka yang valid.")
                return

            df.at[index_asli, 'Ditugaskan ke'] = staf_terpilih
            df.at[index_asli, 'Status'] = "Diproses"
            df.to_csv('data_pesananD.csv', index=False)
            print(f"\nStaf '{staf_terpilih}' berhasil diutus untuk pesanan nomor {nomor}.")
            input("Tekan Enter untuk kembali ke menu")
            menu_adminD()

        except ValueError:
            print("Masukkan angka yang valid untuk nomor pesanan.")
            menu_adminD()
    except FileNotFoundError:
        print("File data_pesananD.csv tidak ditemukan.")
        menu_adminD()

def urutan_pesanan_perstaf():
    filename = "data_pesananD.csv"
    if not os.path.exists(filename):
        print("File data pesanan tidak ditemukan.")
        return

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data_pesanan = list(reader)

    data_pesanan_aktif = [
        d for d in data_pesanan
        if d["Status"].lower() != "selesai" and d["Ditugaskan ke"].strip() != "-"
    ]

    if not data_pesanan_aktif:
        print("Tidak ada pesanan aktif.")
        return

    daftar_staf = sorted(set(d["Ditugaskan ke"] for d in data_pesanan_aktif))

    print("\nLihat Urutan Pesanan Berdasarkan Staf:")
    for i, staf in enumerate(daftar_staf, start=1):
        print(f"{i}. {staf}")
    print("0. Kembali")

    try:
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 0:
            return
        elif 1 <= pilihan <= len(daftar_staf):
            nama_staf = daftar_staf[pilihan - 1]
            pesanan_staf = [
                d for d in data_pesanan_aktif if d["Ditugaskan ke"].lower() == nama_staf.lower()
            ]

            def sort_key(x):
                berat = float(x["Berat /Kg"])
                sesi_mesin = int(berat // 5) + (1 if berat % 5 else 0)

                return (
                    datetime.strptime(x["Pesanan Dibuat"], "%Y-%m-%d"),
                    0 if x["Metode cucian"].lower() == "express" else 1,
                    berat,
                    sesi_mesin
                )

            pesanan_staf.sort(key=sort_key)

            print(f"\nUrutan Pesanan Greedy untuk Staf '{nama_staf}':")
            tabel = PrettyTable()
            tabel.field_names = [
                "Nama", "No Hp", "Berat /Kg", "Sesi Mesin", "Metode", "Total",
                "Dibuat", "Selesai", "Status"]

            for d in pesanan_staf:
                berat = float(d["Berat /Kg"])
                sesi_mesin = int(berat // 5) + (1 if berat % 5 else 0)

                tabel.add_row([
                    d["Nama"], d["No Hp"], berat, sesi_mesin,
                    d["Metode cucian"], d["Total"],
                    d["Pesanan Dibuat"], d["Estimasi Selesai"], d["Status"]
                ])
            print(tabel)
            input("Tekan enter untuk kembali ke halaman sebelumnya")
            urutan_pesanan_perstaf()
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

def jump_search(data, target, keyf):
    panjang = len(data)

    step = 1
    while step * step < panjang:
        step += 1

    i = 0
    while i < panjang:
        if keyf(data[i]) >= target:
            break
        i += step

    j = i - step
    if j < 0:
        j = 0
    while j < panjang and j <= i:
        if keyf(data[j]) == target:
            return j
        j += 1

    return -1

def quick_sort(data, key):
    if len(data) <= 1:
        return data
    pivot = key(data[0])
    kiri = [item for item in data[1:] if key(item) <= pivot]
    kanan = [item for item in data[1:] if key(item) > pivot]
    return quick_sort(kiri, key) + [data[0]] + quick_sort(kanan, key)

def ambil_berat(row):
    return float(row['Berat /Kg'])

def ambil_bulan(row):
    return datetime.strptime(row['Pesanan Dibuat'], "%Y-%m-%d").month

def ambil_total(row):
    return float(row['Total'])

def forstaff_cek_riwayat():
    os.system('cls')
    print("=========================================")
    print("          Riwayat Pesanan Selesai        ")
    print("=========================================")
    print("1. Urut berdasarkan BERAT (ringan ke berat)")
    print("2. Urut berdasarkan BULAN (Jan - Des)")
    print("3. Urut berdasarkan TOTAL BIAYA (murah ke mahal)")
    print("4. Cari berdasarkan USERNAME)")
    print("5. Kembali ke Menu Admin")

    pilihan = input("Pilih metode pengurutan [1/2/3/4/5]: ")

    try:
        with open('data_pesananD.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            hasil = [
                row for row in reader 
                if row['Status'].lower() == 'selesai'
            ]

        if not hasil:
            print("Belum ada riwayat pesanan selesai.")
            input("Tekan Enter untuk kembali...")
            return

        if pilihan == "1":
            hasil = quick_sort(hasil, ambil_berat)
        elif pilihan == "2":
            hasil = quick_sort(hasil, ambil_bulan)
        elif pilihan == "3":
            hasil = quick_sort (hasil,ambil_total)
        elif pilihan == "4":
            nama_dicari = input("Masukkan nama pelanggan yang ingin dicari: ").strip().lower()
            hasil_sort = quick_sort(hasil, lambda x: x["Nama"].lower())
            index = jump_search(hasil_sort, nama_dicari, lambda x: x["Nama"].lower())
            if index != -1:
                row = hasil_sort[index]
                print("\nPesanan ditemukan:")
                tabel = PrettyTable()
                tabel.field_names = ["Nama", "No Telp", "Berat /Kg", "Metode", "Total", "Pembayaran", "Dibuat", "Selesai", "Status", "Ditugaskan ke"]
                tabel.add_row([
                    row["Nama"], row["No Hp"], row["Berat /Kg"], row["Metode cucian"], row["Total"],
                    row["Metode Pembayaran"], row["Pesanan Dibuat"], row["Estimasi Selesai"],
                    row["Status"], row["Ditugaskan ke"]
                ])
                print(tabel)
                input("Tekan Enter untuk kembali...")
                return
            else:
                print(f"Tidak ditemukan riwayat dengan nama '{nama_dicari}'.")
                input("Tekan Enter untuk kembali...")
                return 
        elif pilihan == "5":
            menu_adminD()
        else:
            print("Pilihan tidak valid.")
            return

        tabel = PrettyTable()
        tabel.field_names = [
            "Nama", "No Telp", "Berat /Kg", "Metode", "Total",
            "Pembayaran", "Dibuat", "Selesai", "Status", "Ditugaskan ke"
        ]

        for row in hasil:
            tabel.add_row([
                row["Nama"], row["No Hp"], row["Berat /Kg"], row["Metode cucian"],
                row["Total"], row["Metode Pembayaran"], row["Pesanan Dibuat"],
                row["Estimasi Selesai"], row["Status"], row["Ditugaskan ke"]
            ])

        print(tabel)

    except FileNotFoundError:
        print("File data_pesananD.csv tidak ditemukan.")

    input("Tekan Enter untuk kembali ke menu...")
    forstaff_cek_riwayat()

#================================================ HALAMAN PUNYA STAFF ==================================================

def loginstaff():
    os.system('cls')
    print("========================================")
    print("Halo Staff, Silahkan Login")
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
        menu_staf()
    elif kondisi == False:
        os.system('cls')
        print("========================================")
        print("Kamu Bukan Staff")
        print("========================================")
        loading("Kembali ke menu login")
        loginstaff()
    else:
        menu_regislogin()


def menu_staf():
    os.system('cls')
    loading("Harap Tunggu")
    os.system('cls')
    print("========================================")
    print("Hallo Staff")
    print("========================================")
    print("1. Buat akun pelanggan")
    print("2. Buat data pesanan")
    print("3. Update data status") 
    print("4. Keluar")
    print("========================================")
    
    pilihan = input("Pilih Menu [1/2/3/4]: ")
    if pilihan == "1":
        buat_akun_pelanggan()
    elif pilihan == "2":
        data_pesanan()
    elif pilihan == "3":
        update_status_pesanan()
    elif pilihan == "4":        
        menu_regislogin()
    else :
        menu_staf()

def buat_akun_pelanggan():
    os.system('cls')
    loading("Masuk ke menu Registrasi")
    os.system('cls')

    if not os.path.exists('akun_pelanggan.csv'):
        with open('akun_pelanggan.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password']) 

    data = []
    with open('akun_pelanggan.csv', 'r') as file:
        csv_user = csv.reader(file, delimiter=',')
        for row in csv_user:
            if row:
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
    menu_staf()

def data_pesanan():
    print("\n=== Input Data Pesanan ===")
    try:
        username = input("Masukkan username pelanggan: ")
    
        akun_terdaftar = False
        if os.path.exists('akun_pelanggan.csv'):
            with open('akun_pelanggan.csv', 'r') as file_pelanggan:
                reader = csv.DictReader(file_pelanggan)
                for row in reader:
                    if row['username'].strip().lower() == username.strip().lower():
                        akun_terdaftar = True
                        break
        if not akun_terdaftar:
            print("Maaf, username tersebut belum terdaftar sebagai pelanggan.")
            print("Kamu akan diarahkan ke halaman Registrasi untuk mendaftarkan pelanggan...")
            time.sleep(3) 
            buat_akun_pelanggan()

        nama = input("Masukkan nama pelanggan: ")
        while True:
            nohp = input("Masukkan nomer HP: ").strip()
            if nohp.isdigit() and 12 <= len(nohp) <= 13:
                break
            else:
                print("Nomor HP harus berupa angka. Max 13")
        while True:
            try:
                berat = float(input("Masukkan berat cucian (kg, contoh: 45.5): ").strip())
                if berat > 0 and int(berat) < 100:
                    break
                else:
                    print("Berat cucian harus lebih dari 0 dan maksimal 2 digit sebelum koma (misal 99.99).")
            except ValueError:
                print("Masukkan berat cucian berupa angka.")

        metodecucian = input("Masukkan metode cucian (Reguler/Express): ").strip().lower()

        if metodecucian == "reguler":
            harga_per_kg = 5000
            estimasi_hari = 3
        elif metodecucian == "express":
            harga_per_kg = 10000
            estimasi_hari = 1
        else:
            print("Metode cucian tidak valid.")
            return

        staff_terpilih = "-"
        print("Penugasan akan ditentukan oleh admin")
        filename = 'data_pesananD.csv'

#=========================== bayar bayar ===========================
        total_biaya = int(berat * harga_per_kg)

        print("Pilih metode pembayaran:")
        print("1. Tunai")
        print("2. Transfer")
        metode_input = input("Masukkan pilihan (1/2): ").strip()

        if metode_input == "1":
            metode_pembayaran = "Tunai"
        elif metode_input == "2":
            metode_pembayaran = "Transfer"
            img = mpimg.imread('tober.png')
            plt.imshow(img)
            plt.axis('off')  # Hilangkan axis (garis x/y)
            plt.title("Silakan Transfer ke Rekening Berikut")  # Opsional: Judul gambar
            plt.show()
        else:
            print("Pilihan tidak valid.")
            return

        Status = "Diproses"
        waktu_sekarang = datetime.now()
        tanggal_pesanan = waktu_sekarang.strftime("%Y-%m-%d")
        tanggal_estimasi = (waktu_sekarang + timedelta(days=estimasi_hari)).strftime("%Y-%m-%d")

# ===================== data disimpen =====================
        file_exists = os.path.exists(filename)

        with open(filename, 'a', newline='') as file:
            fieldnames = [
                "username", "Nama", "No Hp", "Berat /Kg", "Metode cucian", "Total", "Metode Pembayaran",
                "Pesanan Dibuat", "Estimasi Selesai",
                "Ditugaskan ke", "Status"
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "username": username,
                "Nama": nama,
                "No Hp": nohp,
                "Berat /Kg": berat,
                "Metode cucian": metodecucian.capitalize(),
                "Total": total_biaya,
                "Metode Pembayaran": metode_pembayaran,
                "Pesanan Dibuat": tanggal_pesanan,
                "Estimasi Selesai": tanggal_estimasi,
                "Ditugaskan ke": staff_terpilih,
                "Status": Status
            })

# ======================== cetak struk =========================
        print("\n=========== STRUK PESANAN ===========")
        print(f"Username              : {username}")
        print(f"Nama                  : {nama}")
        print(f"No HP                 : {nohp}")
        print(f"Berat Cucian          : {berat} Kg")
        print(f"Metode Cucian         : {metodecucian.capitalize()}") #capitalize ini biar kalo inputannya "reguler" nanti hasil yang muncul "Reguler"
        print(f"Metode Pembayaran     : {metode_pembayaran}")
        print(f"Total Biaya           : Rp {total_biaya}")
        print(f"Tanggal Pemesanan     : {tanggal_pesanan}")
        print(f"Estimasi Selesai      : {tanggal_estimasi}")
        print(f"Ditugaskan ke         : {staff_terpilih}")
        print(f"Status                : {Status}")
        print("=====================================")

        tekan_enter = input("Tekan Enter untuk kembali ke menu...")
        os.system('cls')
        menu_staf()

    except ValueError:
        print("Input berat harus berupa angka.")

def update_status_pesanan():
    os.system('cls')
    print("=======================================")
    print("         Update Status Pesanan        ")
    print("=======================================")

    username = input("Masukkan username pelanggan: ").strip()

    try:
        with open('data_pesananD.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            daftar_pesanan = list(reader)

        pesanan_ditemukan = False

        for row in daftar_pesanan:
            if row['username'].strip().lower() == username.lower() and row['Status'].strip().lower() != 'selesai':
                pesanan_ditemukan = True
                print("\nPesanan ditemukan:")
                tabel = PrettyTable()
                tabel.field_names = ["Nama", "No Telp", "Berat /Kg", "Metode", "Total", 
                                     "Pembayaran", "Pesanan Dibuat", 
                                     "Estimasi Selesai", "Status", "Ditugaskan ke"]
                
                tabel.add_row([row["Nama"], row["No Hp"], row["Berat /Kg"], row["Metode cucian"],
                    row["Total"], row["Metode Pembayaran"], row["Pesanan Dibuat"],
                    row["Estimasi Selesai"], row["Status"], row["Ditugaskan ke"]])
                
                print("\nPesanan ditemukan:")
                print(tabel)

                print("\nStatus baru: [1] Diterima, [2] Siap diambil, [3] Selesai")
                pilihan = input("Pilih status baru [1/2/3]: ").strip()

                if pilihan == '1':
                    row['Status'] = 'Diterima'
                elif pilihan == '2':
                    row['Status'] = 'Siap diambil'
                elif pilihan == '3':
                    row['Status'] = 'Selesai'
                else:
                    print("Pilihan tidak valid. Update dibatalkan.")
                    return

                with open('data_pesananD.csv', mode='w', newline='') as file:
                    fieldnames = ['username', 'Nama', 'No Hp', 'Berat /Kg', 'Metode cucian', 'Total',
                                  'Metode Pembayaran', 'Pesanan Dibuat', 'Estimasi Selesai', 'Ditugaskan ke', 'Status']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(daftar_pesanan)

                print("Status berhasil diperbarui.\n")
                input("Tekan enter untuk kembali...")
                menu_staf()

        if not pesanan_ditemukan:
            print("Pesanan dengan username tersebut tidak ditemukan.")
            input("Tekan Enter untuk kembali...")
            menu_staf()

    except FileNotFoundError:
        print("File data_pesananD.csv tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        menu_staf()

#========================================== HALAMANNYA PELANGGAN INI ==============================================

def loginpelanggan():
    os.system('cls')
    print("========================================")
    print("Halo Pelanggan, Silahkan Login")
    print("========================================")
    username= (input(" Masukkan username = "))
    password= (input(" Masukkan password = "))
    kondisi = False
    data = []
    
    with open('akun_pelanggan.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            data.append({'username': row[0], 'password': row[1]})

    for row in data:
        if row['username'] == username and row['password'] == password :
            kondisi = True
            break

    if kondisi:
        print("Login berhasil!")
        input("Tekan Enter untuk lanjut...")
        menu_pelanggan(username) 
    else:
        print("Username atau password salah.")
        input("Tekan Enter untuk coba lagi...")
        loginpelanggan()   

def menu_pelanggan(username):
    os.system('cls')
    print("========================================")
    print("Hallo Pelanggan")
    print("========================================")
    print("1. Cek status pesanan")
    print("2. Cek riwayat pesanan")
    print("3. Keluar")
    pilihan = input("Pilih menu [1/2/3/4]: ")
    kondisi = True

    if not kondisi:
        os.system('cls')
        print("========================================")
        print("Kamu Bukan Pelanggan")
        print("========================================")
        loading("Kembali ke menu login")
        loginpelanggan()

    if pilihan == "1":
        cek_status_pesanan(username)
    elif pilihan == "2":
        cek_riwayat_pesanan(username)
    elif pilihan == "3":
        menu_regislogin()

def cek_status_pesanan(username):
    os.system('cls')
    print("========================================")
    print("       Pesanan yang Sedang Diproses     ")
    print("========================================")

    try:
        with open('data_pesananD.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            hasil = [
                row for row in reader 
                if row['username'] == username and row['Status'].lower() != 'Selesai'
            ]

        if not hasil:
            print("Tidak ada pesanan yang sedang diproses.")
        else:
            tabel = PrettyTable()
            tabel.field_names = [
                "Nama", "No Telp", "Berat /Kg", "Metode", "Total",
                "Pembayaran", "Dibuat", "Selesai", "Status", "Ditugaskan ke"
            ]

            for row in hasil:
                tabel.add_row([
                    row["Nama"], row["No Hp"], row["Berat /Kg"], row["Metode cucian"],
                    row["Total"], row["Metode Pembayaran"], row["Pesanan Dibuat"],
                    row["Estimasi Selesai"], row["Status"], row["Ditugaskan ke"]
                ])

            print(tabel)

    except FileNotFoundError:
        print("File data_pesananD.csv tidak ditemukan.")
    
    input("Tekan Enter untuk kembali...")
    menu_pelanggan(username)

def cek_riwayat_pesanan(username):
    os.system('cls')
    print("=========================================")
    print("          Riwayat Pesanan Selesai        ")
    print("=========================================")
    print("1. Urut berdasarkan BERAT (ringan ke berat)")
    print("2. Urut berdasarkan BULAN (Jan - Des)")
    print("3. Urut berdasarkan TOTAL BIAYA (murah ke mahal)")
    print("4. Kembali ke Menu Pelanggan")
    pilihan = input("Pilih metode pengurutan [1/2/3/4]: ")

    try:
        with open('data_pesananD.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            hasil = [
                row for row in reader 
                if row['username'] == username and row['Status'].lower() == 'selesai'
            ]

        if not hasil:
            print("Belum ada riwayat pesanan selesai.")
            input("Tekan Enter untuk kembali...")
            return

        if pilihan == "1":
            hasil = quick_sort(hasil, ambil_berat)
        elif pilihan == "2":
            hasil = quick_sort(hasil, ambil_bulan)
        elif pilihan == "3":
            hasil = quick_sort(hasil, ambil_total)
        elif pilihan == "4":
            menu_pelanggan(username)
            return
        else:
            print("Pilihan tidak valid.")
            return

        tabel = PrettyTable()
        tabel.field_names = [
            "Nama", "No Telp", "Berat /Kg", "Metode", "Total",
            "Pembayaran", "Dibuat", "Selesai", "Status", "Ditugaskan ke"
        ]

        for row in hasil:
            tabel.add_row([
                row["Nama"], row["No Hp"], row["Berat /Kg"], row["Metode cucian"],
                row["Total"], row["Metode Pembayaran"],row["Pesanan Dibuat"],
                row["Estimasi Selesai"], row["Status"],row["Ditugaskan ke"]
            ])

        print(tabel)

    except FileNotFoundError:
        print("File riwayat_pesanan.csv tidak ditemukan.")
    
    input("Tekan Enter untuk kembali ke menu...")  
    cek_riwayat_pesanan(username)

#===========================================PROGRAM MULAI===========================================

if __name__ == "__main__":
    menu_regislogin()