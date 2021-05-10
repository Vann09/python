#### I1. Pregunta al operador 5 colores
listcolor = []
print ("Dime 5 colores de 1 en 1: ")
while len(listcolor) < 5:
    colors = input ()
    listcolor.append(colors)

#### I2. Muestra los colores ordenados
listcolor.sort()
print(listcolor)

#### I3. Muestra el color que más letras contenga
letra = 0
for c in range (0, len(listcolor)-1):
    if  len(listcolor[letra]) < len(listcolor[c+1]): 
        letra = c+1
print (listcolor[letra]+" es el color con más letras, " + str(len(listcolor[letra])))
    
#### I4. Muestra el color que más vocales contenga
vocal = "aeiouAEIOU"
for i in range (len(listcolor)-1 ):
    for k in  range (len(listcolor[i])-1):
        if letra == "aeiouAEIOU":
            
        

#### I5. Muestra la cantidad de colores que comienza y finaliza por vocal