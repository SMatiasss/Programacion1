from datos_y_estructura import menu,estudiantes
from opciones import *

opcion = None
while opcion != "s":
    print(menu)
    opcion = input("Ingrese una opción: ")
    opcion = obligar_opcion(opcion)
    match opcion:
        case "1":
            ejecutar_opcion_1(estudiantes)
        case "2":
            ejecutar_opcion_2(estudiantes)
        case "3":
            ejecutar_opcion_3(estudiantes)
        case "4":
            ejecutar_opcion_4(estudiantes)
        case "5":
            ejecutar_opcion_5(estudiantes)
        case "6":
            ejecutar_opcion_6(estudiantes)
        case "7":
            ejecutar_opcion_7(estudiantes)
        case "8":
            opcion = finalizar_programa()