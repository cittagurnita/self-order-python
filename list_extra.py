import csv
import customtkinter as ctk
from tkinter import ttk

def baca_csv(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def buat_label_entry(frame, text, row, col):
    label = ctk.CTkLabel(master=frame, text=text)
    label.grid(row=row, column=col, padx=10, pady=5, sticky="w")

    entry = ctk.CTkEntry(master=frame, width=50, font=("Helvetica", 14))
    entry.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")
    return entry

pesanan = []  # List untuk menyimpan pesanan yang telah dipesan

def pesan(menu, jumlah):
    # Menambahkan pesanan ke dalam list pesanan
    pesanan.append((menu, jumlah.get()))
    print(f"Pesanan: {menu}, Jumlah: {jumlah.get()}")
    update_order_summary()

def kurangi_pesanan(menu):
    # Mengurangi jumlah pesanan atau menghapus pesanan jika jumlah mencapai nol
    for i, (m, j) in enumerate(pesanan):
        if m == menu:
            if int(j) > 1:
                pesanan[i] = (m, str(int(j) - 1))
            else:
                pesanan.pop(i)
            break
    update_order_summary()

def kembali_ke_menu_sebelumnya():
    root.destroy()

def scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=800, height=400)

root = ctk.CTk()
root.title("Daftar Extra")
root.geometry("1366x768")

main_frame = ctk.CTkFrame(master=root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create a frame for the scrollable menu on the left side
menu_frame = ctk.CTkFrame(master=main_frame)
menu_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

canvas = ctk.CTkCanvas(master=menu_frame)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(master=menu_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

scrollable_frame = ctk.CTkFrame(master=canvas)

scrollable_frame.bind("<Configure>", scroll)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame for the order summary on the right side
order_frame = ctk.CTkFrame(master=main_frame)
order_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

data_extra = baca_csv("Menu_extra.csv")

for i, item in enumerate(data_extra):
    entry = buat_label_entry(scrollable_frame, item["Nama Extra"], i + 1, 0)
    button_pesan = ctk.CTkButton(master=scrollable_frame, text="Pesan", command=lambda item=item["Nama Extra"], jumlah=entry: pesan(item, jumlah))
    button_pesan.grid(row=i + 1, column=2, padx=10, pady=5, sticky="w")

def update_order_summary():
    for widget in order_frame.winfo_children():
        widget.destroy()

    total_harga = 0
    for i, (menu, jumlah) in enumerate(pesanan):
        for item in data_extra:
            if item["Nama Extra"] == menu:
                harga = int(item["Harga"]) * int(jumlah)
                total_harga += harga
                frame = ctk.CTkFrame(master=order_frame)
                frame.pack(anchor="w", padx=10, pady=5, fill="x")
                ctk.CTkLabel(frame, text=f"{menu} (x{jumlah}): Rp {harga}").pack(side="left", anchor="w", padx=10)
                button_kurangi = ctk.CTkButton(frame, text="Kurangi", command=lambda item=menu: kurangi_pesanan(item))
                button_kurangi.pack(side="right", anchor="e", padx=10)

    total_frame = ctk.CTkFrame(master=order_frame)
    total_frame.pack(anchor="w", padx=10, pady=5, fill="x")
    ctk.CTkLabel(total_frame, text=f"Total Harga: Rp {total_harga}").pack(side="left", anchor="w", padx=10)

tombol_kembali = ctk.CTkButton(master=main_frame, text="Kembali", command=kembali_ke_menu_sebelumnya)
tombol_kembali.pack(side="bottom", pady=10)

root.mainloop()

