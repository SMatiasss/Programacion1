from funciones_almacen import *
alta = True
opcion = None
while opcion != False:
    opcion = input("-" * 10 + "\nBienvenido\n" + "-" * 10 + "\n1-Alta de productos\n2-Baja de productos\n3-Modificar productos\n4-Listar productos\n5-Listar productos por nombre ascendente.\n6-Salir\n\nIngrese una opción: ")
    if alta:
        match opcion:
            case "6":
                print("")
                opcion = cerrar_menu()
                if opcion == False:
                    print("\nFinalizando programa.")
            case "1":
                producto = input("Ingrese el nombre del producto que desea dar de alta (siempre en singular, ingrese 0 para cancelar): ").lower()
                if producto == "0":
                    producto = None
                    print("Operación cancelada.")
                else:
                    alta = crear_nuevo_producto(stock, producto)
                    producto = None
            case "2" | "3" | "4" | "5":
                print("Debe realizar el alta de almenos 1 producto para utilizar las demás opciones.")
            case _:
                print("Opción inválida, intente denuevo.\n")
    else:
        match opcion:
            case "1":
                producto = input("Ingrese el nombre del producto que desea dar de alta (siempre en singular, ingrese 0 para cancelar): ").lower()
                if producto == "0":
                    producto = None
                    print("Operación cancelada.")
                else:
                    crear_nuevo_producto(stock, producto)
                    producto = None
            case "2":
                for i in range(len(stock)):
                    for j in range(len(stock[i])):
                        if stock[i][j][0] == None:
                            print("Vacio", end="  ")
                        else:
                            print(f"{stock[i][j][0]} = {stock[i][j][1]}", end="  ")
                    print("")
                producto = input("\nIngrese el nombre del producto que desea dar de baja (siempre en singular, ingrese 0 para cancelar): ").lower()
                if producto == "0":
                    producto = None
                    print("Operación cancelada.")
                else:
                    eliminar_producto(stock, producto)
                    producto = None
            case "3":
                for i in range(len(stock)):
                    for j in range(len(stock[i])):
                        if stock[i][j][0] == None:
                            print("Vacio", end="  ")
                        else:
                            print(f"{stock[i][j][0]} = {stock[i][j][1]}", end="  ")
                    print("")
                producto = input("\nIngrese el nombre del producto que desea modificar (siempre en singular, ingrese 0 para cancelar): ").lower()
                encontrado = True
                while (encontrado and producto != "0") or (producto == "vacio" or producto == "vacío"):
                    if producto == "vacio" or producto == "vacío":
                        print('"Vacío" no puede ser modificado, si desea agregar un producto seleccione la opción 1 en el inicio.')
                        producto = input("\nIngrese el nombre del producto que desea modificar (siempre en singular, ingrese 0 para cancelar): ").lower()
                    else:
                        for i in range(len(stock)):
                            for j in range(len(stock[i])):
                                if producto == stock[i][j][0]:
                                    cantidad_existente = stock[i][j][1]
                                    ubicacion_i = i
                                    ubicacion_j = j
                                    encontrado = False
                        if encontrado:
                            print("El producto no se encuentra en el stock, intente denuevo")
                            producto = input("\nIngrese el nombre del producto que desea modificar (siempre en singular, ingrese 0 para cancelar): ").lower()
                encontrado = None
                if producto == None:
                    pass
                elif producto == "0":
                    producto = None
                    print("Operación cancelada.\n")
                else:
                    opcion2 = input(f"\n1-Modificar cantidad de {producto}\n2-Modificar ubicación de {producto}\n0-Cancelar\n\nIngrese una opción: ")
                    match opcion2:
                        case "0":
                            producto = None
                            opcion2 = None
                            print("Operación cancelada.\n")
                        case "1":
                            cantidad = int(input(f"Ingrese la cantidad a establecer en el stock para {producto} (-1 para cancelar): "))
                            if cantidad == -1:
                                cantidad = None
                                producto = None
                                print("Operación cancelada.")
                            else:
                                actualizar_cantidad(stock, producto, cantidad)
                                cantidad = None
                                producto = None
                        case "2":
                            encontrado = True
                            while encontrado:
                                fila = (int(input(f'Ingrese la fila a colocar en el stock "{producto}(0 para cancelar)": '))) - 1
                                if fila == -1:
                                    print("Operación cancelada.")
                                    encontrado = False
                                    producto = None
                                columna = (int(input(f'Ingrese la columna a colocar en el stock "{producto}(0 para cancelar)": '))) - 1
                                if columna == -1:
                                    print("Operación cancelada.")
                                    encontrado = False
                                    producto = None
                                elif stock[fila][columna][0] != None:
                                    print(f"La ubicación en la fila {fila}, columna {columna} se encuentra ocupada por {stock[fila][columna][0]}\nIntente denuevo.")
                                else:
                                    encontrado = False
                                    actualizar_ubicacion(stock, producto, cantidad_existente, ubicacion_i, ubicacion_j, fila, columna)
                                    ubicacion_i = None
                                    ubicacion_j = None
                            encontrado = None
                        case _:
                            print("Opción inválida, intente denuevo.")
                            opcion2 = input(f"\n1-Modificar cantidad de {producto}\n2-Modificar ubicación de {producto}\n0-Cancelar\n\nIngrese una opción: ")
            case "4":
                lista = listar_productos(stock)
                for producto in lista:
                    print(producto)
            case "5":
                for producto in ordenar_lista_productos_ascendente_nombre():
                    print(producto)
            case "6":
                print("")
                opcion = cerrar_menu()
                print("\nFinalizando programa.")