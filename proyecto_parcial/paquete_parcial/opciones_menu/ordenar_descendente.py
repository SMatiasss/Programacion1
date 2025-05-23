def ordenar_descendente(nombres: list, matriz: list)-> list:
    """
    Parametros:
        nombres (list): Lista paralela con nombres.
        matriz (list): Matriz paralela con datos.
    Función:
        Ordena de manera descendente los datos paralelos en una lista nueva.
    Retorna:
        "lista_nueva" con los datos ordenados.
    """

    lista_nueva = []
    for i in range(len(matriz)):
        lista_nueva.append([nombres[i], matriz[i][0], matriz[i][1], matriz[i][2] , matriz[i][0] + matriz[i][1] + matriz[i][2]])
    for i in range(len(lista_nueva)-1):
        for j in range(i + 1, len(lista_nueva)):
            if lista_nueva[j][-1] > lista_nueva[i][-1]:
                contenedor = lista_nueva[i]
                lista_nueva[i] = lista_nueva[j]
                lista_nueva[j] = contenedor
                break
    return lista_nueva