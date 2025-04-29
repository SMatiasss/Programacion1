# Ejercicio 1:
# Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
# sueldo para esa persona.

nombre = input("Introduzca su nombre: ")
sueldo = int(input("Introduzca su sueldo: "))
aumento = 1.1

sueldo_actualizado = sueldo * aumento

print(f"{nombre}, su sueldo ha recibido un aumentó del 10%, con un total de {sueldo_actualizado}")

# Ejercicio 2:
# Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
# adolescente (entre 13 y 17 años) o niño (menor a 13 años)

edad = int(input("Introduzca su edad: "))

if edad < 0:
    print("Número inválido.")
elif edad < 13:
    print("Sos un menor")
elif edad < 18:
    print("Sos un adolescente.")
else:
    print("sos mayor de edad.")
    
# Ejercicio 3:
# Ingresar 5 números enteros, distintos de cero.
# Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.

numero_1 = int(input("Ingrese un número entero distinto de 0:"))
numero_2 = int(input("Ingrese un número entero distinto de 0:"))
numero_3 = int(input("Ingrese un número entero distinto de 0:"))
numero_4 = int(input("Ingrese un número entero distinto de 0:"))
numero_5 = int(input("Ingrese un número entero distinto de 0:"))

numeros = [numero_1,numero_2,numero_3,numero_4,numero_5]
impares = []
pares = []
contador_pares = 0
contador_impares = 0
menor = 9999999
mayor_par = -9999999


positivos = []
suma = 0

negativos = []
producto = 1

for n in numeros:
    if n < menor:
        menor = n

for n in numeros:
    if (n % 2) == 0:
        pares.append(n)
        contador_pares += 1
    else:
        contador_impares += 1

for n in pares:
    if n > mayor_par:
        mayor_par = n
if contador_pares == 0:
    mayor_par = "* No hay números pares *"

for n in numeros:
    if n > 0:
        positivos.append(n)
for n in positivos:
    suma= suma + n

for n in numeros:
    if n < 0:
        negativos.append(n)

if negativos:
    for n in negativos:
        producto = producto * n
else:
    producto = "* No hay números negativos *"


print("")
print(f"a. La cantidad de números pares es: {contador_pares}.")
print(f"a. La cantidad de números impares es: {contador_impares}.")
print("")
print(f"b. El menor número ingresado es: {menor}.")
print("")
print(f"c. El mayor número par ingresado es: {mayor_par}.")
print("")
print(f"d. La suma de los números positivos es: {suma}.")
print("")
print(f"El producto de los números negativos es: {producto}")

# Ejercicio 4:
# Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
# distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
# ser soltero.

edad_B = int(input("Ingrese su edad: "))
estado_civil = input("Ingrese su estado civil (soltero/casado/separado/divorciado/viudo): ").lower()
if estado_civil != "soltero" and edad_B < 18:
    print("Es muy pequeño para NO ser soltero.")


# Ejercicio 5:
# Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
# por cada estadía como base, se pide el ingreso de una estación del
# año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
# Plata/Córdoba) para vacacionar para poder calcular el precio final:
# -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
# descuento del 10% Mar del Plata tiene un descuento del 20%
# -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
# un aumento del 10% Mar del Plata tiene un aumento del 20%
# -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
# aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
# precio sin descuento.
# Validar el ingreso de datos

estacion = input("Ingrese la estación del año en el que desea vacacionar (Invierno/Verano/Otoño/Primavera): ").lower()
if estacion == "invierno" or estacion == "verano" or estacion == "otoño" or estacion == "primavera":
    localidad = input("Ingrese la localidad a la que desea vacacionar (Bariloche/Cataratas/Mar del Plata/Córdoba): ").lower()
    if localidad == "bariloche" or localidad == "cataratas" or localidad == "mar del plata" or localidad == "cordoba":
        precio_base = 15000

        if estacion == "invierno":
            if localidad == "bariloche":
                precio_base = precio_base * 1.2
            elif localidad == "mar del plata":
                precio_base = precio_base * 0.8
            else:
                precio_base = precio_base * 0.9
        elif estacion == "verano":
            if localidad == "bariloche":
                precio_base = precio_base * 0.8
            elif localidad == "mar del plata":
                precio_base = precio_base * 1.2
            else:
                precio_base = precio_base * 1.1
        else:
            if localidad == "bariloche" or localidad == "cataratas" or localidad == "mar del plata":
                precio_base = precio_base * 1.1


        print("")
        print(f"Estacion elegida: {estacion}")
        print(f"Localidad elegida: {localidad}")
        print("")
        print(f"El costo de las vacaciones es de: ${precio_base}")
    else:
        print("")
        print("Opción inválida")
else:
    print("")
    print("Opción inválida")

