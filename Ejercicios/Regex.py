import re
Nombre = r'[A-Z][a-z]+ [A-Z][a-z]+'
Correo = r'@[\w]+'
Cadena = r'.*([A-Za-z]+.*\d+|\d+.*[A-Za-z]+).*'

nombre = "mi nombre es Danna Marquez"
x = re.search(Nombre , nombre)
print(x.group())

correo = "@usuario123"
y = re.search(Correo, correo)
print(y.group())

cadena = "hola123ab"
z = re.search(Cadena, cadena)
if cadena != None:
    print(z.group())