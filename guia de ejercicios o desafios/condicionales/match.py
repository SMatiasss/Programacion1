# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# a-Si es invierno: solo se viaja a Bariloche.
# b-Si es verano: se viaja a Mar del plata y Cataratas.
# c-Si es otoño: se viaja a todos los lugares.
# d-Si es primavera: se viaja a todos los lugares menos Bariloche.
lugar = input("Ingrese su destino de viaje: ").lower()
estacion = input("Ingrese la estación en la que desea viajar: ").lower()
match estacion:
    case "invierno":
        match lugar:
            case "bariloche":
                print("Se viaja.")
            case "mar del plata" | "cataratas":
                print("No se viaja.")
            case _:
                print("Lugar inválido")
    case "verano":
        match lugar:
            case "mar del plata" | "cataratas":
                print("Se viaja.")
            case "bariloche":
                print("No se viaja.")
            case _:
                print("Lugar inválido")
    case "otoño":
        match lugar:
            case "bariloche" | "mar del plata" | "cataratas":
                print("Se viaja.")
            case _:
                print("Lugar inválido.")
    case "primavera":
        match lugar:
            case "bariloche":
                print("No se viaja.")
            case "mar del plata" | "cataratas":
                print("Se viaja.")
            case _:
                print("Lugar inválido.")
    case _:
        print("Estación inválida.")