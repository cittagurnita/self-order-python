from tkinter import Tk, Label, Frame
import tkinter as tk

def nota_pembelian():
    window = tk.Tk()  
    window.title("WARPAT")
    window.geometry("300x700")
    window.configure(bg="white")
    window.resizable(True, True)

    heading = Label(text="WARPAT", bg="white", fg="black", font=("Helvetica", 16))
    heading.place(x=105, y=2)
    heading = Label(text="Surakarta, Jawa Tengah, Indonesia", bg="white", fg="black", font=("Helvetica", 10))
    heading.place(x=45, y=30)
    heading = Label(text="08112651176", bg="white", fg="black", font=("Helvetica", 10))
    heading.place(x=100, y=50)
    heading = Label(text="NOTA PEMBELIAN", bg="white", fg="black", font=("Helvetica", 10, "bold"))
    heading.place(x=90, y=80)
    heading = Label(text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", bg="white", fg="black", font=("Helvetica", 10, "bold"))
    heading.place(x=15, y=100)
    heading = Label(text="hari dan jam?", bg="white", fg="black", font=("Helvetica", 10))
    heading.place(x=15, y=120)
    heading = Label(text="import random antrian", bg="white", fg="black", font=("Helvetica", 10))
    heading.place(x=160, y=120)
    heading = Label(text="USER", bg="white", fg="black", font=("Helvetica", 10))
    heading.place(x=15, y=140)
    heading = Label(text="namanya", bg="white", fg="black", font=("Helvetica", 10))
    heading.place(x=160, y=140)
    heading = Label(text="TYPE", bg="white", fg="black", font=("Helvetica", 10))
    heading.place(x=15, y=160)
    heading = Label(text="metode bayar", bg="white", fg="black", font=("Helvetica", 10))
    heading.place(x=160, y=160)
    window.mainloop()

nota_pembelian()




