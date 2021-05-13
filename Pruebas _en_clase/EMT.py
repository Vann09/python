import requests, json
from datetime import datetime

url = {
    'Base'  :'https://openapi.emtmadrid.es/v1/',
    'Login' :'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'StopInfo':'https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/<stopId>/arrives/'
}

headers = { 'X-ClientId' : 'a42e6bb5-a334-4115-886f-e4a0b7ec24eb', 'passKey' : '9FFCF6F87E38347060F4A1D3BDC1F8BA4F67DB222D4B3A15BB58DA109222878007570375BE7F6286B4567DB2F33497F00B7D02AAA78BF56C39778B205DA8D43E'}
token = None

response = requests.get(url['Login'], headers=headers)
if (response.status_code == 200):
    #print(response.text)
    token = response.json()['data'][0]['accessToken']
    print ('token:', response.json()['data'][0]['accessToken'])  
else:
    print ('Error:', response.reason)

if (token !=None):
    stopID = input("Dime tu parada: ")
    headers = {'accessToken' :token}
    data = {
        "cultureInfo":"ES",
        "Text_StopRequired_YN":"Y",
        "Text_EstimationsRequired_YN":"Y",
        "Text_IncidencesRequired_YN":"Y",
        "DateTime_Referenced_Incidencies_YYYYMMDD": datetime.now().strftime ('%Y%m%d')
    }
    
response = requests.post(url['StopInfo'].replace ('<stopId>', stopID), data=json.dumps(data), headers=headers)
if response.status_code == 200:
    data = response.json()
    print (f"Información de la parada: {stopID}")

    for d in data['data'][0]['Arrive']:
        print ("==============================================")
        print ('Línea:', d['line'])
        print ('Destino:' , d['destination'])
        print ('Bus: ', d['bus'])
        print ('Distancia:' , d['DistanceBus'], "metros")
        if (d['estimateArrive'] >= 1200):
            print ("El autobus tardará 20 minutos o más")
        else:
            print ('Llegada:' , (d['estimateArrive']//60), "min")
else:
    print ('Error:', response.reason)
