import csv
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

def baca_csv(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def simpan_pesanan(pesanan):
    order_details = get_order_summary()
    with open("order_makan.csv", "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Menu', 'Jumlah', 'Harga']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for menu, jumlah, harga in order_details:
            writer.writerow({'Menu': menu, 'Jumlah': jumlah, 'Harga': harga})

    messagebox.showinfo("Pesanan Disimpan", "Pesanan telah disimpan")
    exit()

def pesan(menu, jumlah, pesanan):
    if jumlah > 0:
        if menu in pesanan:
            pesanan[menu] += jumlah
        else:
            pesanan[menu] = jumlah
        update_order_summary(pesanan)

def kurangi_pesanan(menu, pesanan):
    if menu in pesanan:
        if pesanan[menu] > 1:
            pesanan[menu] -= 1
        else:
            del pesanan[menu]
        update_order_summary(pesanan)

def tambah_jumlah(entry):
    current_value = int(entry.get())
    entry.delete(0, "end")
    entry.insert(0, str(current_value + 1))

def kurangi_jumlah(entry):
    current_value = int(entry.get())
    if current_value > 0:
        entry.delete(0, "end")
        entry.insert(0, str(current_value - 1))

def update_order_summary(pesanan):
    for widget in order_frame.winfo_children():
        widget.destroy()

    total_harga = 0
    for menu, jumlah in pesanan.items():
        for item in data_makanan:
            if item["Nama Menu"] == menu:
                harga = int(item["Harga"]) * jumlah
                total_harga += harga
                frame = ctk.CTkFrame(master=order_frame, fg_color="#fbcd64")
                frame.pack(anchor="w", padx=10, pady=5, fill="x")
                ctk.CTkLabel(frame, text=f"{menu} (x{jumlah}): Rp {harga}", text_color="#8B4513").pack(side="left", anchor="w", padx=10)
                button_kurangi = ctk.CTkButton(frame, text="Kurangi", command=lambda item=menu: kurangi_pesanan(item, pesanan), width=7, height=2, fg_color="#8B4513")
                button_kurangi.pack(side="right", anchor="e", padx=10)

    ctk.CTkLabel(order_frame, text=f"Total Harga: Rp {total_harga}", text_color="#8B4513").pack(anchor="w", padx=10, pady=5)
    return total_harga

def get_order_summary():
    total_harga = 0
    order_details = []
    for menu, jumlah in pesanan.items():
        for item in data_makanan:
            if item["Nama Menu"] == menu:
                harga = int(item["Harga"]) * jumlah
                total_harga += harga
                order_details.append((menu, jumlah, harga))
    return order_details

ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Daftar Makanan")
root.geometry("850x500")
root.configure(fg_color="#fbcd64")

menu_frame = ctk.CTkFrame(master=root, fg_color="#fbcd64")
menu_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

canvas = ctk.CTkCanvas(master=menu_frame, bg="#fbcd64")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(master=menu_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = ctk.CTkFrame(master=canvas, fg_color="#fbcd64")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

order_frame = ctk.CTkFrame(master=root, width=300, fg_color="#fbcd64")
order_frame.pack(side="right", fill="y", padx=10, pady=10, anchor="n")

data_makanan = baca_csv("menu_makan.csv")

pesanan = {}

order_summary_label = ctk.CTkLabel(master=order_frame, text="", justify="left")
order_summary_label.pack(anchor="w", padx=10, pady=5)

for i, item in enumerate(data_makanan):
    label_menu = ctk.CTkLabel(master=scrollable_frame, text=item["Nama Menu"], text_color="#8B4513")
    label_menu.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

    entry_kuantitas = ctk.CTkEntry(master=scrollable_frame, width=50, font=("Helvetica", 14))
    entry_kuantitas.grid(row=i + 1, column=1, padx=5, pady=5, sticky="w")
    entry_kuantitas.insert(0, "0")

    button_tambah = ctk.CTkButton(master=scrollable_frame, text="+", font=("Helvetica", 10), command=lambda entry=entry_kuantitas: tambah_jumlah(entry), width=30, height=2, fg_color="#8B4513")
    button_tambah.grid(row=i + 1, column=2, padx=5, pady=5, sticky="w")

    button_kurangi = ctk.CTkButton(master=scrollable_frame, text="-", font=("Helvetica", 10), command=lambda entry=entry_kuantitas: kurangi_jumlah(entry), width=30, height=2, fg_color="#8B4513")
    button_kurangi.grid(row=i + 1, column=3, padx=5, pady=5, sticky="w")

    button_pesan = ctk.CTkButton(master=scrollable_frame, text="Pesan", command=lambda item=item["Nama Menu"], entry=entry_kuantitas: pesan(item, int(entry.get()), pesanan), fg_color="#8B4513")
    button_pesan.grid(row=i + 1, column=4, padx=10, pady=5, sticky="w")

button_simpan = ctk.CTkButton(master=root, text="Simpan Pesanan", command=lambda: simpan_pesanan(pesanan), fg_color="#8B4513")
button_simpan.place(relx=0.95, rely=0.95, anchor="se")

root.mainloop()

