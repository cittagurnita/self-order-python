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
    with open("order_makan.csv", "w", newline='', encoding='utf-8') as csvfile:  # Ubah nama file menjadi 'order_makan.csv'
        fieldnames = ['Menu', 'Jumlah', 'Harga']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for menu, jumlah, harga in order_details:
            writer.writerow({'Menu': menu, 'Jumlah': jumlah, 'Harga': harga})

    messagebox.showinfo("Pesanan Disimpan", "Pesanan telah disimpan ke file order_makan.csv")  # Ubah pesan dialog
    exit()  # Keluar dari program setelah menyimpan pesanan

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
        for item in data_makanan:  # Ubah 'data_minuman' menjadi 'data_makanan'
            if item["Nama Menu"] == menu:
                harga = int(item["Harga"]) * jumlah
                total_harga += harga
                frame = ctk.CTkFrame(master=order_frame)
                frame.pack(anchor="w", padx=10, pady=5, fill="x")
                ctk.CTkLabel(frame, text=f"{menu} (x{jumlah}): Rp {harga}").pack(side="left", anchor="w", padx=10)
                button_kurangi = ctk.CTkButton(frame, text="Kurangi", command=lambda item=menu: kurangi_pesanan(item, pesanan), width=7, height=2)
                button_kurangi.pack(side="right", anchor="e", padx=10)

    ctk.CTkLabel(order_frame, text=f"Total Harga: Rp {total_harga}").pack(anchor="w", padx=10, pady=5)
    return total_harga

def get_order_summary():
    total_harga = 0
    order_details = []
    for menu, jumlah in pesanan.items():
        for item in data_makanan:  # Ubah 'data_minuman' menjadi 'data_makanan'
            if item["Nama Menu"] == menu:
                harga = int(item["Harga"]) * jumlah
                total_harga += harga
                order_details.append((menu, jumlah, harga))
    return order_details

root = ctk.CTk()
root.title("Daftar Makanan")  # Ubah judul menjadi "Daftar Makanan"
root.geometry("1366x768")

# Create a frame for the scrollable menu on the left side
menu_frame = ctk.CTkFrame(master=root)
menu_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Remove background image and canvas, making background plain
canvas = ctk.CTkCanvas(master=menu_frame)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(master=menu_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = ctk.CTkFrame(master=canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame for the order summary on the right side
order_frame = ctk.CTkFrame(master=root, width=300)  
order_frame.pack(side="right", fill="y", padx=10, pady=10, anchor="n")  

data_makanan = baca_csv("menu_makan.csv")  # Ubah 'menu_minum.csv' menjadi 'menu_makan.csv'

pesanan = {}  

# Display the order summary in a label
order_summary_label = ctk.CTkLabel(master=order_frame, text="", justify="left")
order_summary_label.pack(anchor="w", padx=10, pady=5)

for i, item in enumerate(data_makanan):  # Ubah 'data_minuman' menjadi 'data_makanan'
    label_menu = ctk.CTkLabel(master=scrollable_frame, text=item["Nama Menu"])
    label_menu.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

    entry_kuantitas = ctk.CTkEntry(master=scrollable_frame, width=50, font=("Helvetica", 14))
    entry_kuantitas.grid(row=i + 1, column=1, padx=5, pady=5, sticky="w")
    entry_kuantitas.insert(0, "0")

    button_tambah = ctk.CTkButton(master=scrollable_frame, text="+", font=("Helvetica", 10), command=lambda entry=entry_kuantitas: tambah_jumlah(entry), width=30, height=2)
    button_tambah.grid(row=i + 1, column=2, padx=5, pady=5, sticky="w")

    button_kurangi = ctk.CTkButton(master=scrollable_frame, text="-", font=("Helvetica", 10), command=lambda entry=entry_kuantitas: kurangi_jumlah(entry), width=30, height=2)
    button_kurangi.grid(row=i + 1, column=3, padx=5, pady=5, sticky="w")

    button_pesan = ctk.CTkButton(master=scrollable_frame, text="Pesan", command=lambda item=item["Nama Menu"], entry=entry_kuantitas: pesan(item, int(entry.get()), pesanan))
    button_pesan.grid(row=i + 1, column=4, padx=10, pady=5, sticky="w")

# Button to save the order to a file
button_simpan = ctk.CTkButton(master=root, text="Simpan Pesanan", command=lambda: simpan_pesanan(pesanan))
button_simpan.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
