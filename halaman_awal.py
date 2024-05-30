from pathlib import Path
from tkinter import *
import tkinter as tk
from tkinter import Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\SELF ORDER MACHINE\assets")

def halaman_awal():
    window = tk.Tk()
    window.title("WARPAT!")
    window.geometry('1200x675')
    window.configure(bg="#FFFFFF")
    window.resizable(True,True)

    frame = Frame(window, width=1200, height=410, bg='#48775d')
    frame.place(x=0, y=600)

    frame = Frame(window, width=1200, height=850, bg='#fbcd64')
    frame.place(x=0, y=-250)
    
    frame = Frame(window, width=1200, height=370, bg='#c7411e')
    frame.place(x=0, y=-300)
    
    
    heading = Label(text="Selamat Datang", fg="#000000", bg="#fbcd64", font=("Monserrat",40,"bold"))
    heading.place(x=390,y=200)
    
    heading = Label(text="di", fg="#000000", bg="#fbcd64", font=("Monserrat",40,"bold"))
    heading.place(x=560,y=260)
    
    heading = Label(text="WARPAT!", fg="#000000", bg="#fbcd64", font=("Monserrat",40,"bold"))
    heading.place(x=460,y=330)

    def button_start(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    button_image_1 = PhotoImage(
    file=button_start("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        bg="#fbcd64",
        highlightthickness=0,
        command=dine_option(),
        relief="flat"
    )
    button_1.place(
        x=520.0,
        y=420.0,
        width=110.0,
        height=35.0
    )

def dine_option():
    window2 = tk.Tk()
    window2.title("WARPAT!")
    window2.geometry('1200x675')
    window2.configure(bg="#FFFFFF")
    window2.resizable(True,True)

    heading = Label(text="Pilih Penyajian", fg="#000000", bg="#FFFFFF", font=("Monserrat",40,"bold"))
    heading.place(x=470,y=200)

        
    

    window.mainloop()

halaman_awal()