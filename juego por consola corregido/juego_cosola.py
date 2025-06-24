from biblioteca.datos_y_estructura import *
from biblioteca.juego import *
from biblioteca.funciones_internas.funciones import s_n

if posicion_del_jugador > 0 and posicion_del_jugador < 30:
    jugar = s_n(input(desea_jugar), desea_jugar)
    if jugar:
        nombre = input("Ingrese su nombre: ")
        while jugar:
            posicion_del_jugador = ejecutar_trivia(posicion_del_jugador, preguntas, tablero)
            jugar = establecer_fin_del_juego(posicion_del_jugador, preguntas, espera, nombre)
            if jugar:
                print(f"Usted se ha movido a la posicion {posicion_del_jugador}")
                jugar = s_n(input(desea_continuar), desea_continuar)
                if not jugar:
                    input(f"\nUsted ha finalizado en la posición: {posicion_del_jugador}." + espera)
        guardar(nombre, posicion_del_jugador)
    print("\nFinalizando...")
else:
    print("La posicion inicial debe ser mayor a 0 y menor a 30")
