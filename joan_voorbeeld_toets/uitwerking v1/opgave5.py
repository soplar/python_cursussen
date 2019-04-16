import tkinter as tk

def maak_groen():
    root["bg"] = "green"
def maak_blauw():
    root["bg"] = "blue"


root = tk.Tk()
root.geometry("300x200")
knop1 = tk.Button(root, text = "groen", command = maak_groen)
knop1.pack()
knop2 = tk.Button(root, text = "blauw", command = maak_blauw)
knop2.pack()

root.mainloop()
