from libreria import *
from random import choice
from copy import deepcopy


jugar = s_n(input(pregunta_desea_jugar).lower(),"¿Desea jugar?")
if jugar:
    nombre = input("Ingrese su nombre: ")
    #preguntas_temporal = deepcopy(preguntas)
    fin = True
    while jugar:
        jugar = ejecutar_juego(tablero,posicion,preguntas, choice(preguntas), pregunta_desea_continuar)
        if len(preguntas) <= 0:
            fin = False
            jugar = False
            ejecutar_fin_del_juego(nombre, posicion[0])
            input(f"""
Se han acabado las preguntas {nombre}, tu posicion final es: {posicion[0]}.
Ingrese cualquier entrada para finalizar:
""")
    if fin:
        ejecutar_fin_del_juego(nombre, posicion[0])
