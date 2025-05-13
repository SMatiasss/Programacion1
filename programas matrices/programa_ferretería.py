from funciones_ferreteria import *
opcion = None
while opcion != False:
    opcion = input("-" * 10 + "\nBienvenido\n" + "-" * 10 + "\n1-Reponer mercadería\n2-Vender mercadería\n3- Listar inventario\n4- Salir\n\nIngrese una opción: ")
    match opcion:
        case "1":
            opcion= elegir_tipo_producto()
            if opcion == "0":
                print("Operación cancelada")
            else:
                opcion2 = elegir_agregar_o_establecer()
                if opcion2 == "0":
                    opcion2 = None
                    print("Operación cancelada")
                else:
                    match opcion:
                        case "1":
                            mostrar_matriz(tornillos)
                            objeto = elegir_tamaño(opcion)
                            if objeto == "0":
                                print("Operacion cancelada")
                                opcion2 = None
                                objeto = None
                            elif opcion2 == "1":
                                cantidad = int(input("Ingrese la cantidad a agregar (0 para cancelar): "))
                                if cantidad == 0:
                                    print("Operacion cancelada")
                                else:
                                    agregar_tornillos(tornillos, objeto, cantidad)
                                opcion2 = None
                                objeto = None
                                cantidad = None
                            else:
                                cantidad = int(input("Ingrese la cantidad a establecer (0 para cancelar): "))
                                if cantidad == 0:
                                    print("Operacion cancelada")
                                else:
                                    establecer_cantidad_tornillos(tornillos, objeto, cantidad)
                                opcion2 = None
                                objeto = None
                                cantidad = None
                        case "2":
                            mostrar_matriz(tarugos)
                            objeto = elegir_tamaño(opcion)
                            if objeto == "0":
                                print("Operacion cancelada")
                                opcion2 = None
                                objeto = None
                            elif opcion2 == "1":
                                cantidad = int(input("Ingrese la cantidad a agregar (0 para cancelar): "))
                                if cantidad == 0:
                                    print("Operacion cancelada")
                                else:
                                    agregar_tarugos(tarugos,objeto,cantidad)
                                objeto = None
                                cantidad = None
                            else:
                                cantidad = int(input("Ingrese la cantidad a establecer (0 para cancelar): "))
                                if cantidad == 0:
                                    print("Operacion cancelada")
                                else:
                                    establecer_cantidad_tarugos(tarugos,objeto,cantidad)
                                opcion2 = None
                                objeto = None
                                cantidad = None
            opcion = None
            opcion2 = None
        case "2":
            opcion= elegir_tipo_producto()
            if opcion == "0":
                print("Operación cancelada")
            else:
                if opcion == "1":
                    mostrar_matriz(tornillos)
                else:
                    mostrar_matriz(tarugos)
                objeto = elegir_tamaño(opcion)
                if objeto == "0":
                    print("Operacion cancelada")
                    opcion2 = None
                    objeto = None
                else:
                    venta = int(input(f"Ingrese cuantos {objeto}, desea vender: "))
                    if opcion == "1":
                        vender_mercaderia(tornillos, objeto, venta)
                        opcion2 = None
                        objeto = None
                        venta = None
                    else:
                        vender_mercaderia(tarugos, objeto, venta)
                        opcion2 = None
                        objeto = None
                        venta = None
            opcion = None
        case "3":
            opcion = elegir_tipo_producto()
            if opcion == "0":
                print("Operación inválida.")
                opcion = None
            if opcion == "1":
                flag = True
                if flag:
                    lista_tornillos = listar_inventario(tornillos)
                    flag = False
                print("")
                for i in lista_tornillos:
                    print(i)
            elif opcion == "2":
                flag2 = True
                if flag2:
                    lista_tarugos = listar_inventario(tarugos)
                    flag2 = False
                print("")
                for i in lista_tarugos:
                    print(i)    
        case "4":
            opcion = cerrar_menu()
            