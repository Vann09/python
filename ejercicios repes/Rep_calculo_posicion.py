################################################
# 1. Preguntar una frase
# 2. Preguntar una letra
# 3. Contar cuantas veces se repite esa letra
# 4. Usar un while
################################################

phrase = input("Dime una frase: ")
letter = input ("Dime una letra: ")

valor = 0
count = 0
while valor < len(phrase):
    if phrase[valor] == letter:
        count += 1
    valor +=1

print (f"Tu frase contiene la letra {letter} {count} número de veces.")
