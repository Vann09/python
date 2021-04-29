import modulo 
alumno = modulo.Alumno("Jose", "Izquierdo", "")
print (f"{alumno.getNombreCompleto()}")

from modulo import Alumno 
alumno = Alumno("Jose", "Izquierdo", "")
print (f"{alumno.getNombreCompleto()}")

from modulo import Alumno as FichaAlumno
alumno = FichaAlumno("Jose", "Izquierdo", "")
print (f"{alumno.getNombreCompleto()}")

from modulo import *
alumno = Alumno("Jose", "Izquierdo", "")
print (f"{alumno.getNombreCompleto()}")