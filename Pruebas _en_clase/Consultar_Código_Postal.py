import requests

url = 'https://www.zippopotam.us/es/'
cp = input ('Dime un código postal de España: ')

response = requests.get(url + cp)

print ('Código de estado:', response.status_code)
print ('Estado: ', response.reason)

if (response.status_code == 200):
    data = response.json()
    print ('Lugar:' , data['places'][0]['place name'])
    print ('Región: ', data['places'][0]['state'])
    print ('Longitud:' , data['places'][0]['longitude'])
    print ('Latitud:' , data['places'][0]['latitude'])
else:
    print ('Error: ', response.reason)

    
        
