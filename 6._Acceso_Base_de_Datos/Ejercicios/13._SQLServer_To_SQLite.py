import sqlite3, pymssql

# Creamos una BD de SQLite llamada Northwind.db
connection = sqlite3.connect('Northwind.db')
cursor = connection.cursor()

#Creamos un tabla creada Customers
command = "SELECT count() FROM sqlite_master WHERE type = 'table' AND name = 'Customers'"
cursor.execute(command)
numTablas = cursor.fetchone()[0]
if (numTablas == 0):
    command = "CREATE TABLE Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax)"
    cursor.execute(command)

#Transladamos la info de SQL Server -> SQLite
connection2 = pymssql.connect(server='localhost', user = 'test', password = 'test100', database = 'Northwind')

cursor2 = connection2.cursor()
command = 'SELECT * FROM Customers'
cursor2.execute(command)

data = cursor2.fetchall()
command = "INSERT INTO Customers VALUES (?,?,?,?,?,?,?,?,?,?,?)"

################################################################################

#for r in data:
#    cursor.execute(command, r)

################################################################################

cursor.executemany(command, data)

################################################################################


connection.commit()

cursor.close()
cursor2.close()
connection2.close()
