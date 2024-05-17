from pathlib import Path
from tkinter import *
import tkinter as tk
from tkinter import Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\SELF ORDER MACHINE\assets")

def halaman_awal():
    window = tk.Tk()
    window.title("Welcome!")
    window.geometry('1200x675')
    window.configure(bg="#FFFFFF")
    window.resizable(True,True)

    heading = Label(text="Welcome", fg="#000000", bg="#FFFFFF", font=("Monserrat",40,"bold"))
    heading.place(x=470,y=200)
    
    heading = Label(text="to WARPAT!", fg="#000000", bg="#FFFFFF", font=("Monserrat",40,"bold"))
    heading.place(x=435,y=260)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=530.0,
        y=370.0,
        width=130.0,
        height=50.0
    )
    

    window.mainloop()

halaman_awal()