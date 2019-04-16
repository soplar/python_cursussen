# importeer de tkinter functies
import tkinter as tk
# maak het formulier
root = tk.Tk()
# bepaal de grootte van het formulier
root.geometry("300x200")
# verander de titel van het venster
root.title("Mijn naam")
# maak een button en plaats het op het formulier
tk.Button(root, text = "klik hier").pack()
# maak een invoerveld en plaats het op het formulier
tk.Entry(root).pack()
# maak een checkbox en plaats het op het formulier
tk.Checkbutton(root, text = "aanwezig").pack()
root.mainloop()
