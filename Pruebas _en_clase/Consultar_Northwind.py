import requests

url = 'http://api.labs.com.es/v1.0/clientes.ashx'
ID = input ('Dime un ID: ')
paramsCliente = {'id': ID}
response = requests.get(url, paramsCliente)

if (response.status_code == 200):
    data = response.json()
    for d in data:
        print()
        print ('Nombre de la compañia:' , d['CustomerID'])
        print ('Nombre de contacto:' , d['ContactName'])
        print ('Puesto de contacto:' , d['ContactTitle'])
        print ('Dirección:' , d['Address'])
        print ('Ciudad:' , d['City'])
        print ('Región:' , d['Region'])
        print ('Código Postal:' , d['PostalCode'])
        print ('Pais:' , d['Country'])
        print ('Teléfono:' , d['Phone'])
        print ('Fax:' , d['Fax'])   
        print()
else:
    print ('Error: ', response.reason)