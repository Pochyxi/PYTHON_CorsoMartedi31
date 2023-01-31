# Creare un'istanza stringa, printare (print() ) l'ultima lettera in uppercase
my_string = "esercizio"

print("esercizio 1", (my_string[0: len(my_string) - 1] + my_string[len(my_string) - 1].upper()))

# Creare due istanze stringa, convertirle in numeri e effettuare la somma (+)
stringa_numerica1 = '44'
stringa_numerica2 = '44'
somma_stringhe = int(stringa_numerica1) + int(stringa_numerica2)

print("esercizio 2", somma_stringhe)

# Printare la parola "ESERCIZIO" senza la prima e l'ultima lettera
print("esercizio 3", my_string[1:-1])

# Della parola "ESERCIZIO" che indica ha la "R"
print("esercizio 4", my_string.index('r'))

print()
print("COLLEZIONI")

# Creare un'istanza lista che dati 5 numeri a caso, restituisca una lista ordinata

lista_disordinata = [4, 7, 9, 2, 11]
lista_disordinata.sort()
print("Esercizio 1", lista_disordinata)

# cambiare il valore di una tupla
mia_tupla = ("prova", "ciao")
mia_lista_tupla = list(mia_tupla)
mia_lista_tupla[1] = "ciaone"
mia_tupla = tuple(mia_lista_tupla)

print("Esercizio 2", mia_tupla)

# Cambiare il primo valore di una lista
mia_lista = [1, 2, 3, 4, 5]
mia_lista[0] = 5

print("Esercizio 3", mia_lista)

# Creare una tupla che contiene al proprio interno una lista e sun set e cambiare il valore contenuto nella lista

mia_tupla_con_dict = ([6, 7, 11, 34], {"ciao", "prova", "uno"})
mia_lista_con_dict = list(mia_tupla_con_dict)
mia_lista_con_dict[0][0] = 1994
mia_tupla_con_dict = tuple(mia_lista_con_dict)

print("Esercizio 4", mia_tupla_con_dict)

# Creare un dizionario cognome:nome, e ricavare la lista di tutte le chiavi con i metodi keys e values

mio_dict = {"saluto": "ciao", "prova": "provino"}
mia_lista_keys = list(mio_dict.keys())
mia_lista_value = list(mio_dict.values())
print("Esercizio 5", mia_lista_keys)
print("Esercizio 5", mia_lista_value)

# Creare un ciclo for con valore da iterare range (20) e fare il print dei soli numeri pari

for i in range(20):
    print(i) if i % 2 == 0 else None


def cifrario(stringa, dichiarazione_di_intenti="crypt"):
    lista_alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "u", "v", "w", "x", "y", "z"]
    if dichiarazione_di_intenti == "crypt":
        stringa_cifrata = ""

        for carattere in stringa:
            indice_carattere = lista_alfabeto.index(carattere.lower())

            if indice_carattere == len(lista_alfabeto) - 1:
                indice_carattere = 0
                stringa_cifrata = stringa_cifrata + lista_alfabeto[indice_carattere]
            else:
                stringa_cifrata = stringa_cifrata + lista_alfabeto[indice_carattere + 1]

        return stringa_cifrata.upper()
    elif dichiarazione_di_intenti == "decrypt":
        stringa_decifrata = ""

        for carattere in stringa:
            indice_carattere = lista_alfabeto.index(carattere.lower())

            if indice_carattere == len(lista_alfabeto) - 1:
                indice_carattere = len(lista_alfabeto) - 1
                stringa_decifrata = stringa_decifrata + lista_alfabeto[indice_carattere]
            else:
                stringa_decifrata = stringa_decifrata + lista_alfabeto[indice_carattere - 1]

        return stringa_decifrata.upper()


print(cifrario("CIAOZ", "crypt"))
print(cifrario("DJBPZ", "decrypt"))
