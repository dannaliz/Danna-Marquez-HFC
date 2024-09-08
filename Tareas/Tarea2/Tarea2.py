# Lo admito, me robe el codigo, no tengo ni idea de como se hace una función aleatoria sin modulos
# Generar un número pseudoaleatorio (usando una fórmula simple)
def generar_numero_aleatorio():
    seed = 42  # Puedes cambiar esta semilla para obtener diferentes números
    return (seed * 12345 + 67890) % 100 + 1  # El resultado siempre será entre 1 y 100

def adivinaNumero():
    numSecreto = generar_numero_aleatorio()   
    print("Adivina el número entre el rango 1 y 100")
    
    while True:
        # Pedir a usuario intento
        respuesta = input("Introduce tu intento o escribe 'salir' para salir: ") 

        # Salir del juego 
        if respuesta == 'salir':
            print("buuuh")
            break

        num = int(respuesta) #pasar de string a num

        if num < numSecreto:
            print("El número secreto es mayor.")
        elif num > numSecreto:
            print("El número secreto es menor.")
        else:
            print("kul, adivinaste el número uwu.")
            break

# Ejecutar el juego
adivinaNumero()
