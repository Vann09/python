import requests, json

url = 'http://school.labs.com.es/api/students/'

#{"firstName":"Ana","lastName":"Sánchez","dateOfBirth":"2006-05-09","classId":1}
name = input("Dime tu nombre: ")
surname = input ("Dime tus apellidos: ")
birth = input ("Dime tu fecha de nacimiento (año-mes-dia): ")
room = int(input("Dime tu clase (1,2,3): "))

headers1 = {'Content-Type':'application/json'}
DataAlumn = {'firstName': name, 'lastName':surname, 'dateOfBirth': birth,'classId':room}

response = requests.post(url, data=json.dumps(DataAlumn), headers=headers1)

print ('Código de estado:', response.status_code)
print ('Estado: ', response.reason)

if (response.status_code == 201):
    print ('Id asignado: ', response.json()['id'])
else:
    print ('Error: ', response.reason)


