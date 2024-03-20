import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import mysql.connector
from tkinter import messagebox

listacampos = []
tablaactual = None
id_actual = None

def eliminarRegistro():
    print("eliminamos el registro que estuviera seleccionado")
    print("el id actual es ",id_actual)
    print("La tabla seleccionada es: ",tablaactual)
    peticion = "DELETE FROM "+tablaactual+" WHERE Identificador = "+str(id_actual)+""
    print(peticion)
    cursor.execute(peticion)
    conexion.commit()
    refrescaTabla(tablaactual)

def seleccionaArbol(event):
    global id_actual
    seleccionado = arbol.selection()[0]
    id_seleccionado = arbol.item(seleccionado)['values'][0]
    id_actual = id_seleccionado

def enviaFormulario():
    envias = 0
    print("Voy a enviar el formulario")
    print(listacampos)
    peticion = "INSERT INTO "+tablaactual+" VALUES(NULL,"
    for uncampo in listacampos:
        if uncampo.get() == "":
            envias += 1
        print(uncampo.get())
        peticion += "'"+uncampo.get()+"',"
    peticion = peticion[:-1]
    peticion += ")";
    print(peticion)
    if envias == 0:
        cursor.execute(peticion)
        conexion.commit()
        messagebox.showinfo("Éxito:","Registro insertado correctamente")
        for entrada in listacampos:
            entrada.delete(0,tk.END)
    else:
        messagebox.showinfo("Error:","Debes completar todos los campos")
    refrescaTabla(tablaactual)

def refrescaTabla(nombretabla):
    global arbol
    arbol.delete(*arbol.get_children())
    arbol['columns'] = ()
    for col in arbol['columns']:
        arbol.heading(col, text="")
    cursor.execute("SHOW COLUMNS FROM " + nombretabla)
    campos = cursor.fetchall()
    arbol['columns'] = [campo[0] for campo in campos]
    for campo in campos:
        arbol.column(campo[0], width=200)
        arbol.heading(campo[0], text=campo[0])
    cursor.execute("SELECT * FROM "+tablaactual)
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)
        arbol.insert("",tk.END,text="1",values=registro)

def seleccionaTabla(nombretabla):
    global listacampos
    global datos
    global formulario
    global marcoformulario
    global tablaactual
    global arbol
    
    tablaactual = nombretabla
    listacampos = []
    datos.configure(text="Datos: " + nombretabla)
    formulario.configure(text="Formulario: " + nombretabla)
    for widget in marcoformulario.winfo_children():
        widget.destroy()
    cursor.execute("SHOW COLUMNS FROM "+nombretabla)
    campos = cursor.fetchall()
    for campo in campos:
        if campo[0] != "Identificador":
            print(campo[0])
            labelcampo1 = ttk.LabelFrame(marcoformulario, text=campo[0], borderwidth=1, relief="ridge")
            labelcampo1.pack(padx=5,pady=5)
            listacampos.append(ttk.Entry(labelcampo1))
            listacampos[-1].pack(padx=5,pady=5)
    refrescaTabla(nombretabla)        
    
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
style = Style(theme="cosmo")



# LISTADO DINÁMICO DE LAS TABLAS DE LA BASE DE DATOS #########################

tablas = ttk.LabelFrame(ventana, text="Tablas", borderwidth=1, relief="ridge")
tablas.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)

cursor.execute("SHOW tables IN gestionempresarial")
listadotablas = cursor.fetchall()
for tabla in listadotablas:
    nombretabla = tabla[0]
    tk.Button(tablas, text=nombretabla,command=lambda nombretabla = nombretabla: seleccionaTabla(nombretabla),width=20).pack(padx=5, pady=5)

# DATOS QUE CONTIENE LA TABLA SELECCIONADA ###################################

datos = ttk.LabelFrame(ventana, text="Datos", borderwidth=1, relief="ridge",width=200)
datos.grid(row=0, column=1, sticky="nsew",padx=10,pady=10)

arbol = ttk.Treeview(datos)
arbol.pack(padx=10,pady=10,fill="both",expand=True)
arbol['columns'] = ("nombre","email","telefono")
arbol.column("#0",width=200)
arbol.column("nombre",width=200)
arbol.column("email",width=200)
arbol.column("telefono",width=200)
arbol.heading("#0",text="id")
arbol.heading("nombre",text="nombre")
arbol.heading("email",text="email")
arbol.heading("telefono",text="telefono")

arbol.insert("",tk.END,text="1",values=("Jose Vicente","info@jocarsa.com","1235"))

arbol.bind("<<TreeviewSelect>>",seleccionaArbol)

# FORMULARIO DE DATOS DEL CAMPO SELECCIONADO #################################

formulario = ttk.LabelFrame(ventana, text="Formulario", borderwidth=1, relief="ridge")
formulario.grid(row=0, column=2, sticky="nsew",padx=10,pady=10)

boton_eliminar = tk.Button(formulario,text="Eliminar",command=eliminarRegistro)
boton_eliminar.pack(padx=5,pady=5)

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
botonenviar = tk.Button(formulario,text="Enviar",command=enviaFormulario)
botonenviar.pack(padx=5,pady=5)

ventana.grid_columnconfigure(0, weight=10)
ventana.grid_columnconfigure(1, weight=80)
ventana.grid_columnconfigure(2, weight=10)
ventana.grid_rowconfigure(0, weight=1)

ventana.mainloop()
