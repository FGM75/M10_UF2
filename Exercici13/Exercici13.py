
numero = int(input("un número del 1 al 10: "))

if 1 <= numero <= 10:

    print(f"Tabla de multiplicar de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("ERRROR pon un número del 1 al 10.")
