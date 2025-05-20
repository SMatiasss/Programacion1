# 1) Crear una función que reciba como parámetro una cadena y determine la
# cantidad de vocales que hay de cada una (individualmente). La función
# retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
# la cantidad.
# Por ej:
# cadena = “murcielaguito”
# “a” 1
# “e” 1
# “i” 2
# “o” 1
# “u” 2

def determinar_cantidad_vocales(cadena: str) -> list:
    vocales = [["a", 0],["e", 0],["i", 0],["o", 0],["u", 0]]
    for i in cadena:
        for j in range(len(vocales)):
            if i == vocales[j][0]:
                vocales[j][1] += 1
    return vocales
determinar_cantidad_vocales("estacionamiento")

# 2) Crear una función que reciba una cadena y un caracter. La función deberá
# devolver el índice en el que se encuentre la primera incidencia de dicho
# caracter, o -1 en caso de que no esté.
def encontrar_primer_indice(cadena: str, caracter: str)->int:
    indice = -1
    for i in range(len(cadena)):
        if caracter == cadena[i]:
            indice = i
            break
    return indice
print(encontrar_primer_indice("caceria","a"))

# 3) Crear una función que reciba como parámetro una cadena y determine si la
# misma es o no un palíndromo. Deberá retornar un valor booleano indicando
# lo sucedido.
def determinar_palindromo(cadena: str)-> bool:
    palindromo = False
    if cadena == cadena[::-1]:
        palindromo = True
    return palindromo
print(determinar_palindromo("menem"))

# 4) Crear una función que reciba como parámetro una cadena y suprima los
# caracteres repetidos.
# Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def suprimir_caracteres_repetidos(cadena: str)-> str:
    nueva_cadena = ""
    for i in cadena:
        if i not in nueva_cadena:
            nueva_cadena += i
    return nueva_cadena

print(suprimir_caracteres_repetidos("Hooola"))

# 5) Crear una función que reciba una cadena por parámetro y suprima las
# vocales de la misma.
# Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.

def suprimir_vocales(cadena: str):
    nueva_cadena = ""
    vocales = ["a","e","i","o","u"]
    for i in cadena:
        for j in vocales:
            if i == j:
                break
        else:
            nueva_cadena += i
    return nueva_cadena

print(suprimir_vocales("abcdefghi"))

# 6) Crear una función para contar cuántas veces aparece una subcadena dentro
# de una cadena.
# Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá
# retornar el valor 2.
def contar_apariciones_subcadena(cadena: str, subcadena: str)-> int:
    contador = 0
    print(cadena[:len(cadena) - len(subcadena) + 1])
    for i in range(len(cadena) - len(subcadena) + 1):
        print(cadena[i:i + len(subcadena)])
        if cadena[i:i + len(subcadena)] == subcadena:
            contador += 1
    return contador

print(contar_apariciones_subcadena("El pan del panadero","pan"))