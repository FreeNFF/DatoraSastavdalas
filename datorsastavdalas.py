import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


#galvenā loga izveide
logs = Tk()
logs.geometry("340x175")
logs.title("Instrumentu noma")
logs.configure(background="#b3ebf2")

#bildes ievietošana
bilde_frame = tk.Frame(logs)
bilde_frame.grid(row=1, column=0, padx=5, pady=5)
bilde_image =Image.open("images.png")
resized_bilde = bilde_image.resize((150,125))#bildes garums
bilde = ImageTk.PhotoImage(resized_bilde)
bilde_label = ttk.Label(bilde_frame, image=bilde)
bilde_label.grid(row=1, column=0, padx=1, pady=1)

#izveidot pogu
btn=Button(logs, text="Pasūtījums", bd="5", command=lambda: pasutijums())#pievieno komandu, lai atvērtu citu logu
btn1=Button(logs, text="Aizvērt", bd="5", command=logs.destroy)
btn.grid(row=1, column=2, padx=10, pady=1)
btn1.grid(row=1, column=3, padx=10, pady=1)

#funkcija, kas izveido 2. līmeņa logu
def pasutijums():
    logs1 = Toplevel()
    logs1.geometry("350x500")
    logs1.title("Pasūtījums")
    logs1.configure(background="#b3ebf2")

    #teksti
    ttk.Label(logs1, text="Izvēlaties darbinieku:", background="#b3ebf2").grid(row=1, column=0, padx=10, pady=10)
    ttk.Label(logs1, text="Izvēlaties detaļu:", background="#b3ebf2").grid(row=2, column=0, padx=10, pady=10)
    ttk.Label(logs1, text="Norādi cenu:", background="#b3ebf2").grid(row=3, column=0, padx=10, pady=10)
    ttk.Label(logs1, text="Norādiet detaļas skaitu:", background="#b3ebf2").grid(row=4, column=0, padx=10, pady=10)

    #mainīgie
    vardsuzvards = tk.StringVar()
    detala = tk.StringVar()
    cena = tk.StringVar()
    skaits = tk.StringVar()

    #izvēles izveide
    darbinieks = ttk.Combobox(logs1, textvariable=vardsuzvards)
    detalas = ttk.Combobox(logs1, textvariable=detala)
    detalascena = ttk.Combobox(logs1, textvariable=cena)#izvēles logs
    detalasskaits = ttk.Entry(logs1, textvariable=skaits)#ievades logs

    #izvēles vērtības
    darbinieks["values"] = ("Mareks Bahmanis", "Jānis Eglis", "Sergejs Estris", "Juris Kalniņš") 
    detalas["values"] = ("Monitors", "Pelīte", "Klavietūra", "Austiņas")
    detalascena["values"] = ("5", "10", "25", "50", "100", "250", "1000")

    darbinieks.grid(row=1, column=2, padx=10, pady=10)
    detalas.grid(row=2, column=2, padx=10, pady=10)
    detalascena.grid(row=3, column=2, padx=10, pady=10)
    detalasskaits.grid(row=4, column=2, padx=10, pady=10)




logs.mainloop()
