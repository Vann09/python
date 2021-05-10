import pymssql

conexion = pymssql.connect(server='localhost', user = 'test', password = 'test100', database = 'Northwind')


cursor = conexion.cursor()
cursor = conexion.cursor(as_dict=True)
cursor.execute('SELECT*FROM Customers') #Coge todos los campos de Customers

row = cursor.fetchone()
print (type(row))
print(row)

while (row):
    print(f"     ID: {row['CustomerID']}")
    print(f"Empresa: {row['CompanyName']}")
    print ()
    row = cursor.fetchone()

cursor.close()
conexion.close()

#Para añadir info a la base de datos
cursor.execute("INSERT INTO Customers (CustomerID , CompanyName, City, Country) VALUES ('DEMO2', 'Empresa2, SL', 'Madrid', 'Spain') ")
command = "INSERT INTO Customers (CustomerID , CompanyName, City, Country) VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s)"

#Para eliminar info de la base de datos
cursor.execute("DELETE FROM Customers WHERE CustomerID = %d", #[lo que se quiera eliminar])
#Hay que confirmar la acción con cualquiera de los 2 códigos
conexion.commit() 
#conexion.rollback()