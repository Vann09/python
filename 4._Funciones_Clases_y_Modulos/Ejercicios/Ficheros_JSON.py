import json

def PrintData (cliente):
    print (f"Identificador: {cliente['CustomerID']}")
    print (f"Compañia:      {cliente['CompanyName']}") 
    print (f"Contacto:      {cliente['ContactName']} ({cliente['ContactTitle']})")    
    print (f"Dirección:     {cliente['Address']}")
    print (f"               {cliente['PostalCode']} {cliente['City']} {cliente['Country']}")
    print (f"Teléfono:      {cliente['Phone']} Fax: {cliente['Fax']}") 


file = open("Ficheros\\clientes.json", "rt", encoding='UTF-8')

dataJSON = file.read()
file.close ()

customers = json.loads (dataJSON)

#'CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode', 'Country', 'Phone', 'Fax'

#print (type(dataJSON))
#print (type(customers))
#print (len(customers))
#print (customers[0].keys())

#Cod ANATR ANTON

ID = input ("Id: ")

busqueda = list(filter(lambda x : x['CustomerID'] == ID , customers))

if (len(busqueda) == 0):
    print ("El identificador no existe")
else:
    PrintData (busqueda[0])