lista = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
#### D1. Pregunta al operador su DNI sin letra.
dni = int(input("Dime tu DNI sin la letra: "))

#### D2. Calcula el resto de dividir el número del DNI entre 23.
letra = dni%23 

#### D3. Muestra el DNI con la letra. El resto de la división representa la posición de la letra del DNI en ***lista***.
print(f"La letra del DNI es {lista[letra]} y el DNI completo es ",dni,"-",lista[letra])


