tornillos = [[["to12", 65],["to16", 86],["to20", 65],["to25", 45]],
             [["to30", 68],["to35", 73],["to40", 85],["to45", 89]]]
tarugos = [[["ta4", 58],["ta5", 48],["ta6", 64],["ta7", 96]],
           [["ta8", 36],["ta10", 72],["ta12", 78],["ta14", 71]]]

def mostrar_matriz(matriz: list):
    print("-" * 38)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j][0]}={matriz[i][j][1]}", end="   ")
        print("")

def elegir_tipo_producto():
    opcion = input("-"* 22 + "\n1-Tornillos\n2-Tarugos\n\nElija una opción(0 para cancelar): ")
    while opcion != "1" and opcion != "2" and opcion != "0":
        print("Opción inválida")
        opcion = input("\n1-Tornillos\n2-Tarugos\n\nElija una opción: ")
    return opcion

def elegir_agregar_o_establecer():
    opcion = input("-"* 22 + "\n1-Agregar al stock\n2-Establecer una cantidad\n\nElija una opción(0 para cancelar): ")
    while opcion != "1" and opcion != "2" and opcion != "0":
        print("Opción inválida")
        opcion = input("\n1-Agregar al stock\n2-Establecer una cantidad\n\nElija una opción(0 para cancelar): ")
    return opcion

def elegir_tamaño(eleccion: int)->str:
    objeto = input("\nIngrese su tamaño: ")
    if objeto == "0":
        return objeto
    if eleccion == "1":
        while objeto != "12" and objeto != "16" and objeto != "20" and objeto != "25" and  objeto != "30" and objeto != "35" and objeto != "40" and objeto != "45":
            print("Tamaño inválido, intente denuevo.")
            objeto = input("\nIngrese el tamaño del tornillo: ")
        return "to" + objeto
    else:
        while objeto != "4" and objeto != "5" and objeto != "6" and objeto != "7" and objeto != "8" and objeto != "10" and objeto != "12" and objeto != "14":
            print("Tamaño inválido, intente denuevo.")
            objeto = input("\nIngrese el tamaño de la tarugo: ")
        return "ta" + objeto

def agregar_tornillos(matriz: list, dato1: str, dato2: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if dato1 == matriz[i][j][0]:
                matriz[i][j][1] += dato2

def establecer_cantidad_tornillos(matriz: list, dato1: str, dato2: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if dato1 == matriz[i][j][0]:
                matriz[i][j][1] = dato2

def agregar_tarugos(matriz: list, dato1: str, dato2: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if dato1 == matriz[i][j][0]:
                matriz[i][j][1] += dato2

def establecer_cantidad_tarugos(matriz: list, dato1: str, dato2: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if dato1 == matriz[i][j][0]:
                matriz[i][j][1] = dato2

def vender_mercaderia(matriz:list, dato1: int, dato2: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if dato1 == matriz[i][j][0]:
                if dato2 <= matriz[i][j][1]:
                    matriz[i][j][1] -= dato2
                else:
                    print("La cantidad a vender excede el existente en stock.")

def listar_inventario(matriz):
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista.append(f"{matriz[i][j][0]}: {matriz[i][j][1]}")
    return lista

def cerrar_menu():
    opcion = input("Está seguro que desea finalizar el programa ? (s/n)").lower()
    while opcion != "s" and opcion != "n":
        print("Opción inválida, intente denuevo (s/n).")
        opcion = input("Está seguro que desea finalizar el programa ? (s/n)").lower()
    if opcion == "s":
        return False
    else:
        return True