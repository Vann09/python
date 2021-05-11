import requests

# Utilizo función get() para realizar llamadas a microservicios en modo GET
url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)

print ('Código de estado:', response.status_code)
print ('Estado: ', response.reason)

if (response.status_code == 200):
    print ('Cabeceras:', response.headers)
    print ('Tipo del Contenido:', response.headers['Content-Type'])
    if (response.headers['Content-Type'] == 'application/json'):
        data = response.json()
        print ('Latitud:' , data['iss.position']['latitude'])
        print ('Longitud:' , data['iss.position']['longitude'])
        print ('Registro de tiempo:' , data['timestamp'])
        print ('Mensaje:' , data['message'])
    else:    
        print ('Contenido: ', response.text)
        print ('Contenido: ', response.content) #en formato bytes
else:
    print ('Error: ', response.reason)