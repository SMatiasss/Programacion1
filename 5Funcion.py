#Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe como parámetro.
def numero_pantalla(numero:int):
    print(numero)

numero_pantalla(2)

# Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.
def ingreso_de_numero()->int:
    numero = int(input("Ingrese un numero:"))
    return numero

# Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La función retorna “True” en caso
# afirmativo y “False en caso contrario. Probar en el programa principal realizando la invocación o llamada.
def numero_par(numero:int)->bool:
    es_par = False
    if numero % 2 == 0:
        return True
    return es_par

numero = int(input("Ingrese un número:"))
numero_par(numero)

if numero_par:
    print("El número ingresado es par.")
else:
    print("El número ingresado no es par")

# Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en un rango determinado
# pasado por parámetro “desde”-“hasta”.

def rango_num(desde:int, hasta:int):
    numero = int(input("Ingrese un número: "))
    if numero >= hasta or numero <= desde:
        print(f"El número {numero} no se encuentra dentro del rango.")
    else:
        print(f"El número {numero} se encuentra dentro del rango.")

minimo_rango = int(input("Determine el mínimo del rango: "))
maximo_rango = int(input("Determine el máximo del rango: "))
rango_num(minimo_rango, maximo_rango)

# Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la 
# función restar en sus 4 combinaciones.
#  restar1(int, int)->int:
#  restar2()->int:
#  restar3(int, int):
#  restar4():
def restar1(num1:int,num2:int)->int:
    resta = num1 - num2
    return resta

def restar2()->int:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese un número: "))
    resta = num1 - num2
    return resta

def restar3(num1:int, num2:int):
    resta = num1 - num2
    print(resta)

def restar4():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese un número: "))
    resta = num1 - num2
    print(resta)

print(restar1(3,2))
print(restar2())
restar3(4,3)
restar4()

# Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor solicitado al usuario, valide el
# mismo entre 10 y 100, realice un descuento del 5% a dicho valor a través de una función llamada realizarDescuento().
# Mostrar el resultado por pantalla. Atención: pueden reutilizarse funciones ya creadas.

def realizarDescuento():
    numero1 = int(input("Ingrese un número: "))
    if numero1 > 10 and numero1 < 100:
        numero1 = numero1 * 0.95
    print(numero1)

# Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2 los valores solicitados al
# usuario, valide los mismos entre 10 y 100, asigne a la variable operacion el valor solicitado al usuario: 's'-sumar,
# 'r'-restar (validar),realice la operación de dichos valores a través de una función. Mostrar el resultado por
# pantalla.
numero1 = 0
numero2 = 0
operacion = None

while numero1 <= 10 or numero1 >= 100:
    numero1 = int(input("Ingrese un número mayor a 10 y menor a 100: "))
    if numero1 <= 10 or numero1 >= 100:
        print(" \nIntente denuevo.\n")
while numero2 <= 10 or numero2 >= 100:
    numero2 = int(input("Ingrese otro número mayor a 10 y menor a 100: "))
    if numero2 <= 10 or numero2 >= 100:
        print(" \nIntente denuevo.\n")
while operacion != 's' and operacion != 'r':
    operacion = input(" \nIngrese 's' si desea sumar o 'r' si desea restar: ").lower()
    if operacion != 's' and operacion != 'r':
        print(" \nIntente denuevo.")

def desarrollo_operacion(num1, num2)->int:
    if operacion == 's':
        cuenta = num1 + num2
    else:
        cuenta = num1 - num2
    return cuenta

print(f" \n{desarrollo_operacion(numero1,numero2)}")
