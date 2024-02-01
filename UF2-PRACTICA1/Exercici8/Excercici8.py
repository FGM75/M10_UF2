
paraules = input("pon de 1 a 3 palabras: ")

num_paraules = paraules.count(" ") + 1
if num_paraules < 1 or num_paraules > 3:
    print("Cantidad de palabras no validas")
    exit()

for paraula in paraules.split():
    print(paraula)

for paraula in paraules.split():
    print("'{}' tiene {} letras.".format(paraula, len(paraula)))


for paraula in paraules.split():
    print("Comienza por '{}'.".format(paraula[0]))
    print("Acaba en '{}'.".format(paraula[-1]))