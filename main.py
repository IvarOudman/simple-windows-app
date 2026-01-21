import tkinter as tk
from tkinter import messagebox

def knop_klik():
    messagebox.showinfo("Hallo", "Je hebt op de knop geklikt!")

root = tk.Tk()
root.title("Mijn eerste app")
root.geometry("300x150")

label = tk.Label(root, text="Dit is mijn Windows app")
label.pack(pady=10)

knop = tk.Button(root, text="Klik mij", command=knop_klik)
knop.pack()

root.mainloop()
