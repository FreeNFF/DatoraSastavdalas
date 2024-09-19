import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


#galvenā loga izveide
logs = Tk()
logs.geometry("350x400")
logs.title("Instrumentu noma")
logs.configure(background="#b3ebf2")

bilde_frame = tk.Frame(logs)
bilde_frame.grid(row=6, column=0)
bilde_image =Image.open("images.png")
resized_bilde = bilde_image.resize((150,125))
bilde = ImageTk.PhotoImage(resized_bilde)
bilde_label = ttk.Label(bilde_frame, image=bilde)
bilde_label.grid(row=6, column=0)

#izveidot pogu







logs.mainloop()
