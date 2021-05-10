import sqlite3, pymssql


# Creamos una BD de SQLite llamada Northwind.db
connection = sqlite3.connect('Northwind.db')
cursor = connection.cursor()

#Creamos un tabla creada Customers
command = "SELECT count() FROM sqlite_master WHERE type = 'table' AND name = 'Customers'
cursor.execute(command)
numTablas = cursor.fetchone()[0]
if (numTablas == 0):
    command = "CREATE TABLE Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax)"
    cursor.execute(command)

#Transladamos la info de SQL Server -> SQLite
