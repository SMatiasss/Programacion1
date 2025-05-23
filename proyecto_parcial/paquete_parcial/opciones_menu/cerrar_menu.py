def cerrar_menu()-> str:
    """
    Parametros:
        No recibe.
    Función:
        Consulta y valida si el usuario desea finalizar el programa.
    Retorna:
        "s" o "n".
    """

    opcion = input("¿Está seguro que desea cerrar el programa?\n(s/n): ").lower()
    while opcion != "s" and opcion != "n":
        opcion = input("Opción inválida, intente denuevo\n\n¿Está seguro que desea cerrar el programa?\n(s/n): ").lower()
    return opcion