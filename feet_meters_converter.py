import tkinter as tk
from tkinter import ttk


def calculate(*args):
    print(args)
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        raise Exception('Geen geldige waarde')
    
scherm = tk.Tk() # constructor
scherm.title("Feet to Meters")

feet = tk.StringVar()
meters = tk.StringVar()

mainframe = ttk.Frame(scherm, padding="3 3 12 12")
mainframe.grid(column=0, row=0)

invoer_veld = ttk.Entry(mainframe, width=7, textvariable=feet)
invoer_veld.grid(column=2, row=1)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3)

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2)

ttk.Label(mainframe, text="feet").grid(column=3, row=1)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2)
ttk.Label(mainframe, text="meters").grid(column=3, row=2)

invoer_veld.focus()
scherm.bind('<Return>', calculate)

scherm.mainloop()
