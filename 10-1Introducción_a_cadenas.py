# Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
# Debe retornar las veces que la letra está incluida en el texto.

def contar_veces_letra_en_texto(letra: str, cadena: str)-> int:
    contador = 0
    for i in range(len(cadena)):
        if letra == cadena[i]:
            contador += 1
    return contador

print(contar_veces_letra_en_texto("s","sancion seccionada en su suelo."))
# Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
# Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
# Si las posiciones no son válidas se debe informar.

def extraer_cadena(cadena: str, indice1: int, indice2: int):
    if 0 <= indice1 <= len(cadena) and 0 <= indice2 <= len(cadena) and indice1 < indice2:
        print(cadena[indice1:indice2])
    else:
        print("Las posiciones brindadas no son válidas.")

extraer_cadena("pensamiento",4,6)

# Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
# Se debe retornar el caracter en la posición indicada por el número si ésta es válida.

def char_at(cadena: str, numero: int)->str:
    if numero >= 0 and numero < len(cadena):
        return cadena[numero]

print(char_at("cucharita",0))