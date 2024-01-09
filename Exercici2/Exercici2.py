
valor = float(input("Introduce el valor en €: "))

iva = int(input("Introduce el % de IVA: "))

calculaIva = valor * (iva / 100)

totalConIva = valor + calculaIva

print("El valor es de:", valor ,"€")
print("El % de IVA es:", iva ,"€")
print("El valor total con iva es:", totalConIva ,"€")
