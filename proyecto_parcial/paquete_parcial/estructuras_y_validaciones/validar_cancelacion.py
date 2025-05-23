def validar_cancelación(entrada: str)-> bool:
    """
    Parametros:
        entrada (string): Cadena de carácteres.
    Función:
        Verifica si el usuario desea cancelar la operación y retorna el resultado.
    Retorna:
        True o False.
    """

    validez = False
    if entrada == "0":
        validez = True
    return validez