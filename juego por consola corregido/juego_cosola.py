from biblioteca.datos_y_estructura import *
from biblioteca.juego import *
from biblioteca.funciones_internas.funciones import s_n

if posicion_del_jugador > 0 and posicion_del_jugador < 30:
    jugar = s_n(input(desea_jugar), desea_jugar)
    if jugar:
        nombre = input("Ingrese su nombre: ")
        while jugar:
            if fin == 0:
                posicion_del_jugador = ejecutar_trivia(posicion_del_jugador, preguntas, tablero)
                fin = establecer_fin_del_juego(posicion_del_jugador, preguntas)
                if fin == 0:
                    print(f"Usted se ha movido a la posicion {posicion_del_jugador}")
                    jugar = s_n(input(desea_continuar), desea_continuar)
            else:
                jugar = fin_del_juego(fin, espera, nombre, posicion_del_jugador)
        guardar(nombre, posicion_del_jugador)
        print("\nFinalizando...")
else:
    print("La posicion inicial debe ser mayor a 0 y menor a 30")
