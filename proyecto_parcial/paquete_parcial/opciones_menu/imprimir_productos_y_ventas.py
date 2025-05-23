def imprimir_productos_y_ventas(nombres: list, matriz: list):
    """
    Parametros:
        nombres (list): Lista paralela con nombres.
        matriz (list): Matriz paralela con datos.
    Función:
        Imprime los datos paralelos recibidos en forma de cuadro.
    Retorna:
        No retorna.
    """

    print(("\n\n" +"-" * 27 + "\n{:>8}| {:<2}| {:<2}| {:<2}| Total\n" + "-" * 27).format("Producto","T1","T2","T3"))
    for i in range(len(nombres)):
        print(("{:>8}| {:<2}| {:<2}| {:<2}| {:<2}").format(nombres[i], matriz[i][0], matriz[i][1], matriz[i][2], (matriz[i][0] + matriz[i][1] + matriz[i][2])))
    print("")