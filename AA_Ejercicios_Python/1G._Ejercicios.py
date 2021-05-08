
while True:
    #### G1. Pregunta al operador cualquier cosa.
    ask = input("Dime lo que quieras: ")
    #### G2. Muestra por ***Simón dice xxxxxxxxx*** incluyendo la respuesta del operador
    if ask != "fin":
        print (f"Simón dice {ask}.")
        #### G3. Esta secuencia de *pregunta/mostrar en pantalla* se repite hasta que el operado responde *fin*
    else:
        break


