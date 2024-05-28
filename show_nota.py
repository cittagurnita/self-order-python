import csv
from PIL import Image
import time
import random
import calendar

# Waktu dan tanggal pemesanan
waktu_pemesanan = time.strftime("%d-%m-%Y %H:%M", time.localtime())
bulan_sekarang = calendar.month_abbr[time.localtime().tm_mon].upper()  # Mengambil tiga huruf pertama dari nama bulan

# Nomor antrian
nomer_antrian = random.randint(10000, 99999)

# Variabel global untuk menyimpan nama pelanggan dan metode pembayaran
nama_customer = ""
metode_bayar = ""
pesanan = []

# Fungsi untuk membaca kode promo dari file CSV
def baca_kode_promo(file_name):
    kode_promo = {}
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) < 2:
                    continue
                kode_promo[row[0]] = float(row[1])
    except FileNotFoundError:
        print(f"File '{file_name}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    return kode_promo

# Fungsi untuk memvalidasi kode promo berdasarkan bulan saat ini
def validasi_kode_promo(kode, kode_promo):
    if kode not in kode_promo:
        return "Kode promo tidak ditemukan"
    if bulan_sekarang not in kode.upper():
        return f"Kode promo hanya berlaku untuk bulan {bulan_sekarang}"
    return kode_promo[kode]

def input_customer():
    global nama_customer
    nama_customer = input("Masukkan Nama Anda: ")

def show_menu(file_name, menu_title):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            print(f"\nDaftar {menu_title} yang Tersedia:")
            print("=========================================")
            count = 1
            menu_list = []
            for row in reader:
                if len(row) < 2:
                    continue
                menu_list.append(row)
                print(f"Pilih Menu : {count}")
                print(f"Nama Menu  : {row[0]}")
                print(f"Harga      : {row[1]}")
                print("=========================================")
                count += 1
            return menu_list
    except FileNotFoundError:
        print(f"File '{file_name}' tidak ditemukan.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

def show_menu_bubur():
    return show_menu('menu_bubur.csv', 'Makanan')

def show_menu_extra():
    return show_menu('menu_extra.csv', 'Extra')

def show_menu_lauk():
    return show_menu('menu_lauk.csv', 'Makanan')

def show_menu_mie():
    return show_menu('menu_mie.csv', 'Makanan')

def show_menu_minum():
    return show_menu('menu_minum.csv', 'Minuman')

def show_menu_nasgor():
    return show_menu('menu_nasgor.csv', 'Makanan')

def show_menu_snack():
    return show_menu('menu_snack.csv', 'Makanan')

def choose_menu(pesan_list, kategori):
    if not pesan_list:
        print(f"Tidak ada menu {kategori} untuk dipilih.")
        return

    while True:
        try:
            choice = int(input(f"\nMasukkan nomor {kategori} yang Anda pilih: "))
            if 1 <= choice <= len(pesan_list):
                chosen_item = pesan_list[choice - 1]
                while True:
                    try:
                        quantity = int(input("Masukkan kuantitas: "))
                        if quantity > 0:
                            break
                        else:
                            print("Kuantitas harus lebih dari 0. Silakan coba lagi.")
                    except ValueError:
                        print("Masukkan angka yang valid untuk kuantitas.")
                
                print("\nAnda memilih :")
                print(f"Nama Menu  : {chosen_item[0]}")
                print(f"Harga      : {chosen_item[1]}")
                print(f"Kuantitas  : {quantity}\n")
                
                pesanan.append({
                    'nama': chosen_item[0],
                    'harga': int(chosen_item[1]),
                    'kuantitas': quantity
                })
                break
            else:
                print("Nomor yang Anda masukkan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Masukkan nomor yang valid.")

def choose_menu_makan(pesan_makan):
    choose_menu(pesan_makan, "makanan")

def choose_menu_minum(pesan_minum):
    choose_menu(pesan_minum, "minuman")

def choose_menu_ekstra(pesan_extra):
    choose_menu(pesan_extra, "extra")

def hitung_subtotal():
    total = 0
    for item in pesanan:
        total += item['harga'] * item['kuantitas']
    return total

# Fungsi untuk menampilkan rincian pesanan, subtotal, dan mengaplikasikan diskon jika ada kode promo
def tampilkan_rincian_dan_subtotal():
    print("\nRincian Pesanan Anda:")
    print("=========================================")
    for item in pesanan:
        print(f"Nama Menu  : {item['nama']}")
        print(f"Harga      : {item['harga']}")
        print(f"Kuantitas  : {item['kuantitas']}")
        print(f"Total      : {item['harga'] * item['kuantitas']}")
        print("-----------------------------------------")
    subtotal = hitung_subtotal()
    print(f"Subtotal   : {subtotal}")
    print("=========================================\n")

    kode_promo = input("Masukkan kode promo (jika ada, atau tekan Enter untuk melanjutkan): ").strip()
    total_diskon = 0
    if kode_promo:
        kode_promo_list = baca_kode_promo('list_koprom.csv')
        result = validasi_kode_promo(kode_promo, kode_promo_list)
        if isinstance(result, float):
            total_diskon = subtotal * result
            print(f"Total Diskon: {total_diskon}")
            print(f"Total Setelah Diskon: {subtotal - total_diskon}")
        else:
            print(result)
            print("Tidak ada diskon yang diterapkan.")
    else:
        print("Tidak ada kode promo yang dimasukkan.")

    print("=========================================\n")

    # Menyimpan diskon dan harga akhir untuk nota
    global total_diskon_final, total_setelah_diskon_final
    total_diskon_final = total_diskon
    total_setelah_diskon_final = subtotal - total_diskon

def pilih_metode():
    print("========Pilih Metode Pembayaran=========")
    print("1. Tunai\n2. Qris\n3. Transfer")
    metode_bayar = int(input("Pilih metode pembayaran: "))
    if metode_bayar == 1:
        return "Tunai"
    elif metode_bayar == 2:
        return "QRIS"
    elif metode_bayar == 3:
        return "Transfer"
    else:
        return "Tidak valid"

def bayar_tunai():
    total = total_setelah_diskon_final if total_diskon_final else hitung_subtotal()
    print("Silahkan ambil nota dan siapkan uang sebesar Rp", total, " lalu transaksi di kasir")

def bayar_qris():
    total = total_setelah_diskon_final if total_diskon_final else hitung_subtotal()
    print("Silahkan bayar sebesar Rp", total)
    qris = Image.open("qris.jpg")
    qris.show()

def bayar_transfer():
    total = total_setelah_diskon_final if total_diskon_final else hitung_subtotal()
    print("1. Bank Jago\n2. Bank Rakyat Indonesia\n3. Bank Negara Indonesia\n4. Bank Syariah Indonesia\n5. Bank CIMB Niaga")
    rekening_tujuan = int(input("Pilih jenis bank: "))
    if rekening_tujuan == 1:
        print("Bayar pesanan anda sebesar Rp", total, "ke rekening tujuan 104976349648 a.n. Fedo Niam Buya Kharismawanto")
    elif rekening_tujuan == 2:
        print("Bayar pesanan anda sebesar Rp", total, "ke rekening tujuan 6632 0102 3871 530 a.n. Bima Aryasakti Persada")
    elif rekening_tujuan == 3:
        print("Bayar pesanan anda sebesar Rp", total, "ke rekening tujuan 1786806019 a.n. Aghniya Ajrun Nisa")
    elif rekening_tujuan == 4:
        print("Bayar pesanan anda sebesar Rp", total, "ke rekening tujuan 7240491014 a.n. Ferizki Ferdinata")
    elif rekening_tujuan == 5:
        print("Bayar pesanan anda sebesar Rp", total, "ke rekening tujuan 707638220000 a.n. Citta Gurnita Prasista")
    else:
        print("Maaf, kode tidak valid")

def rincian_nota():
    for item in pesanan:
        print(f"{item['nama']}")
        print(f"            {item['kuantitas']} X    @{item['harga']}       {item['harga'] * item['kuantitas']}")
        print("------------------------------------")
    subtotal = hitung_subtotal()
    print(f"                 Subtotal   : {subtotal}")
    if total_diskon_final:
        print(f"                 Diskon     : -{total_diskon_final}")
        print(f"                 Total      : {total_setelah_diskon_final}")
    print("====================================\n")

def nota_pembelian():
    print("              WARPAT                ")
    print("  Surakarta, Jawa Tengah, Indonesia ")
    print("           08112651176              ")
    print("====================================")
    print("           NOTA PEMBELIAN           ")
    print("====================================")
    print(waktu_pemesanan,"             ", nomer_antrian)
    print("USER                          ", nama_customer)
    print("TYPE                          ", metode_bayar)
    print("====================================")
    rincian_nota()

def pilih_menu():
    print("1. Makanan\n2. Minuman\n3. Extra\n4. Lihat Rincian dan Subtotal\n5. Selesaikan Pesanan dan Pilih Pembayaran\n0. Batalkan Pesanan")
    pilih_menu = int(input("Masukkan menu yang ingin dipilih: "))
    return pilih_menu

def pilih_menu_makanan():
    print("1. Bubur\n2. Lauk\n3. Mie\n4. Nasgor\n5. Snack\n0. Kembali")
    pilih_menu_makanan = int(input("Masukkan jenis makanan yang ingin dipesan: "))
    return pilih_menu_makanan

def main_coba_pesan():
    global metode_bayar
    input_customer()
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
            elif menu_makan == 0:
                continue
            else:
                print("Makanan tidak valid")
                continue
            choose_menu_makan(pesan_makan)
        elif lihat_menu == 2:
            pesan_minum = show_menu_minum()
            choose_menu_minum(pesan_minum)
        elif lihat_menu == 3:
            pesan_extra = show_menu_extra()
            choose_menu_ekstra(pesan_extra)
        elif lihat_menu == 4:
            tampilkan_rincian_dan_subtotal()
        elif lihat_menu == 5:
            tampilkan_rincian_dan_subtotal()
            metode_bayar = pilih_metode()
            if metode_bayar == "Tunai":
                bayar_tunai()
                nota_pembelian()
                break
            elif metode_bayar == "QRIS":
                bayar_qris()
                nota_pembelian()
                break
            elif metode_bayar == "Transfer":
                bayar_transfer()
                nota_pembelian()
                break
            else:
                print("Metode pembayaran tidak valid")
        elif lihat_menu == 0:
            print("Pesanan dibatalkan")
            break
        else:
            print("Menu tidak valid")

if __name__ == "__main__":
    main_coba_pesan()
