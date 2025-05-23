def calcular_promedio(lista: list, valor: int)-> bool:
    # Parametros formales: 
    # "lista", recibe una lista de numeros.
    # "valor", recibe un numero entero.
    acumulador = 0
    for numero in lista:
        acumulador += numero
    es_mayor = False
    if valor < acumulador // len(lista):
        es_mayor = True
    return es_mayor

entrada = [10, 20, 30, 40]
valor = 24
print(calcular_promedio(entrada, valor)) # Parametros reales "entrada" ([10, 20, 30, 40]) y "valor" (26)
      #^ Invoca a la función. 