def verificar_tesoro(mapa: list, x: int, y: int) -> int:
    encontrado = 1
    if mapa[y][x == 1:
        encontrado = 0
    return encontrado

continuar = True
while continuar:
    x_usuario = input("Ingrese una coordenada x (entre 1 y 5 inclusive.): ")
    while x_usuario != "1" and x_usuario != "2" and  x_usuario != "3" and x_usuario != "4" and x_usuario != "5":
        x_usuario = input("Número inválido, intente denuevo.\n\nIngrese una coordenada x (entre 1 y 5 inclusive.): ")
    y_usuario = input("Ingrese una coordenada y (entre 1 y 5 inclusive.): ")
    while y_usuario != "1" and y_usuario != "2" and  y_usuario != "3" and y_usuario != "4" and y_usuario != "5":
        y_usuario = input("Número inválido, intente denuevo.\n\nIngrese una coordenada y (entre 1 y 5 inclusive.): ")

    mapa = [[0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    
    if verificar_tesoro(mapa, int(x_usuario) - 1, int(y_usuario) - 1) == 0:
        print("¡Encontraste el tesoro!")
        continuar = False
    else:
        x_tesoro = 4
        y_tesoro = 2
        distancia = (int(x_usuario) - x_tesoro) + (int(y_usuario) - y_tesoro)
        if distancia < 0:
            distancia *= -1
        x_usuario = None
        y_usuario = None
        print(f"\nFallaste. El tesoro está a {distancia} casilleros de distancia.")
        opcion = input("\n¿Desea continuar ?\n(s/n): ").lower()
        while opcion != "s" and opcion != "n":
            opcion = input("Opción inválida, intente denuevo.\n\n¿Desea continuar ?\n(s/n): ").lower()
        if opcion == "n":
            continuar = False
print("\nFinalizando programa")
