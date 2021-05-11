def Numero_Menu():
    digito = False
    num = 0    

    while (not digito):
        try:
            num = int(input("Introduce un numero entero: "))
            digito = True
        except ValueError:
            print('Opcion incorrecta introduce un numero entero')

    return num


import datetime
import time

Id = 0
Cerrar_Programa = False
opcion = 0
count = 0

fecha_hoy = datetime.date.today()



while not Cerrar_Programa:

    print("1 - Registrar una venta")
    print("2 - Consultar una venta")
    print("3 - Reporte de venta por medio de fecha")
    print("4 - Cerrar programa")

    print("Eliga alguna de las siguientes opciones: ")

    opcion = Numero_Menu()

    #Importacion de sqlite3 para generar la base de datos
    import sqlite3

    con = sqlite3.connect('base_datos_cosmeticos.db')
    mi_cursor = con.cursor()
    mi_cursor.execute(
        "CREATE TABLE IF NOT EXISTS ventas(Id INT PRIMARY KEY , fecha, descripcion, cantidad, precio)")
    
    mi_cursor = con.cursor()
    mi_cursor.execute('SELECT Id FROM ventas')
    rows = mi_cursor.fetchall()
    cont = 0

    
    for row in rows:        
        cont = row[0] + 1
    if opcion == 1:
        
        descripcion=input("Descripción del artículo: ""\n")
        piezas=int(input("Cantidad de piezas vendidas: ""\n"))
        precio=float(input("Precio de venta: ""\n"))       
        total=piezas*precio
        Id = cont
        "import sqlite3"
        "con = sqlite3.connect('base_datos_cosmeticos.db')"
        "def sql_insert(con, entities):"
        mi_cursor = con.cursor()
        mi_cursor.execute("INSERT INTO ventas VALUES('"+str(Id)+"', '"+str(fecha_hoy)+"', '"+descripcion+"', '"+str(piezas)+"', '"+str(precio)+"')")
        con.commit()

        print("Total a Pagar: "+str(total))


    #Consultar una venta
    elif opcion == 2:
        opt=int(input("ID de venta a buscar: ""\n"))
        mi_cursor = con.cursor()
        mi_cursor.execute("SELECT * FROM ventas WHERE Id = '"+str(opt)+"'")
        rows = mi_cursor.fetchall()
  
        for row in rows:        
            print(row)


    #Reporte de venta por medio de fecha
    elif opcion == 3:
        opt=input("Reporte por fechas de venta a buscar utilizando el formato YYYY-MM-DD: ""\n")
        mi_cursor = con.cursor()
        mi_cursor.execute("SELECT * FROM ventas WHERE fecha = '"+str(opt)+"'")
        rows = mi_cursor.fetchall()

        for row in rows:        
            print(row)



    #Salida del programa
    elif opcion == 4:
        Cerrar_Programa = True
    else:
        print("Elija una de estas opciones")

print("PROGRAMA CERRADO EXITOSAMENTE")