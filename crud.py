import tkinter as tk
from classes_met_arg import Persoon
from tkinter import ttk

from mysql_connectie import MySQL

conn = MySQL('personen')

def vul_listbox():
    data = conn.query_met_data('SELECT * FROM persoon')

    for rij in data:
        
        p = Persoon(rij['naam'], str(rij['geboortedatum']), rij['geslacht'], rij['bsn'])

        lb.insert(tk.END, p)

def delete_rij(*args):
    geselecteerd = lb.curselection()
    lb.delete(geselecteerd)

def insert_rij(*args):
    p = Persoon(naam.get(), geboorte.get(), geslacht.get(), bsn.get())
    conn.query(f'''INSERT INTO persoon
                   VALUES ('{naam.get()}','{geboorte.get()}','{geslacht.get()}','{bsn.get()}')''')
    
    lb.insert(tk.END, p)
    vul_listbox()

def create_rij(*args):
    create_scherm = tk.Toplevel(scherm)
    
    attributen = ['Naam','Geboortedatum','Geslacht','Bsn']
    variabelen = [naam, geboorte, geslacht, bsn]
    
    for index, attribuut in enumerate(attributen):
        
        ttk.Label(create_scherm, text=f'{attribuut}:').grid(row=index+1,column=1)
        ttk.Entry(create_scherm, textvariable=variabelen[index]).grid(row=index+1, column=2)
        
    tk.Button(create_scherm, text='Insert', command=insert_rij).grid(row=len(attributen)+1, column=2)
    
scherm = tk.Tk()

naam = tk.StringVar()
geboorte = tk.StringVar()
geslacht = tk.StringVar()
bsn = tk.StringVar()

lb = tk.Listbox(scherm, width=50, height=5)
lb.grid(row=1, column=1)
   

btn_delete = ttk.Button(scherm, width=10, text='Delete', command=delete_rij)
btn_delete.grid(row=2, column=2)

btn_create = ttk.Button(scherm, width=10, text='Create', command=create_rij)
btn_create.grid(row=2, column=3)

btn_select = ttk.Button(scherm, width=10, text='Select')
btn_select.grid(row=3, column=2)

btn_update = ttk.Button(scherm, width=10, text='Update')
btn_update.grid(row=3, column=3)

vul_listbox()
