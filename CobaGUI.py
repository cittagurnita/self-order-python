import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import random
import calendar
import time
from show_nota import nota_pembelian

# Global variables
nama_customer = ""
metode_bayar = ""
pesanan = []

# Time and date of the order
waktu_pemesanan = time.strftime("%d-%m-%Y %H:%M", time.localtime())
bulan_sekarang = calendar.month_name[time.localtime().tm_mon].upper()

# Queue number
nomer_antrian = random.randint(10000, 99999)

# Load promo codes from CSV
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

# Validate promo code based on the current month
def validasi_kode_promo(kode, kode_promo):
    if kode not in kode_promo:
        return "Kode tidak valid"
    if bulan_sekarang[:3] not in kode.upper():
        return "Kode tidak berlaku bulan ini"
    return kode_promo[kode]

# Load menu from CSV
def show_menu(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            menu_list = [row for row in reader if len(row) >= 2]
            return menu_list
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{file_name}' tidak ditemukan.")
        return []
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
        return []

def hitung_subtotal():
    return sum(item['harga'] * item['kuantitas'] for item in pesanan)

# Display order details and subtotal, apply discount if promo code is valid
def tampilkan_rincian_dan_subtotal():
    subtotal = hitung_subtotal()
    total_diskon = 0
    kode_promo = entry_promo.get().strip()

    if kode_promo:
        kode_promo_list = baca_kode_promo('list_koprom.csv')
        result = validasi_kode_promo(kode_promo, kode_promo_list)
        if isinstance(result, float):
            total_diskon = subtotal * result
            lbl_total_diskon.config(text=f"Total Diskon: {total_diskon:.2f}")
        else:
            lbl_total_diskon.config(text=result)
            total_diskon = 0
    else:
        lbl_total_diskon.config(text="Tidak ada kode promo yang dimasukkan.")

    lbl_subtotal.config(text=f"Subtotal: {subtotal:.2f}")
    lbl_total.config(text=f"Total: {subtotal - total_diskon:.2f}")

    global total_diskon_final, total_setelah_diskon_final
    total_diskon_final = total_diskon
    total_setelah_diskon_final = subtotal - total_diskon

# Main window
root = tk.Tk()
root.title("Aplikasi Pemesanan")
root.geometry("600x400")

# Name entry
tk.Label(root, text="Masukkan Nama Anda:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Promo code entry
tk.Label(root, text="Masukkan kode promo (jika ada):").pack()
entry_promo = tk.Entry(root)
entry_promo.pack()

# Order details labels
lbl_subtotal = tk.Label(root, text="Subtotal: 0")
lbl_subtotal.pack()

lbl_total_diskon = tk.Label(root, text="Total Diskon: 0")
lbl_total_diskon.pack()

lbl_total = tk.Label(root, text="Total: 0")
lbl_total.pack()

# Menu selection functions
def select_menu(menu_list, category):
    if not menu_list:
        messagebox.showerror("Error", f"Tidak ada menu {category} untuk dipilih.")
        return
    
    menu_window = tk.Toplevel(root)
    menu_window.title(f"Daftar {category}")
    for index, item in enumerate(menu_list):
        tk.Label(menu_window, text=f"{index+1}. {item[0]} - {item[1]}").pack()
    
    tk.Label(menu_window, text="Pilih nomor menu:").pack()
    entry_menu_choice = tk.Entry(menu_window)
    entry_menu_choice.pack()

    tk.Label(menu_window, text="Masukkan kuantitas:").pack()
    entry_quantity = tk.Entry(menu_window)
    entry_quantity.pack()

    def add_to_order():
        try:
            choice = int(entry_menu_choice.get())
            quantity = int(entry_quantity.get())
            if 1 <= choice <= len(menu_list) and quantity > 0:
                chosen_item = menu_list[choice - 1]
                pesanan.append({
                    'nama': chosen_item[0],
                    'harga': int(chosen_item[1]),
                    'kuantitas': quantity
                })
                messagebox.showinfo("Info", f"{chosen_item[0]} ditambahkan ke pesanan.")
                menu_window.destroy()
            else:
                messagebox.showerror("Error", "Pilihan atau kuantitas tidak valid.")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")

    tk.Button(menu_window, text="Tambah ke Pesanan", command=add_to_order).pack()

# Order menu functions
def show_menu_makanan():
    pilih_menu_makanan = tk.Toplevel(root)
    pilih_menu_makanan.title("Pilih Menu Makanan")
    tk.Button(pilih_menu_makanan, text="Bubur", command=lambda: select_menu(show_menu('menu_bubur.csv'), 'Bubur')).pack()
    tk.Button(pilih_menu_makanan, text="Lauk", command=lambda: select_menu(show_menu('menu_lauk.csv'), 'Lauk')).pack()
    tk.Button(pilih_menu_makanan, text="Mie", command=lambda: select_menu(show_menu('menu_mie.csv'), 'Mie')).pack()
    tk.Button(pilih_menu_makanan, text="Nasgor", command=lambda: select_menu(show_menu('menu_nasgor.csv'), 'Nasgor')).pack()
    tk.Button(pilih_menu_makanan, text="Snack", command=lambda: select_menu(show_menu('menu_snack.csv'), 'Snack')).pack()

def show_menu_minuman():
    select_menu(show_menu('menu_minum.csv'), 'Minuman')

def show_menu_extra():
    select_menu(show_menu('menu_extra.csv'), 'Extra')

# Payment method selection
def pilih_metode_pembayaran():
    pembayaran_window = tk.Toplevel(root)
    pembayaran_window.title("Pilih Metode Pembayaran")
    tk.Button(pembayaran_window, text="Tunai", command=lambda: bayar('Tunai')).pack()
    tk.Button(pembayaran_window, text="QRIS", command=lambda: bayar('QRIS')).pack()
    tk.Button(pembayaran_window, text="Transfer", command=lambda: bayar('Transfer')).pack()

def bayar(metode):
    global metode_bayar
    metode_bayar = metode
    if metode == "Tunai":
        bayar_tunai()
    elif metode == "QRIS":
        bayar_qris()
    elif metode == "Transfer":
        bayar_transfer()
    nota_pembelian()

def bayar_tunai():
    total = total_setelah_diskon_final if total_diskon_final else hitung_subtotal()
    messagebox.showinfo("Info", f"Siapkan uang sebesar Rp {total} lalu transaksi di kasir.")

def bayar_qris():
    total = total_setelah_diskon_final if total_diskon_final else hitung_subtotal()
    messagebox.showinfo("Info", f"Silahkan bayar sebesar Rp {total}.")
    qris = Image.open("qris.jpg")
    qris.show()

def bayar_transfer():
    total = total_setelah_diskon_final if total_diskon_final else hitung_subtotal()
    transfer_window = tk.Toplevel(root)
    transfer_window.title("Transfer Bank")
    tk.Label(transfer_window, text=f"Bayar pesanan anda sebesar Rp {total} ke salah satu rekening berikut:").pack()
    tk.Label(transfer_window, text="1. Bank Jago: 104976349648 a.n. Fedo Niam Buya Kharismawanto").pack()
    tk.Label(transfer_window, text="2. BRI: 6632 0102 3871 530 a.n. Bima Aryasakti Persada").pack()
    tk.Label(transfer_window, text="3. BNI: 1786806019 a.n. Aghniya Ajrun Nisa").pack()
    tk.Label(transfer_window, text="4. BSI: 7240491014 a.n. Ferizki Ferdinata").pack()
    tk.Label(transfer_window, text="5. CIMB Niaga: 707638220000 a.n. Citta Gurnita Prasista").pack()

# Purchase receipt
def rincian_nota():
    nota_window = tk.Toplevel(root)
    nota_window.title("Nota Pembelian")
    tk.Label(nota_window, text="WARPAT").pack()
    tk.Label(nota_window, text="Surakarta, Jawa Tengah, Indonesia").pack()
    tk.Label(nota_window, text="08112651176").pack()
    tk.Label(nota_window, text="====================================").pack()
    tk.Label(nota_window, text="NOTA PEMBELIAN").pack()
    tk.Label(nota_window, text="====================================").pack()
    tk.Label(nota_window, text=f"{waktu_pemesanan}    {nomer_antrian}").pack()
    tk.Label(nota_window, text=f"USER: {nama_customer}").pack()
    tk.Label(nota_window, text=f"TYPE: {metode_bayar}").pack()
    tk.Label(nota_window, text="====================================").pack()
    for item in pesanan:
        tk.Label(nota_window, text=f"{item['nama']} - {item['kuantitas']} x @ {item['harga']} = {item['harga'] * item['kuantitas']}").pack()
    subtotal = hitung_subtotal()
    tk.Label(nota_window, text=f"Subtotal: {subtotal}").pack()
    if total_diskon_final:
        tk.Label(nota_window, text=f"Diskon: -{total_diskon_final}").pack()
        tk.Label(nota_window, text=f"Total: {total_setelah_diskon_final}").pack()

# Main menu buttons
tk.Button(root, text="Pilih Makanan", command=show_menu_makanan).pack()
tk.Button(root, text="Pilih Minuman", command=show_menu_minuman).pack()
tk.Button(root, text="Pilih Extra", command=show_menu_extra).pack()
tk.Button(root, text="Lihat Rincian dan Subtotal", command=tampilkan_rincian_dan_subtotal).pack()
tk.Button(root, text="Selesaikan Pesanan dan Pilih Pembayaran", command=pilih_metode_pembayaran).pack()

root.mainloop()
