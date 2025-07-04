def rectangulo_clicado(rectangulos: list, posicion_mouse: tuple)-> bool:
    clicado = False
    for rectangulo in rectangulos:
        if rectangulo.collidepoint(posicion_mouse):
            clicado = True
            break
    return clicado

def leer_datos(archivo: str)-> list:
    lineas = []
    with open(archivo, "r") as puntajes:
        puntajes.readline()
        while True:
            linea = puntajes.readline()
            if linea == "":
                break
            for indice, caracter in enumerate(linea):
                if caracter == ",":
                    lineas.append([linea[:indice], int(linea[indice+1:])])
                    break
    return lineas

def devolver_colision(rectangulos: tuple, posicion_mouse: tuple, opciones: tuple, funcion)-> bool:
    colision = None
    for indice, rectangulo in enumerate(rectangulos):
        if rectangulo.collidepoint(posicion_mouse):
            colision = funcion(opciones[indice])
    return colision

def verificar_respuesta_correcta(entrada: str, dato: str)-> bool:
    ''' verifica que "entrada" sea a/b/c , caso contrario lo vuelve a pedir y 
        retorna True si coincide con la respuesta correcta, caso contrario 
        retorna False.                                                      
    '''
    while entrada != "a" and entrada != "b" and entrada != "c":
        pass
        # entrada = input("Opción inválida, intente denuevo.\n\nIngrese su respuesta: ")
    return entrada == dato

def separar_en_lineas(texto: str, fuente, max_ancho: int)-> list:
    empezar = 0
    palabras = []
    if len(texto) < 2:
        palabras.append(texto)

    else:
        for indice, letra in enumerate(texto):
            if letra == " " or indice == len(texto) - 1:
                if indice == len(texto) - 1 and letra != " ":
                    palabras.append(texto[empezar+1:indice+1])

                else:
                    palabras.append(texto[empezar+1:indice])
                    empezar = indice

        palabras[0] = texto[0] + palabras[0]
        
    lineas = []
    linea = [""]
    for palabra in palabras:
        chequear_linea = "" + linea[0] + palabra
        if fuente.size(chequear_linea)[0] <= max_ancho:
            linea[0] += palabra + " "
            
        else:
            linea[0] = linea[0][:-1]
            lineas.append(linea[0])
            linea = [palabra + " "]
            
    if linea != "":
        lineas.append(linea[0][:-1])

    return lineas

def mover(avanzar: bool, posicion: int, tablero: tuple)-> int:
    ''' Establece si avanza o retrocede, realiza el movimiento adecuado
        y lo retorna.
    '''
    direccion = 1
    if not avanzar:
        direccion = -1
    posicion += direccion
    while tablero[posicion] != 0:
        posicion += (tablero[posicion] * direccion)
    return posicion

def establecer_fin_del_juego(posicion: int, preguntas: list)-> int:
    ''' Determina si el jugador gana, pierde o se acaban las preguntas y retorna True 
        en caso contrario.
    '''
    jugar = 0
    if posicion == 30:
        #input("\n¡Usted ha ganado!" + espera)
        jugar = 1
    elif posicion == 0:
        #input("\n¡Usted ha perdido!" + espera)
        jugar = 2
    elif len(preguntas) == 0:
        #input(f"\n¡Se han acabado las preguntas!\n\n{nombre}, su puntuacion es: {posicion}" + espera)
        jugar = 3
    return jugar

def verificar_s_n(entrada: str)-> bool:
    ''' verifica que "entrada" sea s/n, caso contrario lo vuelve a pedir y 
        retorna True si es "s", False caso contrario.                     
    '''
    while entrada != "s" and entrada != "n":
        pass
        # entrada = input(f"Opción inválida, intente denuevo.\n{texto}")
    return entrada == "s"

def guardar_datos(nombre: str, puntos: int):
    ''' Abre o crea el archivo "Score.csv" y guarda los datos recibidos
    '''
    with open("Score.csv", "a") as puntajes:
        puntajes.write(f"{nombre},{puntos}\n")

guardar = guardar_datos

###
# def mover(eleccion: bool, posicion: list):
#     if eleccion:
#         if posicion[0] == 615:
#             posicion[0] -= (102 * 5)
#             posicion[1] -= 102
#         else:
#             posicion[0] += 102
#     else:
#         if posicion[0] == 105:
#             posicion[0] += (102 * 5)
#             posicion[1] += 102
#         else:
#             posicion[0] -= 102
###