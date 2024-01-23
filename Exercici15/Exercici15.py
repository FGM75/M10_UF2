
numeros = []
while True:

    numero = int(input("pon un numero, si quieres terminar pon un 0: "))

    if numero == 0:
        break

    numeros.append(numero)

if len(numeros) > 0:

    tupla_numeros = tuple(sorted(numeros))

    print("Tupla ordenada:", tupla_numeros)
else:
    print("si no pones numeros, me voy, Programa finalizado.")
