Resoldre els següents exercicis:
Cada exercici és un arxiu diferent de nom exerciciX.py. (on la X correspon al número de l’exercici)

BÀSICS

Imprimir “Hola mundo” per pantalla.

Demanar a l’usuari que introdueixi un valor en €, seguidament demanar que introdueixi el IVA a aplicar-hi (4%, 10% o 21%) i finalment mostrar, per pantalla, el resultat del valor indicat per l’usuari, el % d’IVA demanat per l’usuari i el valor final amb l’IVA afegit.

Demanar a l’usuari que introdueixi 2 valors i mostrar, per pantalla, quin és el més gran.

Demanar a l’usuari dos valors. Una vegada s’executa el programa, aquest ha de mostrar el resultat per pantalla.

Demanar a l’usuari un número. Indicar si el número inserit per l’usuari és parell o senar.

LOOPS: Mostrar els números de l’1 al 100 amb un while.

LOOPS: Mostrar els números imparells de l’1 al 500.

Demanar a l’usuari que posi entre 1 i 3 paraules. Al executar el programa, mostrarà la/es paraula/es indicada/es per l’usuari, indicar quants caràcters té i indicar el primer, i l’últim caràcter.

Demanar a l’usuari que posi dues paraules. Al executar el programa, mostrarà per pantalla les dues paraules amb els dos primers caràcters de cada paraula intercanviats. Exemple: Quatre Camins passaria a Caatre Qumins.

Crear un arxiu on caldrà endevinar el número escollit pel programa entre 1 i 100. Cada vegada que l’usuari hi posi un número, caldrà indicar si és més petit o més gran fins que encerti i el missatge haurà d’indicar que ha encertat. Indicar també el número d’intents.

—--------------------------------------------------------------------------------------------------------------------------------


LLISTES, TUPLES I DICCIONARIS

Demanar a l’usuari un nùmero entre 10 i 100. Posar els números a una tupla desde 1 fins al número indicat per l’usuari. Exemple: usuari indica 34, es crea una tupla i es mostra per pantalla els números de l’1 al 34 (imprimint la tupla).

Crear una tupla amb els mesos de l’any. Demanar a l’usuari que posi un número entre 0 i 12 i mostrar per pantalla el mes corresponent al número indicat per l’usuari. El programa finalitza només quan l’usuari posa 0.

Demanar a l’usuari un número de l’1 al 10 i mostrar per pantalla la seva taula de multiplicar fins el 10. Exemple: l’usuari marca 3, es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30

Demanar a l’usuari que introdueixi 10 números separats per un espai. Al acabar, el programa els introduirà en una tupla i els ordenarà (major o menor, com volgueu), mostrant per pantalla el contingut de la tupla.

El mateix que l’anterior exercici, però sense demanar un màxim de números. L’usuari indicarà quan ha acabat posant un 0.

Demanar a l’usuari una frase. El programa eliminarà els espais i s'afegirà a una tupla. Mostrar per pantalla el contingut de la tupla.

Igual que l’anterior però a la tupla afegir la frase sense els caràcters repetits i mostrar el contingut de la tupla. Exemple: Usuari indica la paula caracteristica. Es mostra per pantalla carteis.

Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla i mostrar per pantalla quantes vegades apareix cada lletra.

Cal buscar la informació que es demana de la següent list:
areas_pis = [“Menjador”, 10.15, “Rebedor”, 9.56, “Habitació1”, 12.34, “Terrassa”, 15.55, “Lavabo”, 7.98, “Cuina”, 12, “Habitació2”, 12.23]
(Cal utilitzar els “:” per a que siguin vàlids els prints següents)
Imprimir el segon element
Imprimir l’últim element
Imprimir l’àrea de la terrassa
Imprimir del primer element al tercer element
Imprimir del tercer element a l’últim
Imprimir el total de l'àrea de les dues habitacions
Modificar l’àrea del lavabo i imprimir la nova list area
Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
Imprimir el total de l’àrea del pis.

Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat. S’haura de demanar a l’usuari que posi contactes (noms i edats). Si algun nom es repeteix no s’fageirà al diccionari (indicant-ho a l’usuari). Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.

Demanar a l’usuari que posi 10 números separats per espais. Afegir aquests números a una llista. Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista. Mostrar per pantalla la llista.

Exemple mostra per pantalla.
Números de l’usuari:
suma total:
mitjana:

—--------------------------------------------------------------------------------------------------------------------------------

XML I JSON

Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). La funció ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:
Un root de nom students.
Cinc childs (del root) amb nom student.
Cada child student ha de tindre 4 subchilds:
 name
 surname
 email
 dni
Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
El text de cada etiqueta serà de la vostra elecció.





