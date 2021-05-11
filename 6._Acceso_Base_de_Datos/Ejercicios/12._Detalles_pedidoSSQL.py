import pymssql

conexion = pymssql.connect(server='localhost', user = 'test', password = 'test100', database = 'Northwind')



idPedido = input ("Identificador del pedido: ")

cursor = conexion.cursor()
cursor = conexion.cursor(as_dict=True)

cursor.execute('SELECT*FROM Orders WHERE OrderID = %d', idPedido )

row = cursor.fetchone()
print(f"=================================================================")
print(f"Datos del pedido {idPedido}.")
print(f"=================================================================")
print(f"Entregar: {row['ShipName']}.")
print(f"          {row['ShipAddress']}.")
print(f"          {row['ShipCity']} {row['ShipCountry']}.")
print(f"=================================================================")
print(f"{'Producto':<35} {'Cant. '} {'Precio':>8} {'Total':>8}")
print(f"=================================================================")

# Buscamos el detalle del pedido
cursor.execute('SELECT*FROM [Order Details] WHERE OrderID = %d', idPedido)
totalPedido = 0  
lista = cursor.fetchall()  
for linea in lista:
   
    # Buscasmos la descripción del producto, utilizando ProductID
    cursor.execute('SELECT ProductName FROM Products WHERE ProductID = %d', linea['ProductID'])
    producto = cursor.fetchone()

    # Mostramos cada linea de pedido
    # producto  -  cantidad  - precio  -  precio * cantidad
    totalLinea = (linea['Quantity'])* (linea['UnitPrice'])
    totalPedido += totalLinea
    print (f"{producto['ProductName']:<35} {linea['Quantity']:>6} {linea['UnitPrice']:>8} {totalLinea:>8}")

#Mostar el importe total del pedido
print(f"=================================================================")
print(f" {'TOTAL':>51} {totalPedido:>8}")
print(f"=================================================================")

cursor.close()
conexion.close