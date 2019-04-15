from tkinter import *
from tkinter import ttk
root = Tk()
l =ttk.Label(root, text="Probeer hier allerlei klik events")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text='Muis bewoog naar binnen'))
l.bind('<Leave>', lambda e: l.configure(text='Muis bewoog naar buiten'))
l.bind('<1>', lambda e: l.configure(text='Op de linkermuisknop geklikt'))
l.bind('<Double-1>', lambda e: l.configure(text='Je hebt gedubbelklikt'))
l.bind('<B3-Motion>', lambda e: l.configure(text='Rechtermuisknop ingehouden %d,%d' % (e.x, e.y)))
root.mainloop()
