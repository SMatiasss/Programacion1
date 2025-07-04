from .interno import *
from pygame.mixer import music
from random import choice
import pygame as pg

pg.init()

def mostrar_pantalla_inicio(fondo: pg.image, clicado: pg.mixer.Sound, ventana: pg.display)-> bool:
    # pygame
    titulo = pg.transform.scale(pg.image.load("./recursos/Inicio/titulo optimizado 4x.png"), (732, 288))
    serpiente_png = pg.transform.scale(pg.image.load("./recursos/Inicio/serpiente_lengua_dentro4x.png"), (288, 288))
    salir = pg.transform.scale(pg.image.load("./recursos/Inicio/salir.png"), (84, 288))
    escalera_puntaje = pg.transform.scale(pg.image.load("./recursos/Inicio/escalera puntaje 4x.png"), (81, 288))

    # posiciones y areas
    posicion_serpiente = (240,396)
    posicion_puntaje = (87, 396)
    area_serpiente = [pg.Rect(313, 396, 136, 133), pg.Rect(270, 529, 228, 53), pg.Rect(240, 582, 288, 103)]
    pos_titulo = (18, 36)
    posicion_salir = (612, 396)

    #flags
    flags={"encima1": False,
           "encima2": False,
           "encima3": False}
    tabla_puntuaciones = False
    arrancar = True

    rect_salir = salir.get_rect(topleft=posicion_salir)
    rect_puntaje = escalera_puntaje.get_rect(topleft=posicion_puntaje)
    while arrancar:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()

            posicion_mouse = pg.mouse.get_pos()
            flags["encima1"] = rect_puntaje.collidepoint(posicion_mouse)
            flags["encima2"] = rectangulo_clicado(area_serpiente, posicion_mouse)
            flags["encima3"] = rect_salir.collidepoint(posicion_mouse)
            
            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                if flags["encima1"]:
                    clicado.play()
                    tabla_puntuaciones = True
                    arrancar = False
                elif flags["encima2"]:
                    clicado.play()
                    arrancar = False
                elif flags["encima3"]:
                    pg.quit(); quit()

        ventana.blit(fondo, (0, 0))
        ventana.blit(titulo, pos_titulo)
        ventana.blit(salir, (612, 396))
        ventana.blit(serpiente_png, posicion_serpiente)
        if flags["encima1"]:
            ventana.blit(pg.transform.scale(escalera_puntaje, (93, 300)),(81, 390))
        else:
            ventana.blit(escalera_puntaje, (87, 396))

        if flags["encima2"]:
            ventana.blit(pg.transform.scale(serpiente_png, (300, 300)), (posicion_serpiente[0] - 6, posicion_serpiente[1] - 6))
        elif flags["encima3"]:
            ventana.blit(pg.transform.scale(salir, (96, 300)), (606, 390))

        pg.display.flip()
    return tabla_puntuaciones

def mostrar_tabla(fondo: pg.image, clicado: pg.mixer.Sound, ventana: pg.display, fuente_chica: pg.font):
    #variables
    amarillo = (255, 224, 71)
    datos = leer_datos("Score.csv")

    # pygame
    tabla_puntajes = pg.transform.scale(pg.image.load("./recursos/puntuaciones/puntuaciones.png"), (624, 732))
    regresar = pg.transform.scale(pg.image.load("./recursos/puntuaciones/flecha regresar.png"), (60, 60))
    regresar2 = pg.transform.scale(pg.image.load("./recursos/puntuaciones/flecha volver seleccionada.png"), (60, 60))
    fuente_chica = pg.font.Font("./fuente/FieldGuide.ttf", 48)

    # posiciones y areas
    area_regresar = (6, 6)
    pos_tabla = (72, 18)
    rect_regresar = regresar.get_rect(topleft=area_regresar)

    #flags
    encima = False
    arrancar = True
    while arrancar:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            
            posicion_mouse = pg.mouse.get_pos()
            encima = rect_regresar.collidepoint(posicion_mouse)
            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1 and encima:
                clicado.play()
                arrancar = False
        
        ventana.blit(fondo, (0, 0))
        ventana.blit(tabla_puntajes, pos_tabla)
        ventana.blit(regresar, (6, 6))
        if encima:
            ventana.blit(regresar2, (6, 6))

        ventana.blit(fuente_chica.render("Nombre", False, amarillo), (102, 84))
        ventana.blit(fuente_chica.render("Puntos", False, amarillo), (468, 84))
        for indice, (nombre, puntos) in enumerate(datos):
            pos_y = 132 + indice * 60
            ventana.blit(fuente_chica.render(nombre, False, amarillo), (102, pos_y))
            ventana.blit(fuente_chica.render(str(puntos), False, amarillo), (486, pos_y))

        pg.display.flip()

