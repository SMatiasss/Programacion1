def verificar_s_n(entrada: str, texto: str)-> bool:
    while entrada != "s" and entrada != "n":
        entrada = input(f"Opción inválida, intente denuevo.\n{texto}")
    return entrada == "s"

def imprimir_trivia(dato: dict):
    print("-" * 58 +f"""\n    {dato["pregunta"]}
    A: {dato["respuesta_a"]}
    B: {dato["respuesta_b"]}
    C: {dato["respuesta_c"]}\n"""+"-" * 58)

def verificar_respuesta_correcta(entrada: str, dato: str)-> bool:
    while entrada != "a" and entrada != "b" and entrada != "c":
        entrada = input("Opción inválida, intente denuevo.\n\nIngrese su respuesta: ")
    return entrada == dato

def mover(avanzar: bool, posicion: int, tablero: tuple)-> int:
    if avanzar:
        posicion += 1
        while tablero[posicion] != 0:
            posicion += tablero[posicion]
    else:
        posicion -= 1
        while tablero[posicion] != 0:
            posicion -= tablero[posicion]
    return posicion

s_n = verificar_s_n
trivia = imprimir_trivia
resultado = verificar_respuesta_correcta