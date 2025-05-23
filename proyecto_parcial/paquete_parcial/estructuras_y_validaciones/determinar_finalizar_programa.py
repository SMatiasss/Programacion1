def determinar_finalizar_programa()-> str:
    """
    Parametros:
        No recibe.
    Función:
        Consulta y valida al usuario si desea continuar o finalizar el programa.
        Luego, convierte la respuesta en su contrario para el programa principal.
    Retorna:
        "s" o "n".
    """

    opcion = input("¿Desea regresar al menú?\n(s/n): ").lower()
    while opcion != "s" and opcion != "n":
        opcion = input("Opción inválida, intente denuevo\n\n¿Desea regresar al menú?\n(s/n): ").lower()
    if opcion == "s":
        opcion = "n"
    else:
        opcion = "s"
    return opcion