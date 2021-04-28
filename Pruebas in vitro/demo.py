from datetime import datetime

dt = datetime.now().date()

class Alumno:

    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None

    def __init__(self, nombre, apell1, apell2) -> None:
        self.Nombre = nombre
        self.Apellido1 = apell1
        self.Apellido2 = apell2

    def getFecha(self) -> None:
        fecha = input ("Dime tu fecha de nacimiento: ")
        self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()


    def Edad(self) -> None:
        self.Edad = dt.year - self.FechaNacimiento.year
        print (f"Tengo {self.Edad} años.")

    def Saludo(self) -> None:

        print(f"Hola, me llamo {self.Nombre} {self.Apellido1} {self.Apellido2}")

        
alumno = Alumno("Borja", "Cabeza", "Rozas")
alumno.getFecha()
alumno.Edad()
alumno.Saludo()