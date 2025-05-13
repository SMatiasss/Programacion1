stock = [[[None,None],["botella", 3],[None, None],["frasco", 8],[None, None]],
         [[None,None],[None, None],["fideo", 4],[None, None],[None, None]],
         [[None,None],[None, None],[None, None],["leche", 6],[None, None]]]

def crear_nuevo_producto(matriz: list, dato: str)->bool:
    encontrado = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if dato == matriz[i][j][0]:
                print(f"El producto ya se encuentra en stock, en la fila {i+1}, columna {j+1}")
                encontrado = False
    if encontrado:
        fila = None
        columna = None
        while True:
            fila = (int(input("Ingrese la fila en la que desea guardar el producto (0 para cancelar): "))) - 1
            while fila < - 1:
                print("La fila no puede ser menor a 1, intente denuevo.\n")
                fila = (int(input("Ingrese la fila en la que desea guardar el producto (0 para cancelar): "))) - 1
            if fila == -1:
                print("Operación cancelada con éxito")
                return True
            columna = (int(input("Ingrese la columna en la que desea guardar el producto (0 para cancelar): "))) - 1
            while columna < - 1:
                print("La fila no puede ser menor a 1, intente denuevo.\n")
                columna = (int(input("Ingrese la columna en la que desea guardar el producto (0 para cancelar): "))) - 1
            if columna == - 1:
                print("Operación cancelada con éxito")
                return True
            elif matriz[fila][columna][0] == None:
                matriz[fila][columna][0] = dato
                matriz[fila][columna][1] = 0
                print(f'\nUsted ha dado de alta "{dato}" con éxito, tiene una cantidad en stock de:  {matriz[fila][columna][1]}')
                return False
            else:
                print(f'\nYa existe el producto "{matriz[fila][columna][0]}", en ese lugar, por favor intente denuevo\n')
                return False

def eliminar_producto(matriz: list, dato: str):
    encontrado = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if dato == matriz[i][j][0]:
                encontrado = False
                matriz[i][j][0] = None
                matriz[i][j][1] = None
                print(f'Se ha dado de baja "{dato}" con éxito.')
    if encontrado:
        print("No se ha encontrado el producto ingresado en el stock.")

def actualizar_cantidad(matriz: list, dato1: str, dato2: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if dato1 == matriz[i][j][0]:
                matriz[i][j][1] = dato2

def actualizar_ubicacion(matriz: list, dato: str, dato2: int,fila_vieja: int, columna_vieja:int, fila: int, columna: int):
    matriz[fila][columna][0] = dato
    matriz[fila][columna][1] = dato2
    matriz[fila_vieja][columna_vieja][0] = None
    matriz[fila_vieja][columna_vieja][1] = None

def listar_productos(matriz:list)->list:
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j][0] != None:
                nombre = matriz[i][j][0]
                numero = matriz[i][j][1]
                lista.append(f"{nombre}: {numero}")
    return lista

def ordenar_lista_productos_ascendente_nombre()->list:
    lista = listar_productos(stock)
    for i in range((len(lista))- 1):
        for j in range(1,len(lista)):
            if lista[j] < lista[i]:
                contenedor = lista[i]
                lista[i] = lista[j]
                lista[j] = contenedor
    return lista

def cerrar_menu()->bool:
    opcion = input("Está seguro que desea finalizar el programa ? (s/n)").lower()
    while opcion != "s" and opcion != "n":
        print("Opción inválida, intente denuevo (s/n).")
        opcion = input("Está seguro que desea finalizar el programa ? (s/n)").lower()
    if opcion == "s":
        return False
    else:
        return True