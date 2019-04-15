import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        raise Exception('Geen geldige waarde')
    
root = tk.Tk()
root.title("Feet to Meters")

feet = tk.StringVar()
meters = tk.StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1)

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2)
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3)

ttk.Label(mainframe, text="feet").grid(column=3, row=1)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2)
ttk.Label(mainframe, text="meters").grid(column=3, row=2)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
