# Creare un'istanza stringa, printare (print() ) l'ultima lettera in uppercase
my_string = "esercizio"

print("esercizio 1", (my_string[0: len(my_string)-1] + my_string[len(my_string) - 1].upper()))

# Creare due istanze stringa, convertirle in numeri e effettuare la somma (+)
stringa_numerica1 = '44'
stringa_numerica2 = '44'
somma_stringhe = int(stringa_numerica1) + int(stringa_numerica2)

print("esercizio 2", somma_stringhe)

# Printare la parola "ESERCIZIO" senza la prima e l'ultima lettera
print("esercizio 3", my_string[1:-1])

# Della parola "ESERCIZIO" che indica ha la "R"
print("esercizio 4", my_string.index('r'))
