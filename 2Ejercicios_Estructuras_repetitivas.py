#1. Mostrar los números ascendentes desde el 1 al 10


for i in range(1,11):
    print(i)
print("")

#2. Mostrar los números descendentes desde el 10 al 1

contador = 10
for i in range(10):
    print(contador)
    contador -= 1
print("")

#3. Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

numero = int(input("Ingrese un número: "))

for i in range(numero + 1):
    print(i)
print("")

#4. Ingresar un número y mostrar la tabla de multiplicar de ese número.

numero = int(input("Ingrese un número: "))

for i in range(11):
    producto = numero * i
    print(f"{numero} x {i} = {producto}")
print("")

#5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
#número 0. Mostrar la suma y el promedio de todos los números.

suma = 0
for i in range(10):
    numero = int(input("Ingrese un número (Ingrese 0 para finalizar): "))
    if numero == 0:
        break
    else:
        suma += numero
promedio = suma / (i)
print(f"La suma de los números es de: {suma}")
print(f"El promedio de los números es de: {promedio}")
print("")

#6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)

for i in range(1,11):
    print(3 * i)
print("")

#7. Mostrar los números pares que hay desde la unidad hasta el número 50 (*)

for i in range(1,51):
    if (i % 2) == 0:
        print(i)
print("")

#8. Realizar un programa que permita mostrar una pirámide de números.

numero = (input("Ingrese un número: "))
contador = 1
acumulador = "1"
for n in range(int(numero)):
    if numero != acumulador:
        print(acumulador)
        contador +=1
        acumulador = acumulador + str(contador)
    else:
        print(acumulador)
print("")

#9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
#el número ingresado. Mostrar la cantidad de divisores encontrados.

numero = int(input("ingrese un número: "))
for i in range(1,numero+1):
    if (numero % i) == 0:
        print(i)
print("")

#10.Ingresar un número. Determinar si el número es primo o no.

numero = int(input("Ingrese un número: "))
flag = True
for i in range(2, numero):
    if (numero % i) == 0:
        flag = False

if flag:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")
print("")

#11.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
#número ingresado. Informar cuántos números primos se encontraron

numero = int(input("Ingrese un número: "))
flag = True
contador = 0
for i in range(2,numero):
    for n in range(2, i):
        if i % n == 0:
            flag = False
            break
    else:
        flag = True
        contador +=1
    if flag:
        print(i)

print(f"Se encontraron {contador} números primos.")
