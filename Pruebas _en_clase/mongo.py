from pymongo import MongoClient
from pprint import pprint

## Establecer conexión con MongoDB (motor de base de datos)

client = MongoClient ('localhost',27017)
client = MongoClient ('mongodb://localhost:27017/')

## Mostrar estado del servidor

#Asigno a la variable db el objeto que representa
db = client.admin

# Ejecuto comandos en la base de datos utilizando command
# serverStatus retorna el estado del servidor en JSON
status = db.command("serverStatus")
#pprint (status)

## Trabajando con datos
# Seleccionar base de datos con la que trabajar

#northwindDB = client ['Northwind']
northwindDB = client.Northwind

#Listar las colecciones de la base de datos
print (northwindDB.list_collection_names())
#print (northwindDB.list_collections())

#Selecciono una coleccion de la base de datos
#collection = client.Northwind.customers
#collection = client['Northwind']['customers']
#collection = northwindDB['customers']
collection = northwindDB.customers

#Utilizo estimated_document_count() para saber el nº de documentos en la coleccion
result = collection.estimated_document_count()
print (result)
#Buscar documentos dentro de una coleccion

result = collection.find({'Country': 'USA'})
result = collection.find({'Country': 'USA', 'City': 'Portland'})
result = collection.find({'Country': {'$in' : ['USA', 'Mexico']}})
result.next()
pprint (result)
print (collection.count_documents({'Country': 'USA'}))


#Buscar documentos dentro de una coleccion y retorna el primer documento encontrado
#result = collection.find_one({'Country': 'USA'})
#pprint (result)


#Insertar nuevos registros
customer = {
    "CustomerID": "DEMO2",
    "CompanyName": "Uno Alimentación SL",
    "ContactName": "Jose Izquierdo",
    "ContactTitle": "Propietario",
    "Address": "Calle Desengaño, 21",
    "City": "Madrid",
    "Region": "Madrid",
    "PostalCode": "28035",
    "Country": "Spain",
    "Phone": "(91) 652 165 456",
    "Fax": "(91) 652 165 454"
}

#idNewDocument = collection.insert_one(customer).inserted_id
#print ('ID Nuevo Documento:', idNewDocument)

query = {'CustomerID': 'DEMO2'}
newValues = {
    "$set" : {
        "CompanyName": "Catering 2 SL", 
        "Address": "Avenida del Tren, 45",
        "Phone": "(91) 658 145 456"
        }
    }

result = collection.update_one(query, newValues)
print (result.matched_count, 'elementos encontrados.')
print (result.modified_count, 'elementos modificados.')
pprint (result)