Crear una funció que mostri, per consola, i guardi en un arxiu extern, un JSON amb una key de nom book que contindrà titel, cover, year i pages. Dintre del JSON hi hauran 4 de cada book (s’ha d’omplir amb values). 

Crear una funció que llegeixi el JSON de l’exercici anterior  i surti el resultat (en format json) per consola.

—--------------------------------------------------------------------------------------------------------------------------------

FUNCIONS


Crear un arxiu de nom vehicle.py. En aquest arxiu s’ha de crear una class de nom vehicle. Aquesta class ha de tindre:
Constructor
Atributs (mínim 6)
Getters/Setters
Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

Crear un arxiu de nom user.py. En aquest arxiu s’ha de crear una class de nom user. Aquesta class ha de tindre:
Constructor
Atributs (mínim 6)
Getters/Setters
Mètode de nom salutacio on es mostren, per pantalla, totes les dades (atributs) del user.
Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

A partir d’aqui cada arxiu creat per a cada exercici ha de tindre un arxiu de nom main.py on cridarà cada arxiu per veure’n el resultat.

Crear una funció que sumi dos números passats per paràmetre. Aquests números seran demanats a l’usuari. 
(En aquest cas haurieu de tindre un arxiu on feu el càlcul de dos números passats per paràmetre i un arxiu main.py on trucarà aquesta funció i li passarà els números indicats per l’usuari.)

Crear una funció que passats dos números per paràmetre (demanats a l’usuari) ens mostri per pantalla un número aleatori entre aquests dos números.

Crear una funció que passats dos números per paràmetre (demanats a l’usuari) ens mostra per pantalla tots els números (enters) que hi ha entre ells. També mostrarà per pantalla la suma d’aquests números enters.

Crear una funció que passat un nom per l’usuari (nom). Mostri per pantalla “Hola nom”.

Crear una funció per calcular el total d’una factura amb l’IVA. La funció ha de rebre (per paràmetre) la quantitat sense IVA i l’IVA a aplicar (introduïts per l’usuari). En cas de no passar-li cap valor o un valor erroni (4%, 10% o 21%) s’aplicarà directament el 21%. Es mostra per pantalla el valor sense IVA, l’IVA i el total.

Crear una funció que agafi una llista amb 10 números, i retorni una altra llista amb els seus quadrats.

—--------------------------------------------------------------------------------------------------------------------------------

PROGRAMACIÓ FUNCIONAL

Crear una funció que rebi un diccionari amb una llista de la compra (amb preus i descomptes).
Exemple llista compra: {100:10, 250:5, 1500:30, …}
on 100 és el preu i 20 el descompte a aplicar a aquests 100.
Demanar a l’usuari l’IVA a aplicar al total de la llista de la compra.
Mostrar per pantalla els valors amb el descompte aplicat més l’IVA.
Exemple:
Producte 1: 
Producte 2: 
…

Crear una funció que rebi, per paràmetres, una funció i una llista. Ha de crear una llista nova amb el nou contingut i mostrar-la per pantalla.
Passes:
Crear una funció que calculi el quadrat d’un número passat per paràmetre.
Crear una segona funció que agafi cada número de la llista (passat per paràmetre) i truqui a la funció anterior i guardar el resultat a una llista.

Crear una funció que rebi una frase per paràmetre. Aquesta frase es demana a l’usuari. Ha de retornar un diccionari amb les paraules que conte i la longitud de cada paraula.

—--------------------------------------------------------------------------------------------------------------------------------

TROBAR ERRORS I MILLORAR PROGRAMES

 Buscar error/s en el següent programa:

passwd= input('Introdueix una contrasenya: ")
if contrasenya  in ['Peliñ4nd0#'):
  print('Correcte')
else
  print('Incorrecte')


Buscar error/s en el següent programa:


ftotal = input('Introdueix el preu de tot el carrito: ')

print(amb_iva(ftotal, iva))

def amb_iva(ftotal, iva = 21):
    ftotal = ftotal * iva   
    return ftotal 


Com a resultat ha de donar 121.0 en cas de que l’usuari posi 100










Buscar error/s en el següent programa. Aquest programa elimina el contacte (nom i telèfon) segons el nom passat per paràmetre.

contactes = {'Roger':678232311, 'Oriol':566879326}

def elimina(contactes, user):
    del contactes[user]
    return contactes[user]

print(elimina(contactes, 'Pablo'))



En el següent codi es vol demanar a l’usuari un número enter i mostri un triangle rectangle segons el número aportat per l’usuari.


n = int(input("Introdueix l’alçada del triangle (enter positiu): "))
for i in range(1, n+1, 2):
    for j in range(j, 1, -1):
        print(j, end=" ")
    print("")


Si l’usuari posa 9 o 10:

Resultat:
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1


