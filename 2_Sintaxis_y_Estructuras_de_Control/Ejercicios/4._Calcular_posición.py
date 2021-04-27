################################################
# 1. Preguntar una frase
# 2. Preguntar una letra
# 3. Contar cuantas veces se repite esa letra
# 4. Usar un while
################################################

frase = input("Dime una frase: ")
letra = input ("Dime una letra: ")

valor = 0                           #variable que funciona como indice
contador = 0                        #variable que uso para contar coincidencias
while (valor < len(frase)):         #mientras valor del indice sea inferio al numero de elementos de la colección
    if (frase[valor] == letra):
        contador +=1
    valor += 1

print (f"En tu frase aparece {contador} veces la letra {letra}.")
print (f"{frase.count(letra)}")



