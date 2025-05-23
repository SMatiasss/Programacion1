def validar_numero_natural_o_0(entrada: str)-> int:
    """
    Parametros:
        entrada (string): Cadena de carácteres.
    Función:
        Verifica y valida que la entrada recibida solo posea números de 0 a 9.
        En caso contrario, solicita nuevamente el
    Retorna:
        "entrada" convertido en entero.
    """
    
    while entrada.isdigit() == False: 
        entrada = input("Valor inválido, intente denuevo.\n\nIngrese el valor a buscar (número/0 para cancelar): ")
    return int(entrada)