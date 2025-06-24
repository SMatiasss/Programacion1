from .funciones_internas import *
from random import choice

def ejecutar_trivia(posicion: int, preguntas: list, tablero: tuple):
    pregunta = choice(preguntas)
    preguntas.remove(pregunta)
    trivia(pregunta)
    correcto = resultado(input("Ingrese su respuesta: "), pregunta["respuesta_correcta"])
    posicion = mover(correcto, posicion, tablero)
    return posicion

def establecer_fin_del_juego(posicion: int, preguntas: list)-> int:
    fin = 0
    if posicion== 30:
        fin = 1
    if posicion== 0:
        fin = 2
    if len(preguntas) == 0:
        fin = 3
    return fin