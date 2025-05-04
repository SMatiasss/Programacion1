#1-A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la 
# posición del jugador en la cancha, considerando los siguientes parámetros:
#Menos de 160 cm: Base
#Entre 160 cm y 179 cm: Escolta
#Entre 180 cm y 199 cm: Alero
#200 cm o más: Ala-Pívot o Pívot
altura = int(input("Ingrese la altura del jugador: "))
base = 160
escolta = 180
alero = 199
if altura <= 100:
    print("Altura inválida")
elif altura <= base:
    print("La posición del jugador será: Base")
elif altura <= escolta:
    print("La posición del jugador será: Escolta")
elif altura <= alero:
    print("La posición del jugador será: Alero")
else:
    print("La posición del jugador será: Ala-Pívot o Pívot")
#2-Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...
nota = int(input("Ingrese la nota (1-10): "))
promocion = 6
aprobado = 4
minimo = 1
if nota > 10:
    print("Nota inválida")
elif nota >= promocion:
    print(f"Promoción directa, la nota es {nota}.")
elif nota >= aprobado:
    print(f"Aprobado, la nota es {nota}.")
elif nota < aprobado and nota >= minimo:
    print(f"Desaprobado, la nota es {nota}.")
else:
    print("Nota inválida.")