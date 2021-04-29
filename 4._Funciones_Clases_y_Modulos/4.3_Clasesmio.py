from datetime import datetime

class Alumno:
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None

    #Función constructor se ejecuta al crear el objeto
    #self represente al mismo objeto
    def __init__(self, nombre, apell1, apell2) -> None:
        self.Nombre = nombre
        self.Apellido1 = apell1
        self.Apellido2 = apell2

    def getNombreCompleto(self) -> None:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"

    def setFechaNacimiento(self, fecha) -> None:
        self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()            

    def getEdad(self) -> int:
        return datetime.now().year - self.FechaNacimiento.year


alumno = Alumno("Jose", "Izquierdo", "")
alumno.setFechaNacimiento(input("Dime tu fecha de nacimiento: "))
print (f"Me llamo {alumno.getNombreCompleto()}")
print(f"Edad: {alumno.getEdad()} años")