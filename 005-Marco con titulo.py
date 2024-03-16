import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("1280x720")
ventana.title("Programa de gestión v0.1")

tablas = ttk.LabelFrame(ventana,text="Tablas",borderwidth=1,relief="ridge")
tablas.grid(row=0,column=0)

tk.Button(tablas,text="Tabla 1").pack(padx=10,pady=10)
tk.Button(tablas,text="Tabla 2").pack(padx=10,pady=10)
tk.Button(tablas,text="Tabla 3").pack(padx=10,pady=10)
tk.Button(tablas,text="Tabla 4").pack(padx=10,pady=10)
tk.Button(tablas,text="Tabla 5").pack(padx=10,pady=10)

ventana.mainloop()
