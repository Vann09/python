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
        print ('Latitud:' , data['iss_position']['latitude'])
        print ('Longitud:' , data['iss_position']['longitude'])
        print ('Registro de tiempo:' , data['timestamp'])
        print ('Mensaje:' , data['message'])
    else:    
        print ('Contenido: ', response.text)
        print ('Contenido: ', response.content) #en formato bytes
else:
    print ('Error: ', response.reason)
print ("====================================================================")

# Utilizo función post() para realizar llamadas a microservicios en modo POST
url = 'https://postman-echo.com/post'

params1 = {'param1':'demo', 'param2':'demo'}
headers1 = {'Content-Type':'application/json'}
data1 = {'Nombre':'Jose', 'Apellidos': 'Izquierdo'}

response = requests.post(url, params=params1, headers=headers1, data=data1)

print ('Código de estado:', response.status_code)
print ('Estado: ', response.reason)

if (response.status_code == 200):
    print ('Cabeceras:', response.headers) 
    print ('Contenido: ', response.text)
else:
    print ('Error: ', response.reason)