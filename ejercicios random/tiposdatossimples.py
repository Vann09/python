#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
#print ("¡Hola Mundo!")

#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
#saludo = '¡Hola Mundo!'
#print (saludo)

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
#nombre = input ("¿Cómo te llamas? ")
#print (f"¡Hola {nombre}!")
#print ("¡Hola " + nombre + "!")

#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética .
#maths = ((3+2)/(2*5))**2
#print (maths)

#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
#hours = float(input ("¿Cuantas horas trabajas? "))
#cost = float(input ("¿Cuanto cobras por hora? "))
#print (f"{hours*cost} € cobras.")

#Escribir un programa que lea un entero positivo,n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n .
#num = int(input("Dime un número: "))
#print (f"La suma de los primeros numeros enteros desde 1 hasta {num} es {(num*(num+1))/2}.")

#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
#peso = float(input("Dime tu peso en kg: "))
#altura = float (input("Dime tu altura en metros: "))
#imc = peso/(altura)**2
#print (f"Tu indice de masa corporal es {imc:2.2f}")

#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
#num1 = int (input("Dime un número entero: "))
#num2 = int (input("Dime otro número: "))
#print (f"{num1} entre {num2} da un cociente {num1//num2} y un resto {num1%num2}.")

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
#dinero = float(input("Cuanto quieres invertir: "))
#inter = float(input ("A que interés anual: "))
#años = int (input("A cuantos años: "))
#print (f"Obtendrás {dinero * (inter/100 + 1) ** años:1.2f} €.")

#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
#clown = 112
#doll = 75
#pclown = int(input ("Payasos a pedir: "))
#pdoll = int(input ("Muñecas a pedir: "))
#print (f"El peso total del pedido a enviar es de {(clown*pclown) + (doll*pdoll)} gramos")

#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
#money = float(input("Dinero a depositar: "))
#interes = 4
#balance1 = money*(interes/100 + 1)
#print(f"El balance del primer año es de {balance1:1.2f}")
#balance2 = balance1*(interes/100 + 1)
#print(f"El balance del primer año es de {balance2:1.2f}")
#balance3 = balance2*(interes/100 + 1)
#print(f"El balance del primer año es de {balance3:1.2f}")

#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
#pan = 3.49
#panp = 0.6
#panpsell = int(input("Pan vendido del dia anterior: "))
#print (f"El precio del pan es de {pan} €, si la barra no es del día se aplica un descuesto del {panp*100} %, por lo que su compra es de {panpsell*pan*(1-panp):1.2f} €.")


