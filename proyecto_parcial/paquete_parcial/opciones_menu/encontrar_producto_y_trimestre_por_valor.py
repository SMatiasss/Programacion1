def encontrar_producto_y_trimestre_por_valor(valor: int, nombres: list, matriz: list)-> list:
    """
    Parametros:
        nombres (list): Lista paralela con nombres.
        matriz (list): Matriz paralela con datos.
    Función:
        Busca el "valor" dentro de "matriz" y almacena los datos
        vinculados de las listas paralelas en una lista nueva.
    Retorna:
        "lista_nueva" con los datos encontrados.
    """

    lista_nueva= []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if valor == matriz[i][j]:
                lista_nueva= [nombres[i], "T"+str(j+1)]
                break
    return lista_nueva