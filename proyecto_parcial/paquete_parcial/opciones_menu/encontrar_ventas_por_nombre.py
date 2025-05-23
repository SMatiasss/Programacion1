def encontrar_ventas_por_nombre(entrada:str, nombres: list, matriz: list)-> list:
    """
    Parametros:
        entrada (string): cadena de caracteres.
        nombres (list): Lista_nuevaparalela con nombres.
        matriz (list): Matriz paralela con datos.
    Función:
        Busca la "entrada" dentro de "nombres" y almacena los datos
        vinculados de las listas paralelas en una lista_nueva.
    Retorna:
        "lista_nueva" con los datos encontrados.
    """

    lista_nueva= []
    for i in range(len(nombres)):
        if entrada == nombres[i]:
            lista_nueva= [nombres[i], matriz[i][0], matriz[i][1], matriz[i][2]]
            break
    return lista_nueva