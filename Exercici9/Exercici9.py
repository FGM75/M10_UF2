
palabra1 = input("primera palabra: ")
palabra2 = input("segunda parabra: ")

nueva_palabra1 = palabra2[:2] + palabra1[2:]
nueva_palabra2 = palabra1[:2] + palabra2[2:]


print("Resultado: {} {}".format(nueva_palabra1, nueva_palabra2))
