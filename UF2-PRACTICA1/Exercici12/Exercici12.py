
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:

    num_mes = int(input("pon un número entre 0 y 12 (0 para salir): "))


    if num_mes == 0:
        print("FUEERITA NOMAS!.")
        break

    elif 1 <= num_mes <= 12:

        print("El mes es:", meses[num_mes - 1])
    else:
        print(" un número entre 0 y 12.")
