import tkinter as tk
from tkinter import Label, Frame, Scrollbar, Text
import calendar
import time
import random

root = tk.Tk()
root.title("NOTA PEMBELIAN")
root.geometry("300x700")
root.configure(bg="white")

# Tanggal dan waktu pemesanan
waktu_pemesanan = time.strftime("%d-%m-%Y %H:%M", time.localtime())

# Nomer antrian random
nomer_antrian = random.randint(10000,99999)

# Nota Section
warung = Label(root, text="WARPAT", bg="white", fg="black", font=("Helvetica", 16, "bold"))
warung.place(x=105, y=2)
alamat = Label(root, text="Surakarta, Jawa Tengah, Indonesia", bg="white", fg="black", font=("Helvetica", 10))
alamat.place(x=50, y=30)
nohp = Label(root, text="08112651176", bg="white", fg="black", font=("Helvetica", 10))
nohp.place(x=110, y=50)
judul = Label(root, text="NOTA PEMBELIAN", bg="white", fg="black", font=("Helvetica", 10, "bold"))
judul.place(x=90, y=84)
garis = Label(root, text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", bg="white", fg="black", font=("Helvetica", 10, "bold"))
garis.place(x=15, y=100)
waktu = Label(root, text= waktu_pemesanan , bg="white", fg="black", font=("Helvetica", 10))
waktu.place(x=15, y=120)
user = Label(root, text="USER", bg="white", fg="black", font=("Helvetica", 10))
user.place(x=15, y=140)
nama = Label(root, text="nama", bg="white", fg="black", font=("Helvetica", 10))
nama.place(x=230, y=137)
antrian = Label(root, text= nomer_antrian, bg="white", fg="black", font=("Helvetica", 10))
antrian.place(x=230, y=120)
type = Label(root, text="TYPE", bg="white", fg="black", font=("Helvetica", 10))
type.place(x=15, y=160)
metode = Label(root, text="tunai", bg="white", fg="black", font=("Helvetica", 10))
metode.place(x=230, y=157)
garis2 = Label(root, text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", bg="white", fg="black", font=("Helvetica", 10, "bold"))
garis2.place(x=15, y=177)

# Scroll
scroll = Scrollbar(root)
scroll.pack(side='right', fill='y')
textarea = Text(root, yscrollcommand=scroll.set)

def additem():
    textarea.insert('end', 'item\n')
    textarea.pack(side='left', fill='both')
    scroll.config(command=textarea.yview)




root.mainloop()