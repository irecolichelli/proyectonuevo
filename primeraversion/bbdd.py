import sqlite3
#PARA QUE ME MUESTRE EL INVENTARIO
def obtener_inventario():
    try:
        conexion_inventario = sqlite3.connect('BBDDCajaNegocio.db')
        cursor_inventario = conexion_inventario.cursor()
        cursor_inventario.execute('SELECT * FROM INVENTARIO')
        datos_inventario = cursor_inventario.fetchall()
        conexion_inventario.close()
        return datos_inventario
    except sqlite3.Error as error:
        print("Error en la BBDD:", error)
        return []

def basededatos(articulo, valor, proveedor, stock, fecha, total, medio):
    try:
        conexion_inventario = sqlite3.connect('BBDDCajaNegocio.db')
        cursor_inventario = conexion_inventario.cursor()
        cursor_inventario.execute('''
            CREATE TABLE IF NOT EXISTS INVENTARIO (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                ARTICULO VARCHAR (50),
                VALOR INTEGER (50),
                PROVEEDOR VARCHAR (50),
                STOCK VARCHAR (50)
            )
            ''')
        cursor_inventario.execute('''
            INSERT INTO INVENTARIO (ARTICULO, VALOR, PROVEEDOR, STOCK)
            VALUES (?, ?, ?, ?)
        ''', (articulo, valor, proveedor, stock))

        conexion_inventario.commit()
        conexion_inventario.close()

        conexion_ventas = sqlite3.connect('BBDDCajaNegocio.db')
        cursor_ventas = conexion_ventas.cursor()
        cursor_ventas.execute('''
            CREATE TABLE IF NOT EXISTS VENTAS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                FECHA INTEGER(50),
                TOTAL INTEGER(50),
                MEDIO_DE_PAGO VARCHAR(50)
            )
        ''')
        cursor_ventas.execute('''
            INSERT INTO VENTAS (FECHA, TOTAL, MEDIO_DE_PAGO)
            VALUES (?, ?, ?)
        ''', (fecha, total, medio))

        conexion_ventas.commit()
        conexion_ventas.close()
    except sqlite3.Error as error:
        print("Error en la BBDD:", error)