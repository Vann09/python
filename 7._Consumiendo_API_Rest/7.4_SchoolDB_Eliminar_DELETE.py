import requests, json

url = 'http://school.labs.com.es/api/students/'

id = id = input ('Dime tu ID: ')

response = requests.delete(url+id)

if (response.status_code == 200):
    print ("Registro borrado correctamente")
    print (f"Data: {response.text}")
else:
    print ("Error: ", response.reason)
    
    