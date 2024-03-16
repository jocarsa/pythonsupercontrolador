import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="gestionempresarial",
    password="gestionempresarial",
    database="gestionempresarial"
    )

cursor = conexion.cursor()

ventana = tk.Tk()
ventana.geometry("1280x720")
ventana.title("Programa de gestión v0.1")

# LISTADO DINÁMICO DE LAS TABLAS DE LA BASE DE DATOS #########################

tablas = ttk.LabelFrame(ventana, text="Tablas", borderwidth=1, relief="ridge")
tablas.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)

cursor.execute("SHOW tables IN gestionempresarial")
listadotablas = cursor.fetchall()
for tabla in listadotablas:
    tk.Button(tablas, text=tabla[0]).pack(padx=10, pady=10)

# DATOS QUE CONTIENE LA TABLA SELECCIONADA ###################################

datos = ttk.LabelFrame(ventana, text="Datos", borderwidth=1, relief="ridge")
datos.grid(row=0, column=1, sticky="nsew",padx=10,pady=10)
tk.Label(datos, text="Aquí ponemos los datos").pack(padx=10, pady=10)

# FORMULARIO DE DATOS DEL CAMPO SELECCIONADO #################################

formulario = ttk.LabelFrame(ventana, text="Formulario", borderwidth=1, relief="ridge")
formulario.grid(row=0, column=2, sticky="nsew",padx=10,pady=10)
tk.Label(formulario, text="Aquí ponemos el formulario").pack(padx=10, pady=10)

ventana.grid_columnconfigure(0, weight=10)
ventana.grid_columnconfigure(1, weight=80)
ventana.grid_columnconfigure(2, weight=10)
ventana.grid_rowconfigure(0, weight=1)

ventana.mainloop()