def pedir_nombre(fondo: pg.image, clicado: pg.mixer.Sound, ventana: pg.display, fuente_grande: pg.font)-> str:
    # variables
    max_caracteres = 9
    nombre = ""
    gris = (226, 234, 252)
    pos_nombre = (384, 284)

    # pygame
    marco = pg.transform.scale(pg.image.load("./recursos/trivia/trivia base 4x.png"), (624, 492))
    solicitar_nombre = fuente_grande.render("Ingrese su nombre:", False, gris)  # Ahora gris ya está definido

    # render de entrada
    superficie_nombre = fuente_grande.render(nombre, False, gris)

    # posiciones y areas
    pos_tabla = (72, 18)
    pos_solicitud = (108, 184)
    rect_nombre = superficie_nombre.get_rect(center=pos_nombre)

    # flags
    arrancar = True
    while arrancar:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()

            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN:
                    clicado.play()
                    if nombre == "":
                        nombre = "Desconocido"
                    arrancar = False

                elif evento.key == pg.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    if len(nombre) < max_caracteres and evento.unicode.isprintable():
                        nombre += evento.unicode

                superficie_nombre = fuente_grande.render(nombre, False, gris)
                rect_nombre = superficie_nombre.get_rect(center=pos_nombre)
    
        ventana.blit(fondo, (0, 0))
        ventana.blit(marco, pos_tabla)
        ventana.blit(solicitar_nombre, pos_solicitud)
        ventana.blit(superficie_nombre, rect_nombre)
        pg.display.flip()
    return nombre

def comienzo_partida(fondo: pg.image, ventana: pg.display, tablero: pg.image, peon_png: pg.image , pos_peon: tuple)-> bool:
    # pygame
    tres_segundos = pg.USEREVENT
    pg.time.set_timer(tres_segundos, 3000)

    # posiciones
    posicion_tablero = (66, 36)

    # Flags
    music.stop()
    arrancar = True
    while arrancar:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            if evento.type == tres_segundos:
                pg.time.set_timer(tres_segundos, 0)
                music.load("./recursos/mp3/bgmmain.mp3")
                music.set_volume(0.6)
                music.play(-1)
                arrancar = False

        ventana.blit(fondo, (0,0))
        ventana.blit(tablero, posicion_tablero)
        ventana.blit(peon_png, pos_peon)
        pg.display.flip()

