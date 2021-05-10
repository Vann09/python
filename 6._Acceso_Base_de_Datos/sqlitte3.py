import sqlite3  #https://docs.python.org/es/3/library/sqlite3.html
import sys

connection = sqlite3.connect('demo.db')
cursor = connection.cursor()


# En una DB nueva, necesitamos crear las tablas
# Este código se ejecuta una sola vez
command = "SELECT COUNT () FROM sqlite_master WHERE type = 'table' AND name = 'Alumno'"
cursor.execute(command)
tablas = cursor.fetchone()[0]
if (tablas == 0):
    command = "CREATE TABLE Alumno (id, nombre, apellidos, curso, notas)"
    cursor.execute(command)

# Consultar datos
cursor.execute(command)
r = cursor.fetchone()
while (r):
    print (r)
    r = cursor.fetchone()

print()

command = "SELECT * FROM Alumno"
for r in cursor.execute(command):
    print (r)

print()

cursor.execute(command)
data = cursor.fetchall()
for r in data:
    print (r)

sys.exit()

#Insertar un registro en la DB
command = "INSERT INTO Alumno (id, nombre) VALUES ('A00','Jose')"
command = "INSERT INTO Alumno VALUES ('A00','Jose', 'Izquierdo', '2B', Null)"
cursor.execute(command)
connection.commit()

#Insertar varios registros en la DB
listaAlumnos = [('H32','Ana','Trujillo','2B', None),('M50','Adrián','Sanchez','2C', None),('Y38','Lidia','Truyol','2A', None)]
command = "INSERT INTO Alumno VALUES (?, ?, ?, ?, ?)"
cursor.execute(command, listaAlumnos)
connection.commit()