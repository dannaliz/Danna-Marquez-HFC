cadena = input()
a = "false"

es_palindromo = True
 
for i in range(len(cadena) // 2):
    if cadena[i] != cadena[len(cadena) - i - 1]:
        print(a)  # Si encontramos una diferencia, no es palíndromo
        es_palindromo = False
        break

# Si no se rompió el bucle, es un palíndromo
if es_palindromo:
    print("true")
