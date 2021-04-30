from datetime import datetime
class Cliente:
    Id = None
    Nombre = None
    Apellido = None
    Genero = None
    Pais = None
    Edad = None
    FechaAlta = None

    def __init__(self, id, nombre, apellido) -> None:
        self.Id = id
        self.Nombre = nombre
        self.Apellido = apellido

def BuscarClienteId (Item):
        if Item.Id == "1562":
            return True
        else:
            return False


def BuscarMale (Item):
        if   Item.Genero == "Male":
            return True
        else:
            return False

def BuscarFemale (Item):
        if   Item.Genero == "Female":
            return True
        else:
            return False

def Buscar26Fr (Item):
    if Item.Edad < 26 and Item.Pais == "France" :
        return True
    else:
        return False

def BuscarMaleUS (Item):
    if Item.Genero == "Male" and Item.Pais == "United States" :
        return True
    else:
        return False

def BuscarFemaleBrit26 (Item):
    if Item.Edad > 26 and Item.Pais == "Great Britain" and Item.Genero == "Female":
        return True
    else:
        return False




clientes = []

path = "4._Funciones_Clases_y_Modulos\\Ejercicios\\fichero.txt"
file = open(path)

for linea in (file.readlines()):
    data = linea.split(",")
    if data[0].isdigit() == True:
        cliente = Cliente (data[7].strip(), data[1].strip(), data[2].strip())
        cliente.Genero = data[3].strip()
        cliente.Edad = int(data[5].strip())
        cliente.Pais = data[4].strip()
        cliente.FechaAlta = datetime.strptime(data[6].strip(), "%d/%m/%Y").date()
        clientes.append(cliente)      
               
file.close ()
print (f"{len(clientes)} importados. ")

#for c in clientes: #para comprobar que ha cogido los datos
    #print (c.Nombre)

#while True:
    #posicion = input("Dime una posicion: ")
    #if posicion == "fin":
        #break
    #else:
        #print (f"{clientes[int(posicion)].Id}{clientes[int(posicion)].Nombre} {clientes[int(posicion)].Apellido}")

#resultado= list(filter(BuscarClienteId, clientes))
#resultado= list(filter(lambda x : x.Id == "1562", clientes))
#print (len(resultado))

hombres = list(filter(BuscarMale, clientes))
mujeres = list(filter(BuscarFemale, clientes))

print (f"{len(list(filter(BuscarMale, clientes)))} clientes varones.")
print (f"{len(list(filter(BuscarFemale, clientes)))} clientes mujeres.")
print()

print (f"{len(list(filter(Buscar26Fr, clientes)))} clientes menores de 26 años y franceses.")
print (f"{len(list(filter(BuscarMaleUS, clientes)))} clientes varones y estadounidenses.")
print (f"{len(list(filter(BuscarFemaleBrit26, clientes)))} clientes mujeres mayores de 26 años y británicas.")
print ()

E = int(input ("Edad: "))
P = input ("Pais: ")
G = input("Genero: ")

print (f"{len(list(filter(lambda x : x.Edad == E and x.Pais == P and x.Genero == G, clientes)))} coincidentes con los criterios.")
asfdgfdgfddfgd


dfhdf