# Conexión con MongoDB
from pymongo import MongoClient

connect = MongoClient ('localhost',27017)
db = connect.Northwind

# Cuantos productos tenemos ??

productos = db.products
numProductos = productos.estimated_document_count()
print (" Número de Productos: ", numProductos)

# Buscar y Mostrar todos los productos

cursor = productos.find()
while (cursor.alive):
    print(cursor.next()['ProductName'])

print("")

listProductos = productos.find()
for n in listProductos:
    print(f"{n['ProductName']}")

print ("")

#  Buscar todos los productos. Con filter buscamos los productos con UnitsInStock = 0
listProductos = productos.find()
productoStock = list(filter(lambda p : p['UnitsInStock'] == '0', listProductos))
for p in productoStock:
    print(f"{p['ProductName']}")

print ("")

# Buscar en la BD los productos que tengan UnitsInStock = 0
cursor = productos.find({'UnitsInStock': '0'})
while (cursor.alive):
    print(cursor.next()['ProductName'])

# Coste o valor de nuestro stock - Producto -> UnitsInStock, UnitPrice
totalStock = 0
#listProductos = productos.find()
listProductos = productos.find({'UnitsInStock': {'$ne' : '0'}})
for n in listProductos:
    totalProd = int(n['UnitsInStock'])*float(n['UnitPrice'])
    totalStock += totalProd
print (f"\nValor total de Stock:  {totalStock:1.2f}")

# Coste o Valor de nuestro Stock utilizand map() y sum()
TotalStock = sum(list(map(lambda x: float(x['UnitPrice']) * float(n['UnitsInStock']) ,productos.find())))
print(f"\nValor del Stock: {TotalStock:1.2f}")

# Coste o Valor de nuestro Stock utilizando la función aggregate()
query = [
    { '$match': { 'UnitsInStock' : { '$ne': '0' } } },
    { '$addFields': {
        'Price': { '$toDouble': '$UnitPrice' },
        'Stock': { '$toInt': '$UnitsInStock' },
        }
    },
    { '$group': {
        '_id': 'Valor del Stock', 
        'Total': { '$sum': { '$multiply': [ '$Price', '$Stock' ] } },
        'Items': { '$sum' : 1 }
        }
    }      
]

listProductos = productos.aggregate(query)
print(listProductos.next())