from .funciones_internas import *
from random import choice

def ejecutar_trivia(posicion: int, preguntas: list, tablero: tuple):
    ''' Obtiene la pregunta a mostrar y elimina la pregunta de la lista de preguntas.
        devuelve la nueva posicion del usuario
    '''
    pregunta = choice(preguntas)
    preguntas.remove(pregunta)
    trivia(pregunta)
    correcto = resultado(input("Ingrese su respuesta: "), pregunta["respuesta_correcta"])
    posicion = mover(correcto, posicion, tablero)
    return posicion

def establecer_fin_del_juego(posicion: int, preguntas: list, espera: str, nombre: str)-> int:
    ''' Determina si el jugador gana, pierde o se acaban las preguntas y retorna True 
        en caso contrario.
    '''
    
    jugar = True
    if posicion == 30:
        input("\n¡Usted ha ganado!" + espera)
        jugar = False
    elif posicion == 0:
        input("\n¡Usted ha perdido!" + espera)
        jugar = False
    elif len(preguntas) == 0:
        input(f"\n¡Se han acabado las preguntas!\n\n{nombre}, su puntuacion es: {posicion}" + espera)
        jugar = False
    return jugar