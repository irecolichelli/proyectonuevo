from tkinter import *
from bbdd import basededatos

root = Tk()
miFrame = Frame(root, width=1200, height=600)
miFrame.pack()
# Variables para almacenar la información
fecha = StringVar()
totalventa = IntVar()
mediopago = StringVar()

# -----------CREAR ENTRYS Y LABEL PARA VENTAS---------->

labelfecha = Label(miFrame, text="Ingrese la fecha:").grid(row=0, column=1, padx=10, pady=10)
entry_fecha = Entry(miFrame, textvariable=fecha)
entry_fecha.grid(row=0, column=2, padx=10, pady=10)

labeltotal = Label(miFrame, text="Total vendido:").grid(row=1, column=1, padx=10, pady=10)
entry_total = Entry(miFrame, textvariable=totalventa)
entry_total.grid(row=1, column=2, padx=10, pady=10)

labelmedio = Label(miFrame, text="Medio de pago:").grid(row=2, column=1, padx=10, pady=10)
entry_medio = Entry(miFrame, textvariable=mediopago)
entry_medio.grid(row=2, column=2, padx=10, pady=10)

Button(miFrame, text="Guardar en BBDD", command=lambda: guardar_venta()).grid(row=8, column=4, padx=10, pady=10)

Button(miFrame, text="Cerrar", command=root.destroy).grid(row=8, column=5, padx=10, pady=10)


def guardar_venta():
    basededatos(
        "",
        "",
        "",
        "",
        fecha.get(),
        totalventa.get(),
        mediopago.get()
    )
    # Limpiar los campos de entrada después de guardar en la base de datos
    entry_fecha.delete(0, END)
    entry_total.delete(0, END)
    entry_medio.delete(0, END)



def abrir_ventana_inventario():
    ventana_inventario = Toplevel(root)
    ventana_inventario.title("Inventario")

    # -----------------CREAR LABELS Y ENTRY PARA INVENTARIO-------->
    label_art = Label(ventana_inventario, text="Ingrese nuevo articulo:").grid(row=4, column=2, padx=10, pady=10)
    entry_art = Entry(ventana_inventario)
    entry_art.grid(row=4, column=3, padx=10, pady=10)

    label_valor = Label(ventana_inventario, text="Ingrese valor del artículo").grid(row=5, column=2, padx=10, pady=10)
    entry_valor = Entry(ventana_inventario)
    entry_valor.grid(row=5, column=3, padx=10, pady=10)

    label_proveedor = Label(ventana_inventario, text="Proveedor: ").grid(row=6, column=2, padx=10, pady=10)
    entry_proveedor = Entry(ventana_inventario)
    entry_proveedor.grid(row=6, column=3, padx=10, pady=10)

    label_stock = Label(ventana_inventario, text="Cantidad: ").grid(row=7, column=2, padx=10, pady=10)
    entry_stock = Entry(ventana_inventario)
    entry_stock.grid(row=7, column=3, padx=10, pady=10)

    def guardar_inventario():
        basededatos(
            entry_art.get(),
            entry_valor.get(),
            entry_proveedor.get(),
            entry_stock.get(),
            "",
            "",
            ""
        )
        entry_art.delete(0, END)
        entry_valor.delete(0, END)
        entry_proveedor.delete(0, END)
        entry_stock.delete(0, END)
    # Botones para guardar y cerrar la ventana del inventario
    Button(ventana_inventario, text="Guardar en inventario", command=lambda: guardar_inventario()).grid(row=8, column=4, padx=10, pady=10)
    Button(ventana_inventario, text="Cerrar", command=root.destroy).grid(row=8, column=5, padx=10, pady=10)

#---------------->>>>>>MOSTRAR INVENTARIO FUNCION<<<<<<<<<<<<<<<<<----------------

# ------------------------------------------->>>>>CREACIÓN DE MENÚS<<<<<<<<---------------------------------------------------------------
barra = Menu(root)
root.config(menu=barra, width=300, height=300)
settings = Menu(barra, tearoff=0)
settings.add_command(label="Añadir stock", command=abrir_ventana_inventario)
settings.add_command(label="Ver inventario")
settings.add_separator()
settings.add_command(label="SALIR")
barra.add_cascade(label="INVENTARIO", menu=settings)
'''
#SUBMENU
submenu= Menu(settings)
submenu.add_command(label="No vas a ver nada JAJA")
submenu.add_command(label="Como cuando no viste que te gorreaban")
settings.add_cascade(label="INventa", menu=submenu)
herramientas=Menu(barra)
herramientas.add_command(label="Buena música", command=)
herramientas.add_command(label="Buen momento", command=)
herramientas.add_command(label="Buena compra", command=)
herramientas.add_command(label="Buena persona", command=)
helpme=Menu(barra)
helpme.add_command(label="Buscar ayuda en Google", command=abrirgoogle)
helpme.add_command(label="Contactar servicio técnico")
helpme.add_separator()
helpme.add_command(label="Bot de ayuda", command=infoadicional) #------------------VENTANA EMERGENTE PUESTA EN EL COMANDO
#COMANDOS DE LOS MENUS
barra.add_cascade(label="Settings", menu=settings)
barra.add_cascade(label="WIBUR", menu=edicion)
barra.add_cascade(label="Cosas buenas", menu=herramientas)
barra.add_cascade(label="Help", menu=helpme)
'''

root.mainloop()
