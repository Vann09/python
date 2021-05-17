import requests, json

url = 'http://school.labs.com.es/api/students/'

id = input ('Dime tu ID: ')
response = requests.get(url+id)
data = None
headers = { 'Content-Type' : 'application/json' }

if (response.status_code == 200):
    data = response.json()
    print (data)
    for key in data.keys():
        if (key == 'id'):
            continue
        print (f'{key}:{data[key]}')    
else:
    print ('Error: ', response.reason)

name = input(f'Nombre ({data["firstName"]}): ')
if (len(name) > 0):
    data['firstName'] = name

surname = input (f'Apellido ({data["lastName"]}): ')
if (len(surname) > 0):
    data['lastName'] = surname

birth = input (f'Fecha de Nacimiento ({data["dateOfBirth"]}): ')
if (birth != ""):
    data['dateOfBirth'] = birth 

room = int(input(f'Clase ({data["classId"]}):'))
if (room != ""):
    data['classId'] = room

requests.put(url+id, data=json.dumps(data),headers = headers)


if (response.status_code == 204):
    print ("Registro modificado correctamente")
else:
    print(f'Error: {response.reason}')


