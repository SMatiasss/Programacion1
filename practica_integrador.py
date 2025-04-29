# UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo
# en Python, que promete revolucionar el mercado.
# Las posibles aplicaciones son las siguientes:
# ● Inteligencia artificial (IA),
# ● Realidad virtual/aumentada (RV/RA),
# ● Internet de las cosas (IOT)
# Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.
# A) Los datos a ingresar por cada empleado encuestado son:
# ● nombre del empleado
# ● edad (no menor a 18)
# ● género (Masculino - Femenino - Otro)
# ● tecnologia (IA, RV/RA, IOT)
# B) Cargar por terminal 10 encuestas.
# C) Determinar:
# 1. Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
# 2. Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre
# entre los 33 y 40.
# 3. Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.

edad = 0
cantidad_encuestas = 10
for i in range(cantidad_encuestas):
    nombre = input("Ingrese su nombre: ")
    while edad < 18:
        edad = int(input(" \nIngrese su edad no menor a 18 años: "))
        if edad < 18:
            print(" \nEdad incorrecta (menor a 18 años), intente denuevo.\n" + "-" * 50)
            nombre = input("Ingrese su nombre: ")
    edad_max = 0
    genero = None
    while genero != "masculino" and genero != "femenino" and genero != "otro":
        genero = input(" \nIngrese su género (Masculino/Femenino/otro): ").lower()
        if genero != "masculino" and genero != "femenino" and genero != "otro":
            print(' \nOpción inválida, intente denuevo (si su genero no es masculino ni femenino, escriba "otro").')
    voto = True
    while voto:
        print(" \nElija una tecnología a votar (solo escriba sus iniciales):")
        print("\nIA_ Inteligencia Artificial.\nRV/RA_ Realidad Virtual/Aumentada.")
        tecnologia = input("IOT_ Internet de las cosas.\n \nopción: ").lower()
        if tecnologia != "ia" and tecnologia != "rv" and tecnologia != "ra" and tecnologia != "rv/ra" and tecnologia != "iot":
            print("Opción inválida, intente denuevo.")
        else:
            voto = False
        print("-" * 50)
    voto = True
    contador_a = 0
    contador_b = 0
    if genero == "masculino" and edad >= 25 and edad <= 50 and (tecnologia == "ia" or tecnologia == "iot"):
        contador_a += 1
    if tecnologia != "ia" and (genero != "femenino" or (edad < 33 or edad > 40)):
        contador_b += 1
    if edad > edad_max and genero == "masculino":
        edad_max = edad
        nombre_mayor = nombre
        tecnologia_mayor = tecnologia
    edad = 0
porcentaje_b = contador_b * 100 / cantidad_encuestas

#1
print(f" \nEmpleados masculinos que han votado por IOT o IA de entre 25 y 50 años inclusive: {contador_a}")
#2
print(f" \nEmpleados que no han votado por IA cuya edad no se encuentra entre 33 y 40 años y/o no sean femeninos: {porcentaje_b}%")
#3
print(f" \nEl empleado masculino con mayor edad se llama {nombre_mayor} y votó por la tecnología {tecnologia_mayor}")