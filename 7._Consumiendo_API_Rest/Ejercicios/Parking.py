import requests, json

url = {
    'Base'  :'https://openapi.emtmadrid.es/v1/',
    'Login' :'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'ParkInfo' : 'https://openapi.emtmadrid.es/v1/citymad/places/parkings/availability/'
}

headers = { "X-ClientId" : 'a42e6bb5-a334-4115-886f-e4a0b7ec24eb', 'passKey' : '9FFCF6F87E38347060F4A1D3BDC1F8BA4F67DB222D4B3A15BB58DA109222878007570375BE7F6286B4567DB2F33497F00B7D02AAA78BF56C39778B205DA8D43E'}

token = None
response = requests.get(url['Login'], headers=headers)
if (response.status_code == 200):
    #print(response.text)
    token = response.json()['data'][0]['accessToken']
    print ('token:', response.json()['data'][0]['accessToken'])  
else:
    print ('Error:', response.reason)

if (token !=None):
    headers = {'accessToken' :token}
    response = requests.get(url['ParkInfo'], headers=headers)
    data = response.json()['data']
    if (response.status_code == 200):
        totalparking = 0
        for d in data:
            print ("===========================================")
            print ("Nombre:" , d['name'])
            print ("Dirección:" , d['address'])
            print ("Codigo Postal" , d['postalCode'])
            print ("Plazas de Parking:", d['freeParking'])
            
            if (d['freeParking'] != None):
                parking = d['freeParking']
                totalparking += parking
            
            print ()
            
print(f"Actualmente hay {totalparking} plaza/as libres.")


    
    