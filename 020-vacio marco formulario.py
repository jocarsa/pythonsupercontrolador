import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import mysql.connector

def seleccionaTabla(nombretabla):
    global datos
    global formulario
    global marcoformulario
    datos.configure(text="Datos: "+nombretabla)
    formulario.configure(text="Fornulario: "+nombretabla)
    print("has hecho click en un boton",nombretabla)
    for widgets in marcoformulario.winfo_children():
        widgets.destroy()
    cursor.execute("SHOW COLUMNS FROM "+nombretabla)
    campos = cursor.fetchall()
    for campo in campos:
        print(campo[0])
    

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

marco = tk.Frame(ventana, width=1280, height=720, bg="red")
marco.pack(padx=10, pady=10)

# LISTADO DINÁMICO DE LAS TABLAS DE LA BASE DE DATOS #########################

tablas = ttk.LabelFrame(marco, text="Tablas", borderwidth=1, relief="ridge")
tablas.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)

cursor.execute("SHOW tables IN gestionempresarial")
listadotablas = cursor.fetchall()
for tabla in listadotablas:
    nombretabla = tabla[0]
    tk.Button(tablas, text=nombretabla,command=lambda nombretabla = nombretabla: seleccionaTabla(nombretabla)).pack(padx=5, pady=5)

# DATOS QUE CONTIENE LA TABLA SELECCIONADA ###################################

datos = ttk.LabelFrame(marco, text="Datos", borderwidth=1, relief="ridge")
datos.grid(row=0, column=1, sticky="nsew",padx=10,pady=10)
tk.Label(datos, text="Aquí ponemos los datos").pack(padx=10, pady=10)

# FORMULARIO DE DATOS DEL CAMPO SELECCIONADO #################################

formulario = ttk.LabelFrame(marco, text="Formulario", borderwidth=1, relief="ridge")
formulario.grid(row=0, column=2, sticky="nsew",padx=10,pady=10)
marcoformulario = tk.Frame(formulario)
marcoformulario.pack()

labelcampo1 = ttk.LabelFrame(marcoformulario, text="Campo1", borderwidth=1, relief="ridge")
labelcampo1.pack(padx=5,pady=5)
entrada1 = ttk.Entry(labelcampo1)
entrada1.pack(padx=5,pady=5)
labelcampo1 = ttk.LabelFrame(marcoformulario, text="Campo1", borderwidth=1, relief="ridge")
labelcampo1.pack(padx=5,pady=5)
entrada1 = ttk.Entry(labelcampo1)
entrada1.pack(padx=5,pady=5)
labelcampo1 = ttk.LabelFrame(marcoformulario, text="Campo1", borderwidth=1, relief="ridge")
labelcampo1.pack(padx=5,pady=5)
entrada1 = ttk.Entry(labelcampo1)
entrada1.pack(padx=5,pady=5)
labelcampo1 = ttk.LabelFrame(marcoformulario, text="Campo1", borderwidth=1, relief="ridge")
labelcampo1.pack(padx=5,pady=5)
entrada1 = ttk.Entry(labelcampo1)
entrada1.pack(padx=5,pady=5)
botonenviar = tk.Button(formulario,text="Enviar")
botonenviar.pack(padx=5,pady=5)

# Set column and row weights to distribute the space
marco.grid_columnconfigure(0, weight=10)
marco.grid_columnconfigure(1, weight=80)
marco.grid_columnconfigure(2, weight=10)
marco.grid_rowconfigure(0, weight=1)

ventana.mainloop()
