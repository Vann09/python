from pymongo import MongoClient

#Cliente
client = MongoClient ('localhost',27017)

#Base de datos
db = client.Northwind

#Colecciones
orders = db.orders
details = db.order_details
products = db.products

idPedido = input("Identificador del pedido: ")

pedido = orders.find_one({'OrderID': idPedido}) 
if (pedido != None):
    print(f"Datos del pedido {idPedido}.")
    print(f"Entregar: {pedido['ShipName']}.")
    print(f"          {pedido['ShipAddress']}.")
    print(f"          {pedido['ShipCity']} {pedido['ShipCountry']}.")
    #Buscamos detalle del pedido
    detalle = details.find({'OrderID' : idPedido})

    #Recorro con while el cursor detalles del pedido y se muestra cada línea
    while (detalle.alive):
        linea = detalle.next()
        #A la vez busco y muestro descripción del producto usando ProductID
        producto = products.find_one({'ProductID': linea ['ProductID']})
    
        #Descripcion - Cantidad - Precio - Precio*cantidad
        total = int(linea['Quantity'])* float(linea['UnitPrice'])
        print (f"{producto['ProductName']:<35} {linea['Quantity']:>6} {linea['UnitPrice']:>8} {total:>8}")
    #Mostrar el importe total del pedido
    
else:
    print (f"El pedido {idPedido} no existe.")