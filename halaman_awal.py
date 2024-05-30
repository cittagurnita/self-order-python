import csv
from tkinter import ttk
from pathlib import Path
import customtkinter as ctk
from PIL import Image, ImageTk
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")

def menu_list():
    window4 = ctk.CTkToplevel()
    window4.title("WARPAT!")
    window4.geometry('1366x768')
    window4.state('zoomed')
    window4.configure(bg="#fbcd64")
    window4.resizable(True, True)

    bg_welcome = ImageTk.PhotoImage(Image.open("assets/background_menu.png"))
    bgr = ctk.CTkLabel(master=window4, image=bg_welcome, text="")
    bgr.pack()

    def button_dine(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    button_makanan = ctk.CTkImage(Image.open(button_dine("button_makanan.png")), size=(322.38, 61.85))
    button_4 = ctk.CTkButton(
        window4,
        image=button_makanan,
        border_width=0,
        corner_radius=0,
        bg_color="#fbcd64",
        fg_color="#fbcd64",
        hover_color="#fbcd64",
        command=lambda: list_makanan(),  # Hapus window4.destroy() di sini
        text=''
    )
    button_4.place(x=-30, y=190.16)

    button_minuman = ctk.CTkImage(Image.open(button_dine("button_minuman.png")), size=(322.38, 61.85))
    button_5 = ctk.CTkButton(
        window4,
        image=button_minuman,
        border_width=0,
        corner_radius=0,
        bg_color="#fbcd64",
        fg_color="#fbcd64",
        hover_color="#fbcd64",
        command=lambda: subprocess.Popen(["python", "list_minuman.py"]),  # Hapus window4.destroy() di sini
        text=''
    )
    button_5.place(x=-30, y=264.9)

    button_extra = ctk.CTkImage(Image.open(button_dine("button_extra.png")), size=(322.38, 61.85))
    button_6 = ctk.CTkButton(
        window4,
        image=button_extra,
        border_width=0,
        corner_radius=0,
        bg_color="#fbcd64",
        fg_color="#fbcd64",
        hover_color="#fbcd64",
        command=lambda: list_extra(),  # Hapus window4.destroy() di sini
        text=''
    )
    button_6.place(x=-30, y=339.16)

# Fungsi untuk membaca program list_extra.py dan menampilkannya di jendela
def list_extra():
    try:
        window7 = ctk.CTkToplevel()
        window7.title("WARPAT!")
        window7.geometry('1366x768')
        window7.state('zoomed')
        window7.configure(bg="#fbcd64")
        window7.resizable(True, True)

        bg_welcome = ImageTk.PhotoImage(Image.open("assets/background_extra.png"))
        bgr = ctk.CTkLabel(master=window7, image=bg_welcome, text="")
        bgr.pack()

        def button_dine(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        button_back_image = ctk.CTkImage(Image.open(button_dine("button_back.png")), size=(75, 75))
        button_back = ctk.CTkButton(
            window7,
            image=button_back_image,
            border_width=0,
            corner_radius=0,
            bg_color="#fbcd64",
            fg_color="#fbcd64",
            hover_color="#fbcd64",
            command=lambda: window7.destroy(),
            text=''
        )
        button_back.place(x=20, y=20)

        # Fungsi untuk membaca program list_extra.py
        def baca_program(file_path):
            with open(file_path, 'r') as f:
                return f.read()

        # Menambahkan widget teks untuk menampilkan isi program list_extra.py
        text_area = ctk.CTkText(window7, wrap="none", padx=10, pady=10)
        text_area.pack(fill="both", expand=True)
        
        program_text = baca_program("list_extra.py")
        text_area.insert("1.0", program_text)

        window7.mainloop()
    except Exception as e:
        print("Error:", e)

# Fungsi lainnya...
def list_minuman():
    window5 = ctk.CTkToplevel()
    window5.title("WARPAT!")
    window5.geometry('1366x768')
    window5.state('zoomed')
    window5.configure(bg="#fbcd64")
    window5.resizable(True, True)

    def baca_csv(file_path):
        data = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data
    
    def buat_label(frame, text, row, col):
        label = ctk.CTkLabel(master=frame, text=text)
        label.grid(row=row, column=col, padx=10, pady=5, sticky="w")
        return label
    
    main_frame = ctk.CTkFrame(master=window5)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = ctk.CTkCanvas(master=main_frame)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(master=main_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    scrollable_frame = ctk.CTkFrame(master=canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    data_minuman = baca_csv("menu_minuman.csv")

    for i, item in enumerate(data_minuman):
        buat_label(scrollable_frame, item["Menu"], i, 0)
        buat_label(scrollable_frame, item["Harga"], i, 1)

    window5.mainloop()

def list_makanan():
    subprocess.Popen(["python", "list_makanan.py"])

def list_extra():
    window7 = ctk.CTkToplevel()
    window7.title("WARPAT!")
    window7.geometry('1366x768')
    window7.state('zoomed')
    window7.configure(bg="#fbcd64")
    window7.resizable(True, True)

    def baca_csv(file_path):
        data = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data
    
    def buat_label(frame, text, row, col):
        label = ctk.CTkLabel(master=frame, text=text)
        label.grid(row=row, column=col, padx=10, pady=5, sticky="w")
        return label
    
    main_frame = ctk.CTkFrame(master=window7)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = ctk.CTkCanvas(master=main_frame)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(master=main_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    scrollable_frame = ctk.CTkFrame(master=canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    data_makanan = baca_csv("menu_makanan.csv")

    for i, item in enumerate(data_makanan):
        buat_label(scrollable_frame, item["Menu"], i, 0)
        buat_label(scrollable_frame, item["Harga"], i, 1)

    window7.mainloop()

def dine_option():
    window3 = ctk.CTkToplevel()
    window3.title("WARPAT!")
    window3.geometry('1366x768')
    window3.state('zoomed')
    window3.configure(bg="#fbcd64")
    window3.resizable(True, True)

    bg_welcome = ImageTk.PhotoImage(Image.open("assets/background_saji.png"))
    bgr = ctk.CTkLabel(master=window3, image=bg_welcome, text="")
    bgr.pack()

    def button_dine(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    button_image_3 = ctk.CTkImage(Image.open(button_dine("button_makansini.png")), size=(307.36, 214.87))
    button_3 = ctk.CTkButton(
        window3,
        image=button_image_3,
        border_width=0,
        corner_radius=0,
        bg_color="#fbcd64",
        fg_color="#fbcd64",
        hover_color="#fbcd64",
        command=lambda: [window3.destroy(), menu_list()],
        text=''
    )
    button_3.place(x=310.0, y=250.0)

    button_image_4 = ctk.CTkImage(Image.open(button_dine("button_bungkus.png")), size=(307.36, 214.87))
    button_4 = ctk.CTkButton(
        window3,
        image=button_image_4,
        border_width=0,
        corner_radius=0,
        bg_color="#fbcd64",
        fg_color="#fbcd64",
        hover_color="#fbcd64",
        command=lambda: [window3.destroy(), menu_list()],
        text=''
    )
    button_4.place(x=650.0, y=250.0)

    window3.mainloop()

def halaman_nama():
    window2 = ctk.CTkToplevel()
    window2.title("WARPAT!")
    window2.geometry('1366x768')
    window2.state('zoomed')
    window2.configure(bg="#fbcd64")
    window2.resizable(True, True)

    bg_welcome = ImageTk.PhotoImage(Image.open("assets/background_nama.png"))
    bgr = ctk.CTkLabel(master=window2, image=bg_welcome, text="")
    bgr.pack()

    entry_nama = ctk.CTkEntry(
        window2,
        placeholder_text="Masukkan Nama Anda",
        height=58.1,
        width=791,
        font=("Helvetica", 18),
        corner_radius=15,
        text_color='#FFFFFF',
        placeholder_text_color="#C7411E",
        fg_color=("#F28743","#C7411E"),
        bg_color="#fbcd64"
    )
    entry_nama.place(x=240, y=300)

    def button_nama(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    button_masuk_img = ctk.CTkImage(Image.open(button_nama("button_masuk.png")), size=(147.29, 53.97))
    button_2 = ctk.CTkButton(
        window2,
        image=button_masuk_img,
        width=147.29,
        height=53.97,
        border_width=0,
        corner_radius=0,
        bg_color="#48775D",
        fg_color="#48775D",
        hover_color="#48775D",
        command=lambda: [window2.destroy(), dine_option()],
        text=''
    )
    button_2.place(x=1100.0, y=665.0)

    window2.mainloop()

def halaman_awal():
    window = ctk.CTk()
    window.title("WARPAT!")
    window.geometry('1366x768')
    window.state('zoomed')
    window.configure(bg="#fbcd64")
    window.resizable(True, True)

    bg_welcome = ImageTk.PhotoImage(Image.open("assets/background_welcome.png"))
    bgr = ctk.CTkLabel(master=window, image=bg_welcome, text="")
    bgr.pack()

    def button_welcome(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    button_start_image = ctk.CTkImage(Image.open(button_welcome("button_start.png")), size=(68.96, 68.96))
    button_1 = ctk.CTkButton(
        window,
        image=button_start_image,
        width=60,
        height=68.96,
        border_width=0,
        corner_radius=0,
        bg_color="#fbcd64",
        fg_color="#fbcd64",
        hover_color="#fbcd64",
        command=lambda: [window.destroy(), halaman_nama()],
        text=''
    )
    button_1.place(x=610.0, y=560.0)

    window.mainloop()

halaman_awal()
