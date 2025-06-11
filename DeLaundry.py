import csv
import os
from pathlib import Path
import pandas as pd
from datetime import datetime, timedelta, date
import time
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
    print("2. pelanggan")
    pilihan = input("Admin/pelanggan[1/2] : ")
    if pilihan == "1":
        os.system('cls') 
        loading("Harap Tunggu")
        if not Path('data_adminD.csv').is_file():
            with open('data_adminD.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['username', 'masukkan'], delimiter=',') 
                header.writeheader()
                writer = csv.writer(filecsv)
                writer.writerow(['admin', '123'])
                    
            if not Path('data_pesananD.csv').is_file():
                with open('data_pesananD.csv', 'w', newline='') as filecsv:
                    header = csv.DictWriter(filecsv, fieldnames=['Nama', 'Nomer Hp', 'Berat /Kg', 'Metode Cucian', 'Status', 'Total Biaya'], delimiter=',')
                    header.writeheader()

        if not Path('riwayat_transaksi.csv').is_file():
            with open('riwayat_transaksi.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['Nama', 'Nomer Hp', 'Berat /Kg', 'Metode Cucian', 'Status', 'Total Biaya'], delimiter=',')
                header.writeheader()

        os.system('cls')            
        print(35 * "==")
        print("Menuju Menu Login")
        print(35 * "\n==")
        loginadminD('data_adminD')

    elif pilihan == "2":
        os.system('cls')
        print("A. Registrasi")
        print("B. Login")
        jawaban = str(input("Registrasi/Login[A/B] : ")).upper()
        if jawaban == "A" :
                os.system('cls')
                print(35 * "==")
                loading("Silahkan Registrasi")
                print('\n 35 * "==')
                loading("Masuk ke menu Registrasi")
                if not(Path('data_pelanggan.csv').is_file()):
                    with open('data_pelanggan.csv', 'w', newline='') as filecsv:
                        header = csv.DictWriter(filecsv, fieldnames=['username','password'],  delimiter=',') 
                        header.writeheader()
                if not(Path('datastok.csv').is_file()):
                    with open('datastok.csv', 'w', newline='') as filecsv:
                        header = csv.DictWriter(filecsv, fieldnames=['nama','jenisbarang','harga','stok','expireddate'],  delimiter=',') 
                        header.writeheader()
                username= (input("\nMasukkan username = "))
                kondisi = False
                data = []
        
                with open('data_pelanggan.csv', 'r') as file:
                    csv_user = csv.reader(file, delimiter=',')
                    for row in csv_user:
                        data.append({'username': row[0]})
        
                for row in data:
                    if row['username'] == username:
                        kondisi = True
                        break
            
                if kondisi:
                    os.system('cls')
                    print(35 * "==")
                    print("username sudah terdaftar")
                    print("Silahkan registrasi dengan username lain")
                    print('\n 35 * "==')
                    loading("Kembali ke menu registrasi")
        
                else:
                    masukkan= (input("Masukkan masukkan = "))
                    with open('data_pelanggan.csv', 'a', newline='') as file:
                        csv_user = csv.writer(file, delimiter=',')
                        csv_user.writerow([username,masukkan])
                        file.close()
                
                    print(35 * "==")
                    loading("Registrasi Berhasil")
                    os.system('cls')
                    loading("Masuk ke menu login")
                    loginpelanggan()

        elif jawaban == "B" :
                print('\n 35 * "==')
                loading("Masuk Ke Menu Login")
                loginpelanggan()
        else: print("Pilihan tidak tersedia")
        
    else:
        menu_regislogin()


def loginadminD():
    menu_regislogin()


if __name__ == "__main__":
    menu_regislogin()
    