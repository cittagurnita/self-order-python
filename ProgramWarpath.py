import csv
import pandas

#pemilihan jenis menu
def show_menu_bubur():
    try:
        with open('menu_bubur.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            print("\nDaftar Makanan yang Tersedia:")
            print("=========================================")
            count = 1
            pesan_makan = []  # List untuk menyimpan data makanan
            for row in reader:
                if len(row) < 2:
                    continue  # Skip rows that don't have enough columns
                pesan_makan.append(row)  # Menambahkan data makanan ke list
                print(f"Pilih Menu : {count}")
                print(f"Nama Menu  : {row[0]}")
                print(f"Harga      : {row[1]}")
                print("=========================================")
                count += 1
            return pesan_makan
    except FileNotFoundError:
        print("File 'menu_bubur.csv' tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

def show_menu_extra():
    try:
        with open('Menu_extra.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            print("\nDaftar Makanan yang Tersedia:")
            print("=========================================")
            count = 1
            pesan_makan = []  # List untuk menyimpan data makanan
            for row in reader:
                if len(row) < 2:
                    continue  # Skip rows that don't have enough columns
                pesan_makan.append(row)  # Menambahkan data makanan ke list
                print(f"Pilih Menu : {count}")
                print(f"Nama Menu  : {row[0]}")
                print(f"Harga      : {row[1]}")
                print("=========================================")
                count += 1
            return pesan_makan
    except FileNotFoundError:
        print("File 'Menu_extra.csv' tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

def show_menu_lauk():
    try:
        with open('menu_lauk.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            print("\nDaftar Makanan yang Tersedia:")
            print("=========================================")
            count = 1
            pesan_makan = []  # List untuk menyimpan data makanan
            for row in reader:
                if len(row) < 2:
                    continue  # Skip rows that don't have enough columns
                pesan_makan.append(row)  # Menambahkan data makanan ke list
                print(f"Pilih Menu : {count}")
                print(f"Nama Menu  : {row[0]}")
                print(f"Harga      : {row[1]}")
                print("=========================================")
                count += 1
            return pesan_makan
    except FileNotFoundError:
        print("File 'menu_lauk.csv' tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

def show_menu_mie():
    try:
        with open('menu_mie.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            print("\nDaftar Makanan yang Tersedia:")
            print("=========================================")
            count = 1
            pesan_makan = []  # List untuk menyimpan data makanan
            for row in reader:
                if len(row) < 2:
                    continue  # Skip rows that don't have enough columns
                pesan_makan.append(row)  # Menambahkan data makanan ke list
                print(f"Pilih Menu : {count}")
                print(f"Nama Menu  : {row[0]}")
                print(f"Harga      : {row[1]}")
                print("=========================================")
                count += 1
            return pesan_makan
    except FileNotFoundError:
        print("File 'menu_mie.csv' tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

def show_menu_minum():
    try:
        with open('menu_minum.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            print("\nDaftar Makanan yang Tersedia:")
            print("=========================================")
            count = 1
            pesan_makan = []  # List untuk menyimpan data makanan
            for row in reader:
                if len(row) < 2:
                    continue  # Skip rows that don't have enough columns
                pesan_makan.append(row)  # Menambahkan data makanan ke list
                print(f"Pilih Menu : {count}")
                print(f"Nama Menu  : {row[0]}")
                print(f"Harga      : {row[1]}")
                print("=========================================")
                count += 1
            return pesan_makan
    except FileNotFoundError:
        print("File 'menu_minum.csv' tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

def show_menu_nasgor():
    try:
        with open('menu_nasgor.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            print("\nDaftar Makanan yang Tersedia:")
            print("=========================================")
            count = 1
            pesan_makan = []  # List untuk menyimpan data makanan
            for row in reader:
                if len(row) < 2:
                    continue  # Skip rows that don't have enough columns
                pesan_makan.append(row)  # Menambahkan data makanan ke list
                print(f"Pilih Menu : {count}")
                print(f"Nama Menu  : {row[0]}")
                print(f"Harga      : {row[1]}")
                print("=========================================")
                count += 1
            return pesan_makan
    except FileNotFoundError:
        print("File 'menu_nasgor.csv' tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

def show_menu_snack():
    try:
        with open('menu_snack.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            print("\nDaftar Makanan yang Tersedia:")
            print("=========================================")
            count = 1
            pesan_makan = []  # List untuk menyimpan data makanan
            for row in reader:
                if len(row) < 2:
                    continue  # Skip rows that don't have enough columns
                pesan_makan.append(row)  # Menambahkan data makanan ke list
                print(f"Pilih Menu : {count}")
                print(f"Nama Menu  : {row[0]}")
                print(f"Harga      : {row[1]}")
                print("=========================================")
                count += 1
            return pesan_makan
    except FileNotFoundError:
        print("File 'menu_snack.csv' tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []
    
#Program Warpath
def welcome_message():
    print("==============================================================")
    print("                  SELAMAT DATANG DI WARPATH!                  ")
    print("--------------Silahkan Memesan Sesuai Menu Kami---------------")
    print("==============================================================")
    print()
print(welcome_message())  

#input nama
def input_customer():
    nama = input("Masukkan Nama Anda : ")
    print(f"Halo", (nama), "Selamat datang di sini!")
    print()
print(input_customer())



def pilih():
    print("=========Daftar Menu===========")
    print("1.Makanan\n2.Minuman\n3.Extra")

def choose_menu_makan(pesan_makan):
    if not pesan_makan:
        print("Tidak ada menu makanan untuk dipilih.")
        return

    while True:
        try:
            choice = int(input("\nMasukkan nomor makanan yang Anda pilih: "))
            if 1 <= choice <= len(pesan_makan):
                chosen_makan = pesan_makan[choice - 1]
                print("\nAnda memilih :")
                print(f"Nama Menu  : {chosen_makan[0]}")
                print(f"Harga      : {chosen_makan[1]}\n")
                break
            else:
                print("Nomor yang Anda masukkan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Masukkan nomor yang valid.")

def pilih_menu():
    print("1.Makanan\n2.Minuman\n3.Ekstra\n4.Keluar/Kembali")
    pilih_menu = int(input("Masukan menu yang ingin dipilih:"))
    return pilih_menu

def pilih_menu_makanan():
    print("1.Bubur\n2.Lauk\n3.Mie\n4.Nasgor\n5.Snack\n6.Kembali/keluar")
    pilih_menu_makanan = int(input("Masukan jenis makanan yang ingin dipesan:"))
    return pilih_menu_makanan

def main_coba_pesan():
    while True:
        lihat_menu = pilih_menu()
        if lihat_menu == 1:
            menu_makan = pilih_menu_makanan()
            if menu_makan == 1:
                pesan_makan = show_menu_bubur()
            elif menu_makan == 2:
                pesan_makan = show_menu_lauk()
            elif menu_makan == 3:
                pesan_makan = show_menu_mie()
            elif menu_makan == 4:
                pesan_makan = show_menu_nasgor()
            elif menu_makan == 5:
                pesan_makan = show_menu_snack()
            elif menu_makan == 6:
                continue
            else:
                print("Makanan tidak valid")
                continue

            choose_menu_makan(pesan_makan)
        elif lihat_menu == 2:
            pesan_makan = show_menu_minum()
            choose_menu_makan(pesan_makan)
        elif lihat_menu == 3:
            pesan_makan = show_menu_extra()
            choose_menu_makan(pesan_makan)
        elif lihat_menu == 4:
            break
        else:
            print("Menu tidak Valid")

if __name__ == "__main__":
    main_coba_pesan()
