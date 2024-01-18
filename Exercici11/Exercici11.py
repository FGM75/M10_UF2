
num_usuario = int(input("Introduce un número entre 10 y 100: "))

if 10 <= num_usuario <= 100:

    numeros = tuple(range(1, num_usuario + 1))

    print("números del 1 al {}: {}".format(num_usuario, numeros))
else:
    print("Error my friend")
