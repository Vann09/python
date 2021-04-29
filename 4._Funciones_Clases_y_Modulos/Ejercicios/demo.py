class Cliente:
    Id = None
    Nombre = None
    Apellido = None
    Genero = None
    Pais = None
    FechaNacimiento = None

    def __init__(self, id, nombre, apellido) -> None:
        self.Id = id
        self.Nombre = nombre
        self.Apellido = apellido

def BuscarClienteId (Item):
        if Item.Id == 2456:
            return True
        else:
            return False

clientes = []

path = "4._Funciones_Clases_y_Modulos\\Ejercicios\\fichero.txt"
file = open(path)

for linea in (file.readlines()):
    data = linea.split(",")
    if data[0].isdigit() == True:
        cliente = Cliente (data[7], data[1], data [2])
        clientes.append(cliente)      
               
file.close ()
print (f"{len(clientes)} importados. ")

#for c in clientes: #para comprobar que ha cogido los datos
    #print (c.Nombre)

while True:
    posicion = input("Dime una posicion: ")
    if posicion == "fin":
        break
    else:
        print (f"{clientes[int(posicion)].Id}{clientes[int(posicion)].Nombre} {clientes[int(posicion)].Apellido}")
    



    
