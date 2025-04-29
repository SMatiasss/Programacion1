# 1. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna
# el área.

def determinar_area_rectanculo(base:int,altura:int)->int:
    area = base * altura
    return area

# 2. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro
# y devolver el área.

def determinar_area_circulo(radio:int)->int:
    area = 3.14 * radio ** 2
    return area

# 3. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje
# indicando si el número es par o impar.

def determinar_par_o_impar():
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

# 4. Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es
# par, False en caso contrario.

def determinar_par_o_impar2()->bool:
    numero = int(input("Ingrese un número: "))
    flag = False
    if numero % 2 == 0:
        flag = True
    return flag
    
# 5. Define una función que encuentre el máximo de tres números. La función debe
# aceptar tres argumentos y devolver el número más grande.

def numero_mas_grande(num1:int,num2:int,num3:int)->int:
    maximo = num1
    if num2 > maximo:
        maximo = num2
    if num3 > maximo:
        maximo = num3
    return maximo

# 6. Diseña una función que calcule la potencia de un número. La función debe recibir la
# base y el exponente como argumentos y devolver el resultado.

def determinar_potencia_de_un_numero(base:int,exponente:int)->int:
    resultado = base ** exponente
    return resultado

print(determinar_potencia_de_un_numero(2,3))

print(determinar_potencia_de_un_numero(10,2))

# 7. Crear una función que reciba un número y retorne True si el número es primo, False
# en caso contrario.

def determinar_si_es_primo(num:int)->bool:
    flag = True
    for i in range(2, num):
        if (num % i) == 0:
            flag = False
    return flag

num = int(input("Ingrese un número: "))
if es_primo(num):
    print("El número es primo.")
else:
    print("El número no es primo")

# 8. Crear una función que (utilizando la función del punto 11 de la guía de For),
# muestre todos los números primos comprendidos entre entre la unidad y un número
# ingresado como parámetro. La función retorna la cantidad de números primos
# encontrados.

def cantidad_de_numeros_primos(numero:int)->int:
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
    return contador

numero = int(input("Ingrese un número: "))
print(f"Se encontraron {cantidad_de_numeros_primos(numero)} números primos.")

# 9. Crear una función que imprima la tabla de multiplicar de un número recibido como
# parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir
# el rango de multiplicación. Por defecto es del 1 al 10.

def tabla_de_multiplicar_de_un_numero(num:int,inicio:int,fin:int):
    if inicio == 0 and fin == 0:
        for i in range(1,11):
            producto = num * i
            print(f"{numero} x {i} = {producto}")
    else:
        for i in range(inicio, fin + 1):
            producto = numero * i
            print(f"{numero} x {i} = {producto}")

numero = int(input("Ingrese un número para crear su tabla de multiplicar: "))
comienzo = int(input("Establezca el inicio de la tabla (0 para no establecer): "))
final = int(input("Establezca el final de la tabla (0 para no establecer): "))
tabla_de_multiplicar_de_un_numero(numero,comienzo,final)

# 10. Crear una función que le solicite al usuario el ingreso de un número entero y lo
# retorne.

def ingreso_numero_entero()->int:
    numero = int(input("ingrese un número entero: "))
    return numero

ingreso_numero_entero()

# 11. Crear una función que le solicite al usuario el ingreso de un número flotante y lo
# retorne.
def ingreso_numero_float()->float:
    numero = float(input("Ingrese un número de tipo flotante: "))
    return numero

ingreso_numero_float()

# 12. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.

def ingreso_de_cadena()->str:
    cadena = input("Ingrese lo que quiera: ")
    return cadena

ingreso_de_cadena()

# 13. Especializar las funciones del punto 10, 11, 12 para hacerlas reutilizables. Agregar
# validaciones.

def validacion_de_entero(num)->int:
    while num != int(num):
        num= float(input("Número inválido, intente denuevo: "))
    return int(numero_entero)

def validacion_de_flotante(num)->float:
    while num == int(num):
        print("Usted ha ingresado un número entero, por favor ingrese un número con decimales")
        num = float(input("\nIngrese un número de tipo flotante: "))
    return num

def validacion_de_cadena(cadena:str)->str:
    if cadena == type(str):
        return cadena

numero_entero = float(input("Ingrese un número entero: "))
validacion_de_entero(numero_entero)
numero_float = float(input(" \nIngrese un número solo de tipo flotante: "))
validacion_de_flotante(numero_float)
cadena = input(" \nIngrese lo que quiera: ")
validacion_de_cadena(cadena)




