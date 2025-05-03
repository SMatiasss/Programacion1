#1. Realizar una función recursiva que calcule la suma de los primeros números naturales:

def suma_naturales(numero: int)->int:
    if numero == 0:
        return numero
    elif numero == 9:
        return numero
    return numero + suma_naturales(numero - 1)

numero = int(input("numero: "))
print(suma_naturales(numero))

#2. Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base: int, exponente: int)->int:
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

#3. Realizar una función recursiva que permita realizar la suma de los dígitos de un número:
123 // 10 = 23 <- //10 = 1 2

def sumar_digitos(num: int)->int:
    if num == 0:
        return 0
    else:
        return num % 10 + sumar_digitos(num // 10)

#4. Realizar una función para calcular el número de Fibonacci de un número ingresado por consola.

def calcular_fibonacci(num: int)->int:
    if num == 0 or num == 1:
        return num
    else:
        return calcular_fibonacci(num - 1) + calcular_fibonacci(num - 2)

print(calcular_fibonacci(8))
