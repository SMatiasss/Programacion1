def verificar_s_n(entrada: str, texto)-> bool:
    while entrada != "s" and entrada != "n":
        entrada = input(f"\nOpción inválida, intente denuevo.\n{texto}\n(s/n): ").lower()
    return entrada == "s"

def imprimir_trivia(preguntas: list, pregunta: dict):
    print("-" * 30 + "\n" + pregunta["pregunta"])
    for letra in ["a", "b", "c"]:
        clave = f"respuesta_{letra}"
        print(f"{letra.upper()}: {pregunta[clave]}")
    print("-" * 30)
    preguntas.remove(pregunta)

def verificar_respuesta(entrada: str, pregunta: dict)-> bool:
    while entrada not in ["a", "b", "c"]:
        entrada = input("Opción inválida, intente denuevo.\n\nIngrese su respuesta (a/b/c): ").lower()
    return entrada == pregunta["respuesta_correcta"]

def avanzar(tablero: list, posicion: list):
    posicion[0] += 1
    if tablero[posicion[0]] != None:
        posicion[0] += tablero[posicion[0]]

def retroceder(tablero: list, posicion: list):
    posicion[0] -= 1
    if tablero[posicion[0]] != None:
        posicion[0] -= tablero[posicion[0]]

def determinar_movimiento(eleccion: bool, tablero: list, posicion: list):
    if eleccion:
        avanzar(tablero, posicion)
    else:
        retroceder(tablero, posicion)
    return posicion

def determinar_victoria_derrota(posicion: list):
    if posicion[0] >= 30:
        posicion[0] = "ganado"
    elif posicion[0] <= 0:
        posicion[0] = "perdido"

def imprimir_resultado(resultado: str)-> bool:
    input("-" * 30 + f"\n¡Usted ha {resultado}!\nIngrese cualquier entrada para continuar:\n")

def imprimir_fin_o_continuar(posicion: int|str, preguntas: list, texto: str)-> bool:
    jugar = False
    if type(posicion) == str:
            imprimir_resultado(posicion)
    else:
        print(f"\nUsted se ha movido a {posicion}")
        if len(preguntas) > 0:
            jugar = s_n(input(texto).lower(),"¿Desea continuar?")
            if not jugar:
                input(f"\nTu puntuación final es: {posicion}\nIngrese cualquier entrada para continuar:\n")
    return jugar

def guardar_puntuacion(nombre: str, puntuacion: int):
    with open("Score.csv", "r+") as puntuaciones:
        puntuaciones.seek(0, 2)
        if puntuacion == "ganado":
            puntuaciones.write(f"{nombre}, 30\n")
        elif puntuacion == "perdido":
            puntuaciones.write(f"{nombre}, 0\n")
        else:
            puntuaciones.write(f"{nombre},{puntuacion}\n")

trivia = imprimir_trivia
s_n = verificar_s_n