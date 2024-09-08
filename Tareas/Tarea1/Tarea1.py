import random
import string

def contraseña(minusculas, mayusculas, numeros):
    #Para sacar los caracteres en mayusculas, minusculas y números
    minusc = string.ascii_lowercase
    mayusc = string.ascii_uppercase
    nums = string.digits

    #Elegir n número random de caracteres y guardarlos
    parteMin= [random.choice(minusc) for _ in range (minusculas)]
    parteMay= [random.choice(mayusc) for _ in range (mayusculas)]
    parteNum= [random.choice(nums) for _ in range (numeros)]

    #Guardar los caracteres en la contraseña y luego shuffulearla 
    contraseña= parteMin + parteMay + parteNum 
    random.shuffle(contraseña)

    #Segun join es para pasar de lista a cadena pero no me jalaaaaaaa
    return ''.join(contraseña)


contraseñaPro = contraseña(4, 3, 2)
print("Contraseña generada:", contraseñaPro)
