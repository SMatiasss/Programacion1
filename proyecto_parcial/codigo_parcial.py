from paquete_parcial import *

opcion = None #Creación de variable para que el while que utiliza el programa se ejecute.
while opcion != "s":
    print("\n")
    imprimir_menu()
    opcion = elegir_opcion_menu()
    # Almacena el retorno de la función para uso posterior.

    match opcion:
        case "1":
            imprimir_productos_y_ventas(productos, ventas)
            opcion = determinar_finalizar_programa()
            # Almacena el retorno de la función para determinar si el programa continuará funcionando.

        case "2":
            organizado = ordenar_descendente(productos, ventas)
            # Almacena el retorno de la función para uso posterior.
            
            imprimir_tope_tabla()
            for i in range(len(organizado)):
                print(("{:>8}| {:<2}| {:<2}| {:<2}| {:<2}").format(organizado[i][0], organizado[i][1], organizado[i][2], organizado[i][3], organizado[i][4]))
            print("\n")
            # Imprime los datos organizados.

            opcion = determinar_finalizar_programa()
        case "3":
            nombre = input("Ingrese el producto que desea buscar (0 para cancelar): ").upper()
            # Almacena el nombre del producto a buscar.

            if validar_cancelación(nombre):
                nombre = None
                # ^ Vacía la variable

            else:
                nombre = encontrar_ventas_por_nombre(nombre, productos, ventas)
                if nombre == []: #Verifica si la lista está vacía.
                    print("\nProducto inexistente.\n")
                else:
                    imprimir_tope_tabla()
                    print(("{:>8}| {:<2}| {:<2}| {:<2}| {}\n\n").format(nombre[0], nombre[1], nombre[2], nombre[3], nombre[1] + nombre[2] + nombre[3]))
                nombre = None
                opcion = determinar_finalizar_programa()
        case "4":
            valor = input("Ingrese el valor a buscar (ingrese 0 para cancelar): ")
            valor = validar_numero_natural_o_0(valor)
            if validar_cancelación(str(valor)):
                valor = None
            else:
                if valor > 999: # Verifica si el número ingresado está representado en miles y lo convierte en unidades de miles
                    valor = valor // 1000
                    print(valor)
                lista = encontrar_producto_y_trimestre_por_valor(valor, productos, ventas)
                if lista == []:
                    print("El valor ingresado no se encuentra registrado.\n")
                else:
                    print(("\n\n{:>4}| {:<2} |{:<2}").format("Producto", "Trimestre", "Valor de venta"))
                    print(("{:>8}| {:<9} |{:<2}\n\n").format(lista[0], lista[1], valor))
                lista = None
                valor = None
                opcion = determinar_finalizar_programa()
        case "5":
            opcion = cerrar_menu()
            # Ejecuta la función y almacena en la variable "opcion" para uso posterior.