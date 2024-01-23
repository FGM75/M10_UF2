
entrada_usuario = input("pon 10 números ")


numeros = [int(x) for x in entrada_usuario.split()]

if len(numeros) == 10:

    tupla_numeros = tuple(sorted(numeros))


    print("numeros ordenados:", tupla_numeros)
else:
    print("pon 10 numeros con espacio")
