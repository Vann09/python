lista = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
#### D1. Pregunta al operador su DNI sin letra.
dni = (input("Dime tu DNI sin la letra: "))
if (str(dni).isdigit()) and ((len(dni) == 8)):
    #### D2. Calcula el resto de dividir el número del DNI entre 23.
    letra = int(dni)%23 

    #### D3. Muestra el DNI con la letra. El resto de la división representa la posición de la letra del DNI en ***lista***.
    print(f"La letra del DNI es {lista[letra]} y el DNI completo es",dni,"-",lista[letra])
else:
    print ("El DNI no es válido.")

