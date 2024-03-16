import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

ventana = tk.Tk()
ventana.geometry("1280x720")
ventana.title("Programa de gestión v0.1")

tablas = ttk.LabelFrame(ventana, text="Tablas", borderwidth=1, relief="ridge")
tablas.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)

tk.Button(tablas, text="Tabla 1").pack(padx=10, pady=10)
tk.Button(tablas, text="Tabla 2").pack(padx=10, pady=10)
tk.Button(tablas, text="Tabla 3").pack(padx=10, pady=10)
tk.Button(tablas, text="Tabla 4").pack(padx=10, pady=10)
tk.Button(tablas, text="Tabla 5").pack(padx=10, pady=10)

datos = ttk.LabelFrame(ventana, text="Datos", borderwidth=1, relief="ridge")
datos.grid(row=0, column=1, sticky="nsew",padx=10,pady=10)
tk.Label(datos, text="Aquí ponemos los datos").pack(padx=10, pady=10)

formulario = ttk.LabelFrame(ventana, text="Formulario", borderwidth=1, relief="ridge")
formulario.grid(row=0, column=2, sticky="nsew",padx=10,pady=10)
tk.Label(formulario, text="Aquí ponemos el formulario").pack(padx=10, pady=10)

ventana.grid_columnconfigure(0, weight=10)
ventana.grid_columnconfigure(1, weight=80)
ventana.grid_columnconfigure(2, weight=10)
ventana.grid_rowconfigure(0, weight=1)

ventana.mainloop()
