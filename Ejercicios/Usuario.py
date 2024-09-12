import re
import hashlib
class Usuario:
    nombre = ''
    email = ''
    password = ''
    archivo= "arch.txt"

    def __init__(self, nombre, email, password):
        # Atributos de instancia
        self.nombre = nombre
        self.email = email
        self.password = password

    def cambiaPass(self, intento):
        patronPass = r'.*(\d.*[A-Za-z]|[A-Za-z].*\d).*'
        if self.contraseñasIguales(intento) == True:
            print("Ingresa nueva contraseña:")
            new= input()
            try:
                contraseña = re.search(patronPass,new)
                len(intento)>=5 
            except PasswordInvalido:
                print("Contraseña invalida")
            else: 
                self.password= new
    def hashea(self):
        hasheado= hashlib.sha256(self.password.encode())
        return hasheado.hexdigest()

    def guardaUser(self):
        newArch= open(self.archivo, ("w"))
        newArch.write("Usuario: " + self.nombre + "\n" + "Contraseña: " + self.hashea())
        newArch.close()

    def contraseñasIguales(self, intento):
        if intento == self.password:
            return True
        else:
            return False
    
if __name__ == "__main__":

    user = Usuario("Hola", "blabla","abc12")

    """

    No me jaloooo es que no sé como abstraer las contraseñas de el usuario que me dan como input. Pensé en usar diccionarios
    pero el tiempo me mató unu.
    
    print("Bienvenido!!" + "\n" + "a) iniciar sesión : " + "b) salir")
    iniciar = input()
    while True:
        if iniciar == "a":
            print("Ingresa tu usuario: ")
            user = input()
            print("Ingresa tu contraseña: ")
            contraseña = input()
            try:
                user.contraseñasIguales(contraseña) == True
            except WrongPassword:
                print("Contraseña incorrecta")
            else: 
                print("Bienvenido =)")
                break
        else:
            print("Adios =)")
            break
    """
    user = Usuario("Hola", "blabla","abc12")
    print(user.nombre + "\n" + user.email + "\n" + user.password)
    print(user.contraseñasIguales("abc12"))
    user.guardaUser()
    user.cambiaPass("abc12")
    print(user.password)
    