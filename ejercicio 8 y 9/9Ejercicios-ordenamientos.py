# Ejercicio 1: Dadas las siguientes listas:
# Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", 
# "Eugenia", "Soledad", "Mario", "Mariela"]
# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
# Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente.

nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

'''
def ordenar_nombres_por_edad_ascendente(edades: list, nombre: list):
    for i in range(len(edades) - 1):
        for j in range(i+1, len(edades)):
            if edades[i] > edades[j]:
                contenedor_nombre = nombre[j]
                nombre[j] = nombre[i]
                nombre[i] = contenedor_nombre
                contenedor_edad = edades[j]
                edades[j] = edades[i]
                edades[i] = contenedor_edad

ordenar_nombres_por_edad_ascendente(edades, nombres)
for i in range(len(edades)):
    print(f"{edades[i]}: {nombres[i]}")
'''

def ordenar_alfabeticamente(nombres: list, edades: list):
    for i in range(len(nombres) - 1):
        for j in range(i+1, len(nombres)):
            if nombres[j] < nombres[i]:
                contenedor_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = contenedor_nombre
                contenedor_edad = edades[i]
                edades[i] = edades[j]
                edades[j] = contenedor_edad

ordenar_alfabeticamente(Nombres, Edades)

for i in range(len(Nombres)):
    print(f"{Nombres[i]}: {Edades[i]}")

# Ejercicio 2: Dadas las siguientes listas:
# Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion",
# "Ingles","Algebra","Contabilidad","Artistica", "Algoritmos","Artistica", 
# "Base de Datos", "Ergonomia", "Naturaleza"]
# Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
# Desarrollar una función que realice el ordenamiento de las listas por nombre de
# manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera descendente.

nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza","Artistica"]
#Agregué un nombre más al final de la lista de "nombres" porque tenía un elemento menos a puntos.
puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenar_materias_ascendente(numero: list, materia: list):
    for i in range(len(materia) - 1):
        for j in range(i+1, len(materia)):
            if materia[i] == materia[j]:
                if numero[i] < numero[j]:
                    contenedor_puntos = numero[i]
                    numero[i] = numero[j]
                    numero[j] = contenedor_puntos
            elif materia[i] > materia[j]:
                contenedor_materia = materia[i]
                materia[i] = materia[j]
                materia[j] = contenedor_materia
                contenedor_puntos = numero[i]
                numero[i] = numero[j]
                numero[j] = contenedor_puntos

ordenar_materias_ascendente(puntos, nombres)
for i in range(len(nombres)):
    print(f"{nombres[i]}: {puntos[i]}")

# Ejercicio 3: Dadas las siguientes listas:
# Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro",
# "Antonio", "Eugenia", "Soledad", "Mario", "María"]
# Apellidos = [“Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui",
# "Mitre","Andrade","Loza","Antares","Roca","Perez"]
# Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
# Desarrollar una función que realice el ordenamiento de las listas por apellido de manera ascendente, si el 
# apellido es el mismo, debe ordenar por nombre de manera ascendente, si el nombre también es el mismo, 
# debe ordenar por nota de manera descendente.

estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "María"]
apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui", "Mitre","Andrade","Loza","Antares","Roca","Perez"]
nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def ordenar_calificaciones(nota: list, apellido: list, nombre: list):
    for i in range(len(apellido) - 1):
        for j in range(i+1, len(apellido)):
            if apellido[i] == apellido[j]:
                if nombre[i] == nombre[j]:
                    if nota[i] < nota[j]:
                        contenedor_puntos = nota[i]
                        nota[i] = nota[j]
                        nota[j] = contenedor_puntos
                else:
                    if nombre[i] > nombre[j]:
                        contenedor_nombre = nombre[i]
                        nombre[i] = nombre[j]
                        nombre[j] = contenedor_nombre
                        contenedor_puntos = nota[i]
                        nota[i] = nota[j]
                        nota[j] = contenedor_puntos
            elif apellido[i] > apellido[j]:
                contenedor_apellido = apellido[i]
                apellido[i] = apellido[j]
                apellido[j] = contenedor_apellido
                contenedor_nombre = nombre[i]
                nombre[i] = nombre[j]
                nombre[j] = contenedor_nombre
                contenedor_puntos = nota[i]
                nota[i] = nota[j]
                nota[j] = contenedor_puntos

ordenar_calificaciones(nota, apellidos, estudiantes)
for i in range(len(estudiantes)):
    print(f"{apellidos[i]} {estudiantes[i]}: {nota[i]}")

# Ejercicio 4: Una startup desea analizar las estadísticas de los usuarios de su sitio de compras on-line 
# recientemente lanzado al mercado para ello necesita un programa que le permita acceder a los datos relevados.
# Agregar los siguientes puntos al Menú de Opciones:
# 9-Listar los datos de los usuarios de México ordenados por nombre
# 10-Listar los datos del/los usuario/s más joven/es ordenados por edad de
# manera ascendente (Si la edad se repite, ordenar por nombre de manera
# ascendente)
# 11-Listar los datos de los usuarios de México y Brasil cuyo código postal
# sea mayor a 8000 ordenado por nombre y edad de manera descendente
# Ejercicio 8: Crear una función para cada opción de menú.
# Ejercicio 9: Desarrollar las funciones en una biblioteca.
# Nota: No se podrá acceder a ninguna opción de menú si no se realizó la importación
# de las listas

#Decidí hacer el programa de compras on-line en un archivo separado, se encuentra en la carpeta "programa Compras On-line"
