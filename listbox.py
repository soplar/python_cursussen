import tkinter as tk

master = tk.Tk()

listbox = tk.Listbox(master)
listbox.pack()

listbox.insert(tk.END)

for item in ["one", "two", "three", "four"]:
    listbox.insert(tk.END, item)

tk.mainloop()
