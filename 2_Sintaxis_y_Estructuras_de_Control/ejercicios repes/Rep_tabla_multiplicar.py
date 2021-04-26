num = int(input("Dime un número: "))
print (f"Tabla de multiplicar de {num}")
print ("===================================")

for n in range (1,11):
    print (f"{num:2.0f} x {n} = {num*n:2.0f}")
print ()
for m in range (1,11):
    print (f"Tabla de multiplicar de {m}")
    print ("=================================")
    for n in range (1,11):
        print (f"{m} x {n} = {m*n}")
    print ()