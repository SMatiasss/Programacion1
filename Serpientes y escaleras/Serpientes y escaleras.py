from libreria import *
from pygame.mixer import music

while True:

    if not fin_del_juego:
        if not mostrar_pantalla_inicio(fondo, clicado, ventana):

            nombre = pedir_nombre(fondo, clicado, ventana)
            comienzo_partida(fondo, ventana, pos_peon)
            music.play()

            while not fin_del_juego:
                posicion_del_jugador, pos_peon = jugar_trivia(fondo, ventana, preguntas, pos_peon, posicion_del_jugador)
                resultado = establecer_fin_del_juego(posicion_del_jugador, preguntas)
                if resultado == 0:
                    fin_del_juego = consultar_continuar(fondo, clicado, ventana, pos_peon)
                else:
                    fin_del_juego = True
            
        else:
            mostrar_tabla(fondo, clicado, ventana)
    else:
        mostrar_fin(fondo, ventana, nombre, resultado, posicion_del_jugador)