def jugar_trivia(fondo: pg.image, ventana: pg.display, fuentes: dict, preguntas: dict, pos_peon: list, posicion: int)-> tuple:
    # variables
    x_respuestas, y_respuestas = (72, 528)
    espacio_respuestas = 216
    tiempo = 15
    gris = (226, 234, 252)
    amarillo = (255, 224, 71)
    rojo = (255, 155, 155)
    segundo = pg.USEREVENT + 1
    fin_animacion = pg.USEREVENT + 2
    pregunta = choice(preguntas)
    estado = ""

    # pygame
    trivia_base = pg.transform.scale(pg.image.load("./recursos/trivia/trivia base 4x.png"), (624, 492))
    trivia_dorado = pg.transform.scale(pg.image.load("./recursos/trivia/trivia dorado 4x.png"), (624, 492))
    trivia_rojo = pg.transform.scale(pg.image.load("./recursos/trivia/trivia rojo 4x.png"), (624, 492))
    respuesta_base = pg.transform.scale(pg.image.load("./recursos/trivia/boton base 4x.png"), (192, 84))
    respuesta_correcta = pg.transform.scale(pg.image.load("./recursos/trivia/boton correcto 4x.png"), (192, 84))
    respuesta_incorrecta = pg.transform.scale(pg.image.load("./recursos/trivia/boton incorrecto 4x.png"), (192, 84))
    fuente_diminuta = pg.font.Font("./fuente/FieldGuide.ttf", 32)
    

    # renders de texto/números
    render_tiempo = fuentes["grande"].render(str(tiempo), False, gris)
    lineas_pregunta = separar_en_lineas(pregunta["pregunta"], fuentes["chica"], 587)
    lineas_respuestas = [separar_en_lineas(pregunta["respuesta_a"], fuente_diminuta, 184),
                        separar_en_lineas(pregunta["respuesta_b"], fuente_diminuta, 184),
                        separar_en_lineas(pregunta["respuesta_c"], fuente_diminuta, 184)]

    # posiciones y areas
    pos_respuestas = {"a": (x_respuestas, y_respuestas),
                      "b": (x_respuestas + espacio_respuestas, y_respuestas),
                      "c": (x_respuestas + espacio_respuestas * 2, y_respuestas)}

    area_respuestas = {"a": respuesta_base.get_rect(topleft=pos_respuestas["a"]),
                       "b": respuesta_base.get_rect(topleft=pos_respuestas["b"]),
                       "c": respuesta_base.get_rect(topleft=pos_respuestas["c"])}

    # flags
    flags = {"encima1": False, "encima2": False, "encima3": False}
    animacion = False
    arrancar = True
    
    pg.time.set_timer(segundo, 1000)
    preguntas.remove(pregunta)
    while arrancar:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            if not animacion:
                if evento.type == segundo: # actualiza temporizador
                    tiempo -= 1
                    if tiempo > 9:
                        render_tiempo = fuentes["grande"].render(str(tiempo), False, gris)
                    elif tiempo < 0:
                        render_tiempo = fuentes["grande"].render("", False, gris)                # Cuando se termina el tiempo, no se muestra 
                        pregunta, tiempo, render_tiempo, estado, animacion, posicion, pos_peon = logica_movimiento(False, posicion, fuentes["grande"], segundo, fin_animacion)       
                    else:
                        render_tiempo = fuentes["grande"].render("0" + str(tiempo), False, gris) # Agrega un 0 delante al bajar del 10
                
                if tiempo >= 0: # Si no se terminó el tiempo.
                    posicion_mouse = pg.mouse.get_pos()
                    flags["encima1"] = area_respuestas["a"].collidepoint(posicion_mouse)
                    flags["encima2"] = area_respuestas["b"].collidepoint(posicion_mouse)
                    flags["encima3"] = area_respuestas["c"].collidepoint(posicion_mouse)

                    if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1 and (flags["encima1"] or flags["encima2"] or flags["encima3"]):
                        #correcto = lambda x: verificar_respuesta_correcta(x, pregunta["respuesta_correcta"])
                        correcto = devolver_colision(tuple(area_respuestas.values()), evento.pos, ("a", "b", "c"), lambda x: verificar_respuesta_correcta(x, pregunta["respuesta_correcta"]))
                        if correcto != None:
                            pregunta, tiempo, render_tiempo, estado, animacion, posicion, pos_peon = logica_movimiento(correcto, posicion, fuentes["grande"], segundo, fin_animacion)

            else: # animacion = True , eligió respuesta y comienza animacion de correcto o incorrecto
                if evento.type == fin_animacion:
                    pg.time.set_timer(fin_animacion, 0)
                    arrancar = False

        ventana.blit(fondo, (0, 0))
        if animacion:
            if estado == "correcto":
                mostrar_trivia(trivia_dorado, respuesta_correcta, lineas_pregunta, lineas_respuestas, amarillo, ventana, pos_respuestas, flags, fuentes["chica"], fuente_diminuta)
            if estado == "incorrecto":
                mostrar_trivia(trivia_rojo, respuesta_incorrecta, lineas_pregunta, lineas_respuestas, rojo, ventana, pos_respuestas, flags, fuentes["chica"], fuente_diminuta)
        
        else:
            mostrar_trivia(trivia_base, respuesta_base, lineas_pregunta, lineas_respuestas, gris, ventana, pos_respuestas, flags, fuentes["chica"], fuente_diminuta)
            ventana.blit(pg.transform.scale(respuesta_base, (128, 56)), (pos_respuestas["b"][0] + 32, pos_respuestas["b"][1] + 110))
            ventana.blit(render_tiempo, (pos_respuestas["b"][0] + 66, pos_respuestas["b"][1] + 90))

        pg.display.flip()
    return posicion, pos_peon
    
