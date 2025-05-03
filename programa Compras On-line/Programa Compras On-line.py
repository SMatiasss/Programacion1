from listas_personas import *
from funciones_compras_online import *
importado = False
opcion = None
print("-" * 100)
while opcion != "0":
    print(" \nBienvenido a la tienda on-line\n " + "\n" + "-" * 100 + "\n \n1-Importar listas\n2-Listar los datos de los usuarios de México\n3-Listar los nombre, mail y teléfono de los usuarios de Brasil\n4-Listar los datos del/los usuario/s más joven/es\n5-Obtener un promedio de edad de los usuarios\n6-De los usuarios de Brasil, listar los datos del usuario de mayor edad\n7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\n8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.\n9-Listar los datos de los usuarios de México ordenados por nombre.\n10-Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente.\n11-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente\n0-Finalizar programa.\n" + "-" * 100)
    opcion = input(" \nElija una opción: ")
    if opcion == "0":
        opcion = cerrar_menu()
    elif opcion == "1":
        print('\n"Listas_personas.py" importado con éxito. \n' + '.' * 100)
        importado = True
        opcion = None
    elif importado == False:
        print("\nDebe importar la lista primero.\n" + "-" * 100)
    else:
        match opcion:
            case "1":
                print('\n"Listas_personas.py" ya ha sido importado \n' + '.' * 100)
                opcion = None
            case "2":
                for usuario in listar_datos_de_mexico():
                    print(f"\n {usuario}\n" + "." * 100)
                print("-" * 100)
                opcion = None
            case "3":
                for usuario in listar_datos_de_brasil():
                    print(f"\n {usuario}\n" + "." * 100)
                print("-" * 100)
                opcion = None
            case "4":
                for usuario in listar_datos_joven():
                    print(f"\n {usuario}\n" + "." * 100)
                print("-" * 100)
                opcion = None
            case "5":
                print(f"\nEl promedio de edad es de {determinar_premedio_de_edad()} años.\n" + "-" * 100)
                opcion = None
            case "6":
                for usuario in listar_mayor_de_brasil():
                    print(f"\n {usuario}")
                print("-" * 100)
                opcion = None
            case "7":
                for usuario in listar_mexico_brasil_zip8000():
                    print(f"\n {usuario}\n" + "." * 100)
                print("-" * 100)
                opcion = None
            case "8":
                for usuario in listar_datos_italianos40():
                    print(f"\n {usuario}\n" + "." * 100)
                print("-" * 100)
                opcion = None
            case "9":
                for usuario in listar_mexicanos_ascendente():
                    print(f"\n {usuario}\n" + "." * 100)
                print("-" * 100)
                opcion = None
            case "10":
                for usuario in listar_jovenes_ascendente():
                    print(f"\n {usuario}\n" + "." * 100)
                print("-" * 100)
                opcion = None
            case "11":
                for usuario in listar_ascendente_mexico_brasil_zip8000():
                    print(f"\n {usuario}\n" + "." * 100)
                print("-" * 100)
                opcion = None
            case "0":
                opcion = cerrar_menu()
            case _:
                print("Opción inválida, intente denuevo.")
                print("-" * 100)