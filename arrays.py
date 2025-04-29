# Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los guarde en una lista y la retorne. El programa principal debe invocar a la función y mostrar por pantalla el retorno.

def guardar_10nombres()->list:
    lista_nombres = []
    for i in range(10):
        lista_nombres += [input("Ingrese el nombre a guardar: ")]
    return lista_nombres

for nombres in guardar_10nombres():
    print(nombres)

# Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida posición y número a guardar
# al usuario, lo guarde en una lista en la posición solicitada aleatoriamente y la retorne. El programa principal
# debe invocar a la función y mostrar por pantalla el retorno.

def pedir_numero_y_posicion()->list:
    lista_numeros = [0] * 10
    numero = int(input("Ingrese un número:"))
    posicion = int(input("Ingrese la posición en la que desea guardarlo (1-10): "))
    lista_numeros[posicion - 1] = numero
    return lista_numeros

for lista in pedir_numero_y_posicion():
    print(lista)

# Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango especificado, validar los números
# solicitados dentro de ese rango, guardar en una lista y retornarla. El programa principal debe invocar a la función
# y mostrar por pantalla el retorno.

def pedir_10nums_en_rango(minimo :int, maximo :int)->list:
    numeros10 = []
    for i in range(10):
        numero = int(input(" \nIngrese un número dentro del rango: "))
        while numero < minimo or numero > maximo:
            if numero < minimo or numero > maximo:
                print(" \nNúmero fuera del rango, intente denuevo. ")
            numero = int(input(" \nIngrese un número dentro del rango: "))
        numeros10 += [numero]
    return numeros10

rango_min = int(input("Ingrese el rango mínimo en el que desea verificar los números: "))
rango_max = int(input("Ingrese el rango máximo en el que desea verificar los números: "))
for numeros in pedir_10nums_en_rango(rango_min,rango_max):
    print(numeros)

# Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números y un número especificado.
# La misma debe buscar el número especificado en la lista y retornar “True” si existe.

def buscar_numero(lista :list, numero :int)->bool:
    flag = False
    for i in range(len(lista)):
        if lista[i] == numero:
            flag = True
    return flag

lista_numeros = [1,67,3,9,88]
numero = 9
if buscar_numero(lista_numeros, numero):
    print("El número se encuentra dentro de la lista.")
else:
    print("El número no se encuentra dentro de la lista.")

# Ejercicio 5: Dadas las siguientes listas:
# Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
# Desarrollar una función que reciba por parámetro la lista de edades, busque a las personas de menor edad
# (puede ser más de una) y las retorne. El programa principal deberá mostrar nombre y edad de los menores.

def buscar_menores(nombres :list,edades :list)-> list:
    menores = []
    minimo = 999
    for i in range(len(edades)):
        if edades[i] <= minimo:
            minimo = edades[i]
    menores.append(minimo)
    for i in range(len(edades)):
        if edades[i] == minimo:
            menores += [nombres[i]]
    return menores

nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
for menor in buscar_menores(nombres,edades):
    print(menor)

# Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo listas_personas.py.
# Importar los nombres a una lista. Realizar una función que muestre los mismos.

from listas_personas import nombres as nombres_local

def mostrar_listas():
    for nombre in nombres_local:
        print(nombre)

# Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de compras on-line 
# recientemente lanzado al mercado para ello necesita un programa que le permita acceder a los datos relevados.
# Realizar una función con el siguiente Menú de Opciones:
# 1-Importar listas
# 2-Listar los datos de los usuarios de México
# 3-Listar los nombre, mail y teléfono de los usuarios de Brasil
# 4-Listar los datos del/los usuario/s más joven/es
# 5-Obtener un promedio de edad de los usuarios
# 6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
# 7-Listar los datos de los usuarios de México y Brasil cuyo código postal
# sea mayor a 8000
# 8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40
# años.
# Ejercicio 8: Crear una función para cada opción de menú.
# Ejercicio 9: Desarrollar las funciones en una biblioteca.

from listas_personas import *
from funciones_compras_online import *

def comenzar_menu():
    importado = False
    opcion = None
    print("-" * 100)
    while opcion != 0:
        print(" \nBienvenido a la tienda on-line\n " + "\n" + "-" * 100 + "\n \n1-Importar listas\n2-Listar los datos de los usuarios de México\n3-Listar los nombre, mail y teléfono de los usuarios de Brasil\n4-Listar los datos del/los usuario/s más joven/es\n5-Obtener un promedio de edad de los usuarios\n6-De los usuarios de Brasil, listar los datos del usuario de mayor edad\n7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.\n0-Finalizar programa.\n" + "-" * 100)
        opcion = int(input(" \nElija una opción: "))
        if opcion == 1:
            print('\n"Listas_personas.py" importado con éxito. \n' + '.' * 100)
            importado = True
            opcion = None
        elif opcion == 0:
            opcion = cerrar_menu()
        elif importado == False:
            print("\nDebe importar la lista primero.\n" + "-" * 100)
        else:
            match opcion:
                case 1:
                    print('\n"Listas_personas.py" ya ha sido importado \n' + '.' * 100)
                    opcion = None
                case 2:
                    for usuario in listar_datos_de_mexico():
                        print(f"\n {usuario}\n" + "." * 100)
                    print("-" * 100)
                    opcion = None
                case 3:
                    for usuario in listar_datos_de_brasil():
                        print(f"\n {usuario}\n" + "." * 100)
                    print("-" * 100)
                    opcion = None
                case 4:
                    for usuario in listar_datos_joven():
                        print(f"\n {usuario}\n" + "." * 100)
                    print("-" * 100)
                    opcion = None
                case 5:
                    print(f"\nEl promedio de edad es de {determinar_premedio_de_edad()} años.\n" + "-" * 100)
                    opcion = None
                case 6:
                    for usuario in listar_mayor_de_brasil():
                        print(f"\n {usuario}")
                    print("-" * 100)
                    opcion = None
                case 7:
                    for usuario in listar_mexico_brasil_zip8000():
                        print(f"\n {usuario}\n" + "." * 100)
                    print("-" * 100)
                    opcion = None
                case 8:
                    for usuario in listar_datos_italianos40():
                        print(f"\n {usuario}\n" + "." * 100)
                    print("-" * 100)
                    opcion = None
                case 0:
                    opcion = cerrar_menu()
                case _:
                    print("Opción inválida, intente denuevo.")
                    print("-" * 100)
                
comenzar_menu()
