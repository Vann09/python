file = open ("fichero.txt")
#file = open ("C:\\Users\\Vann\\source\\repos\\Github\\python\\fichero.txt")

#Lee todas las lineas y las retorna como str. Se puede especificar los caracteres a leer 
contenido = file.read() 
#Lee líneas del contenido, retorna la info como str y avanza el cursor a la siguiente linea
linea = file.readline() 
#Lee todas las líneas y retorna la info como una lista
lineas = file.readlines()

print (f"{contenido}")
print (f"Fichero cerrado: {file.closed}")
file.close() #Cerrar arhivo
print (f"Fichero cerrado: {file.closed}")