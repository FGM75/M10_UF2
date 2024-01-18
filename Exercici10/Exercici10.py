import random
numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    adivida_num = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1
    
    if adivida_num == numero_secreto:
        print("Has adivinado el número {} en {} intentos.".format(numero_secreto, intentos))
        break
    elif adivida_num < numero_secreto:
        print("El número es más grande.")
    else:
        print("El número es más pequeño.")
