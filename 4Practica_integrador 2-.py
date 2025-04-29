# Tabla de Posiciones de Torneo de Ping-Pong
# Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.

# Los datos que se cargarán son:

# Nombre del jugador
# Edad (validar)
# Cantidad de puntos (validar-número entero positivo, hasta 60).
# Número de partidos ganados (validar-número entero positivo, hasta 35).
# Tipo de saque ("plano", "liftado", "cortado")
# Categoría ("elite", "experto", "avanzado")

# Se necesita saber

# Tema A:
# 1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años inclusive.
# 2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
# 3-Porcentaje de jugadores de categoría "experto".
# 4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
# 5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”.

nombre = input("Ingrese el nombre del jugador (ingrese 0 para finalizar/cancelar): ")
contador = 0
while nombre != "0":
    edad = int(input(" \nIngrese la edad del jugador (ingrese 0 para cancelar): "))
    if edad == 0:
        nombre = "0"
    elif edad >= 13 and edad <= 55:
        puntaje = int(input(" \nIngrese su puntaje: "))
        while puntaje < 0 or puntaje > 60:
            print("Puntaje inválido, intente denuevo.")
            puntaje = int(input(" \nIngrese su puntaje: "))
        
        partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
        while partidos_ganados < 0 or partidos_ganados > 35:
            print("Número inválido, intente denuevo.")
            partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
        
        saque = input('Ingrese el tipo de saque que utiliza ("plano", "liftado", "cortado"): ').lower()
        while saque != "plano" and saque != "liftado" and saque != "cortado":
            print("Tipo de saque inválido, intente denuevo.")
            saque = input('Ingrese el tipo de saque que utiliza ("plano", "liftado", "cortado"): ').lower()
        
        categoria = input('Ingrese la categoría a la que pertenece ("elite", "experto", "avanzado")').lower()
        while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
            print("Categoría inválida, intente denuevo.")
            categoria = input('Ingrese la categoría a la que pertenece ("elite", "experto", "avanzado")').lower()
        
        menor_edad = 999
        menor_nombre = 0
        menor_categoria = 0
        contador1 = 0
        contador_plano = 0
        contador_liftado = 0
        contador_cortado = 0
        contador_experto = 0
        contador_elite = 0
        contador_avanzado = 0
        suma_avanzado = 0
        
        if puntaje > 50 and edad < menor_edad:
            menor_edad = edad
            menor_nombre = nombre
            menor_categoria = categoria
        match categoria:
            case "elite":
                contador_elite +=1
                if edad >= 19 and edad <= 25 and saque == "plano":
                    contador1 += 1
                match saque:
                    case "plano":
                        contador_plano += 1
                    case "liftado":
                        contador_liftado += 1
                    case "cortado":
                        contador_cortado += 1
            case "experto":
                contador_experto += 1
            case "avanzado":
                    contador_avanzado += 1
                    suma_avanzado += edad

        contador += 1
    else:
        print("Esta edad no se encuentra dentro del rango permitido para participar.")
    edad = "0"
    nombre = input("Ingrese el nombre del jugador (ingrese 0 para finalizar/cancelar): ")

print(contador)

#1
if contador1 != 0:
    print(f" \nLa cantidad de jugadores de elite con saque plano de entre 19 y 25 años inclusive es de: {contador1}.")
else:
    print(" \nNo hay jugadores de elite con saque plano de entre 19 y 25 años inclusive.")
#2
if menor_nombre == 0:
    print("No hay jugador con más de 50 puntos.")
else:
    print(f" \nEl jugador con mas de 50 puntos y menor edad se llama {menor_nombre} y pertenece a la categoria {menor_categoria}.")

#3
if contador_experto != 0:
    porc_expertos = contador_experto * 100 / contador
    print(f" \nHay un {porc_expertos}% de categoria experto respecto a la totalidad de jugadores.")
else:
    print(" \nNo hay jugadores expertos.")

#4
if contador_avanzado != 0:
    prom_edad_avanzados = suma_avanzado / contador_avanzado
    print(f" \nEl promedio de edad de los jugadores avanzados es: {prom_edad_avanzados}.")
else:
    print(" \nNo hay jugadores avanzados.")

#5
if contador_elite != 0:
    cant_saque_mas_usado_expertos = contador_plano
    saque_mas_usado_expertos = "plano"

    if contador_liftado > cant_saque_mas_usado_expertos:
        cant_saque_mas_usado_expertos = contador_liftado
        saque_mas_usado_expertos = "liftado"
    if contador_cortado > cant_saque_mas_usado_expertos:
        cant_saque_mas_usado_expertos = contador_cortado
        saque_mas_usado_expertos = "cortado"

    print(f" \nEl saque mas usado por los de categoría elite es el: {saque_mas_usado_expertos}.")
else:
    print("No hay jugadores de elite.")
