import csv
from PIL import Image


pesanan = []

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
    return show_menu('Menu_extra.csv', 'Extra')

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

def tampilkan_rincian_dan_subtotal():
    print("\nRincian Pesanan Anda:")
    print("=========================================")
    for item in pesanan:
        print(f"Nama Menu  : {item['nama']}")
        print(f"Harga      : {item['harga']}")
        print(f"Kuantitas  : {item['kuantitas']}")
        print(f"Total      : {item['harga'] * item['kuantitas']}")
        print("-----------------------------------------")
    total = hitung_subtotal()
    print(f"Subtotal   : {total}")
    print("=========================================\n")

def bayar_tunai():
    total = hitung_subtotal()
    print("Silahkan ambil nota dan siapkan uang sebesar Rp", total," lalu transaksi di kasir")
    
def bayar_qris():
    total = hitung_subtotal()
    print("Silahkan bayar sebesar Rp", total)
    qris = Image.open("qris.jpg")
    qris.show()

def bayar_transfer():
    total = hitung_subtotal()
    print("1.Bank Jago\n2.Bank Rakyat Indonesia\n3.Bank Negara Indonesia\n4.Bank Syariah Indonesia\n5.Bank CIMB Niaga")
    rekening_tujuan = int(input("Pilih jenis bank:"))
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

def pilih_metode():
    print("========Pilih Metode Pembayaran=========")
    print("1.Tunai\n2.Qris\n3.Transfer")
    pilih_metode = int(input("Pilih metode pembayaran:"))
    return pilih_metode

def pilih_menu():
    print("1.Makanan\n2.Minuman\n3.Extra\n4.Lihat Rincian dan Subtotal\n5.Selesaikan Pesanan dan Pilih Pembayaran\n0.Batalkan Pesanan")
    pilih_menu = int(input("Masukan menu yang ingin dipilih: "))
    return pilih_menu

def pilih_menu_makanan():
    print("1.Bubur\n2.Lauk\n3.Mie\n4.Nasgor\n5.Snack\n0.Kembali")
    pilih_menu_makanan = int(input("Masukan jenis makanan yang ingin dipesan: "))
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
            metode_bayar = pilih_metode()
            if metode_bayar == 1:
                bayar_tunai()
                break
            elif metode_bayar == 2:
                bayar_qris()
                break
            elif metode_bayar == 3:
                bayar_transfer()
                break
            else:
                print("Metode pembayaran tidak valid")
        elif lihat_menu == 0:
            print("Pesanan dibatalkan")
            break
        else:
            print("Menu tidak Valid")

if __name__ == "__main__":
    main_coba_pesan()