def consultar_continuar(fondo: pg.image, clicado: pg.mixer.Sound, ventana: pg.display, tablero: pg.image, peon_png: pg.image, pos_peon: tuple)-> bool:
    # pygame
    boton_si = pg.transform.scale(pg.image.load("./recursos/desea continuar/boton si.png"), (192, 84))
    boton_no = pg.transform.scale(pg.image.load("./recursos/desea continuar/boton no.png"), (192, 84))
    consulta_continuar = pg.transform.scale(pg.image.load("./recursos/desea continuar/consultar.png"), (624, 84))

    # variables
    y_botones = 678
    x_boton_si = 144

    # posiciones y areas
    posicion_tablero = (66, 36)
    pos_si = x_boton_si, y_botones
    pos_no = x_boton_si * 3, y_botones
    area_si = boton_si.get_rect(topleft=pos_si)
    area_no = boton_no.get_rect(topleft=pos_no)
    
    # flags
    flags = {"encima1": False, "encima2": False}
    arrancar = True
    while arrancar:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()

            posicion_mouse = pg.mouse.get_pos()
            flags["encima1"] = area_si.collidepoint(posicion_mouse)
            flags["encima2"] = area_no.collidepoint(posicion_mouse)

            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                confirmado = devolver_colision((area_si, area_no), evento.pos, ("s", "n"), verificar_s_n)
                if confirmado != None:
                    clicado.play()
                    arrancar = False
        
        ventana.blit(fondo, (0, 0))
        ventana.blit(tablero, posicion_tablero)
        ventana.blit(peon_png, pos_peon)
        ventana.blit(consulta_continuar, (72, y_botones - 102))
        ventana.blit(boton_si, pos_si)
        ventana.blit(boton_no, pos_no)
        if flags["encima1"]:
            ventana.blit(pg.transform.scale(boton_si, (204, 96)), (pos_si[0] - 6, pos_si[1] - 6))
            
        if flags["encima2"]:
            ventana.blit(pg.transform.scale(boton_no, (204, 96)), (pos_no[0] - 6, pos_no[1] - 6))

        pg.display.flip()
    
    return not confirmado

def mostrar_fin(fondo: pg.image, ventana: pg.display, nombre: str, resultado: int, puntos: int):
    # variables
    gris = (226, 234, 252)
    
    # pygame
    fin_del_juego = pg.transform.scale(pg.image.load("./recursos/fin_del_juego.png"), (624, 732))
    fuente = pg.font.Font("./fuente/FieldGuide.ttf", 66)
    fuente_enorme = pg.font.Font("./fuente/FieldGuide.ttf", 480)
    texto_fin = fuente.render("tu puntuacion:", False, gris)

    # posicion
    pos_fin = (72, 18)
    pos_resultado = (387, 72)
    pos_texto_fin = (170, 108)
    pos_puntos = (396, 384)

    victoria = fuente.render("", False, gris)
    if resultado == 1:
        victoria = fuente.render("¡Ganaste!", False, gris)
    elif resultado == 2:
        victoria = fuente.render("¡Perdiste!", False, gris)
    elif resultado == 3:
        victoria = fuente.render("No hay más preguntas", False, gris)
        
    rect_victoria = victoria.get_rect(center=pos_resultado)
    texto_puntos = fuente_enorme.render(str(puntos), False, gris)
    rect_puntos = texto_puntos.get_rect(center=pos_puntos)
    guardar(nombre, puntos)
    ventana.blit(fondo, (0, 0))
    ventana.blit(fin_del_juego, pos_fin)
    ventana.blit(victoria, rect_victoria)
    ventana.blit(texto_puntos, rect_puntos)
    ventana.blit(texto_fin, pos_texto_fin)
    pg.display.flip()
    while True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()

inicio = mostrar_pantalla_inicio
tabla = mostrar_tabla
final = mostrar_fin