from .imprimir_menu import *

def elegir_opcion_menu()-> str:
    """
    Parametros:
        No recibe.
    Función:
        Solicita que el usuario elija una opción y valida que
        introduzca "1", "2", "3", "4" o "5". En caso contrario,
        solicita nuevamente el ingreso.
    Retorna:
        Retorna "1", "2", "3", "4" o "5".
    """

    opcion = input("Ingrese una opción: ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5":
        print("\nOpción inválida, intente denuevo.")
        imprimir_menu()
        opcion = input("Ingrese una opción (1/2/3/4/5): ")
    return opcion