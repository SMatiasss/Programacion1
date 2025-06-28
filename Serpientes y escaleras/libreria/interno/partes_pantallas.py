import pygame as pg
from pygame.mixer import Sound
from .funciones import mover

pg.init()
pg.mixer.init()

def logica_movimiento(correcto: bool, posicion, fuente, segundo, fin_animacion)-> tuple:
    # tuplas
    coordenadas_casilleros = (None, None, (204, 456), (306, 456), (408, 456), None, (612, 456),
                        (612, 354), (510, 354), (408, 354), (306, 354), None, (102, 354),
                        (102, 252), None, None, None, (510, 252), (612, 252),
                        (612, 150), None, (408, 150), (306, 150), None, (102, 150),
                        (102, 48),  (204, 48),  None,  (408, 48),  (510, 48),  None)

    tablero = (0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1,
               0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0)
    
    # Variables
    pos_peon = None
    
    # pygame.mixer
    pg.time.set_timer(segundo, 0)
    sonido_correcto = Sound("./recursos/mp3/correcto.mp3")
    sonido_correcto.set_volume(0.2)
    sonido_incorrecto = Sound("./recursos/mp3/incorrecto.mp3")
    sonido_incorrecto.set_volume(0.55)


    posicion = mover(correcto, posicion, tablero)
    if posicion > 0 and posicion < 30:
        pos_peon = coordenadas_casilleros[posicion]
    if correcto:
        sonido_correcto.play()
        estado = "correcto"

    else:
        sonido_incorrecto.play()
        estado = "incorrecto"

    pg.time.set_timer(fin_animacion, 1000) 
    
    return (None, 15, fuente.render("", False, (0, 0, 0)), estado, True, posicion, pos_peon)

def mostrar_trivia(trivia, opcion, pregunta: list, respuestas: list, color: tuple, ventana, pos_respuestas, flags, fuente_chica, fuente_diminuta):
    ventana.blit(trivia, (72, 18))
    ventana.blit(opcion, (pos_respuestas["a"]))
    ventana.blit(opcion, (pos_respuestas["b"]))
    ventana.blit(opcion, (pos_respuestas["c"]))
    if flags["encima1"]:
        ventana.blit(pg.transform.scale(opcion, (204, 96)), (pos_respuestas["a"][0] - 6, pos_respuestas["a"][1] - 6))

    elif flags["encima2"]:
        ventana.blit(pg.transform.scale(opcion, (204, 96)), (pos_respuestas["b"][0] - 6, pos_respuestas["b"][1] - 6))

    elif flags["encima3"]:
        ventana.blit(pg.transform.scale(opcion, (204, 96)), (pos_respuestas["c"][0] - 6, pos_respuestas["c"][1] - 6))

    for indice, linea in enumerate(pregunta):
        linea = fuente_chica.render(linea, False, color)
        linea_rect = linea.get_rect(center=(768 // 2, (768 // 2 - 200) + 36 * indice))
        ventana.blit(linea, linea_rect)

    for numero, respuesta in enumerate(respuestas):
        x_respuesta = 168
        for indice, linea in enumerate(respuesta):
            y_respuesta = 558
            if len(respuesta) == 1:
                y_respuesta = 566
            linea = fuente_diminuta.render(linea, False, color)
            linea_rect = linea.get_rect(center=(x_respuesta + 216 * numero, y_respuesta + 18 * indice))
            ventana.blit(linea, linea_rect)
            
    #ventana.blit(pg.transform.scale(opcion, (128, 56)), (pos_respuestas["b"][0] + 32, pos_respuestas["b"][1] + 110))
    #ventana.blit(tiempo_s, (pos_respuestas["b"][0] + 66, pos_respuestas["b"][1] + 90))
