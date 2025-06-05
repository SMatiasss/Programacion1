def imprimir_3_datos(entrada: list):
    print("-" * 58 + ("\n{:^10}|{:^12}|{:^13}\n").format("Nombre","Apellido","Nota promedio") + "-" * 58)
    nueva_lista = []
    for i in range(len(entrada)):
        nueva_lista.append([entrada[i][0],entrada[i][1],entrada[i][2]])
        print(("{:^10}|{:^12}|{:^13}").format(nueva_lista[i][0],nueva_lista[i][1],nueva_lista[i][2]))

def imprimir_4_datos(entrada: list, nombre: str):
    ancho = len(nombre)
    print("-" * 58 + ("\n{:^8}|{:^10}|{:^12}|" + "{:^" + str(ancho) + "}\n").format(
        "Legajo","Nombre","Apellido", nombre) + "-" * 58)
    for i in range(len(entrada)):
        linea = []
        if type(entrada[i]) == dict:
            for key in entrada[i]: 
                linea.append(entrada[i][key])
            print(("{:^8}|{:^10}|{:^12}|" + "{:^" + str(ancho) + "}").format(linea[0],linea[1],linea[2],linea[3]))
        else:
            print(("{:^8}|{:^10}|{:^12}|" + "{:^" + str(ancho) + "}").format(entrada[i][0],entrada[i][1],entrada[i][2],entrada[i][3]))