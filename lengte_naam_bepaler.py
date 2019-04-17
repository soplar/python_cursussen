import tkinter as tk
from tkinter import ttk

def bepaalLengte(*args):
    try:
        waarde = naam.get()
        lengte.set(len(waarde))
    except ValueError:
        raise Exception('Geen geldige waarde')

scherm = tk.Tk()
scherm.title('Bepaal het aantal karakters van je naam')

naam = tk.StringVar()
lengte = tk.StringVar()

invoer_veld = ttk.Entry(scherm, textvariable=naam)
invoer_veld.grid(column=1, row=1)

uitvoer_label = ttk.Label(scherm, textvariable=lengte)
uitvoer_label.grid(column=2, row=1)

invoer_veld.focus()

scherm.bind('<Key>', bepaalLengte)
