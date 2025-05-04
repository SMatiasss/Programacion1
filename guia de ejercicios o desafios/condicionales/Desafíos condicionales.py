cliente = input("Ingrese el tipo de cliente (residencial/comercial/industrial): ").lower()
metros = int(input("Ingrese la cantidad de metros cúbicos consumidos: "))
cargo_fijo = 7000
costo_consumo = 200
subtotal = cargo_fijo + costo_consumo * metros
print(f"\n Subtotal = {subtotal}\n")
if cliente == "residencial":
    match metros:
        case metros if metros < 30:
            subtotal = subtotal * 0.9
            print(f"Al subtotal se le aplica un descuento del 10%, con un nuevo subtotal de: ${subtotal}")
        case metros if metros > 80:
            subtotal = subtotal * 1.15
            print(f"Al subtotal se le aplica un recargo del 15%, con un nuevo subtotal de: ${subtotal}")
elif cliente == "comercial":
    match metros:
        case metros if metros > 150:
            subtotal = subtotal * 0.92
            print(f"Al subtotal se le aplica un descuento del 8%, con un nuevo subtotal de: ${subtotal}")
        case metros if metros > 300:
            subtotal = subtotal * 0.88
            print(f"Al subtotal se le aplica un descuento del 12%, con un nuevo subtotal de: ${subtotal}")
        case metros if metros < 50:
            subtotal = subtotal * 1.05
            print(f"Al subtotal se le aplica un recargo del 5%, con un nuevo subtotal de: ${subtotal}")
elif cliente == "industrial":
    match metros:
        case metros if metros > 500:
            subtotal = subtotal * 0.8
            print(f"Al subtotal se le aplica un descuento del 20%, con un nuevo subtotal de: ${subtotal}")
        case metros if metros > 1000:
            subtotal = subtotal * 0.7
            print(f"Al subtotal se le aplica un descuento del 30%, con un nuevo subtotal de: ${subtotal}")
        case metros if metros < 200:
            subtotal = subtotal * 1.10
            print(f"Al subtotal se le aplica un recargo del 10%, con un nuevo subtotal de: ${subtotal}")
else:
    print("Tipo de cliente inválido")
if cliente == "residencial" and subtotal < 35000:
    subtotal = subtotal * 0.95
total = subtotal * 1.21
print(f"\nSe aplica un recargo del {subtotal * 0.21} por el impuesto IVA")
print(f"El total a pagar es de ${total}.")