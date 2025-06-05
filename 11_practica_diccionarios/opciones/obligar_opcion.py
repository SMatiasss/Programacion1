def obligar_opcion(entrada: str)-> str:
    no_numero = False
    while no_numero == False:
        while entrada.isdigit() == False:
            entrada = input("Opción inválida, intente denuevo.\nIngrese una opción (1-8): ")
        if int(entrada) >= 1 and int(entrada) <= 8:
            no_numero = True
        else:
            entrada = input("Opción inválida, intente denuevo.\nIngrese una opción (1-8): ")
    return entrada