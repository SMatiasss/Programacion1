from libreria import *
from pygame.mixer import music

music.play(-1)
while True:

    if not fin_del_juego:
        if not inicio(fondo, clicado, ventana):

            nombre = pedir_nombre(fondo, clicado, ventana, fuentes["grande"])
            comienzo_partida(fondo, ventana, tablero, peon_png, pos_peon)

            while not fin_del_juego:
                posicion_del_jugador, pos_peon = jugar_trivia(fondo, ventana, fuentes, preguntas, pos_peon, posicion_del_jugador)
                resultado = establecer_fin_del_juego(posicion_del_jugador, preguntas)
                if resultado == 0:
                    fin_del_juego = consultar_continuar(fondo, clicado, ventana, tablero, peon_png, pos_peon)
                else:
                    fin_del_juego = True
            
        else:
            tabla(fondo, clicado, ventana, fuentes["chica"])
    else:
        final(fondo, ventana, nombre, resultado, posicion_del_jugador,)