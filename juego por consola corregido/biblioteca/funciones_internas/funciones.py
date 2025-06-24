def verificar_s_n(entrada: str, texto: str)-> bool:
    ''' verifica que "entrada" sea s/n, caso contrario lo vuelve a pedir y 
        retorna True si es "s", False caso contrario.                     
    '''
    while entrada != "s" and entrada != "n":
        entrada = input(f"Opción inválida, intente denuevo.\n{texto}")
    return entrada == "s"

def imprimir_trivia(dato: dict):
    ''' Muestra en pantalla la trivia'''

    print("-" * 58 +f"""\n    {dato["pregunta"]}
    A: {dato["respuesta_a"]}
    B: {dato["respuesta_b"]}
    C: {dato["respuesta_c"]}\n"""+"-" * 58)

def verificar_respuesta_correcta(entrada: str, dato: str)-> bool:
    ''' verifica que "entrada" sea a/b/c , caso contrario lo vuelve a pedir y 
        retorna True si coincide con la respuesta correcta, caso contrario 
        retorna False.                                                      
    '''
    while entrada != "a" and entrada != "b" and entrada != "c":
        entrada = input("Opción inválida, intente denuevo.\n\nIngrese su respuesta: ")
    return entrada == dato

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

def guardar_datos(nombre: str, puntos: int):
    ''' Abre o crea el archivo "Score.csv" y guarda los datos recibidos
    '''
    with open("Score.csv", "a") as puntajes:
        puntajes.write(f"{nombre},{puntos}\n")

guardar = guardar_datos
s_n = verificar_s_n
trivia = imprimir_trivia
resultado = verificar_respuesta_correcta

# def mover(avanzar: bool, posicion: int, tablero: tuple)-> int:
#     if avanzar:
#         posicion += 1
#         while tablero[posicion] != 0:
#             posicion += tablero[posicion]
#     else:
#         posicion -= 1
#         while tablero[posicion] != 0:
#             posicion -= tablero[posicion]
#     return posicion