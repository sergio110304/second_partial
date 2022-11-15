from comprar import Comprar

class Usuario:
    def __init__(self):
        pass

    def Registro(self):
        print("Nuevo registro. Introduza sus datos ")
        self.nomusuario = input("Nombre de usuario:")
        self.asiento = input("Asiento preferido: ")
        self.Registro_usuario()

    def Registro_usuario(self):
        
        file = open("usuarios.txt", "r")
        info = file.read()
        if self.nomusuario in info:
            return "Usuario ya existe. Por favor intente nuevamente"
        file.close()

        
        file = open("usuarios.txt", "w")
        info = (info + " " + self.nomusuario + " " + self.asiento)
        file.write(info)
        file.close()
        self.exito_registro()

    def Verifica_login(self):
        print("Acceso a la cuenta. Introduza sus datos ")
        self.nomusuario = (input("Nombre de usuario:"))
        self.asiento = (input("Asiento preferido: "))


        file = open("usuarios.txt", "r")
        leer = file.read()
        leer = leer.split()

        if self.nomusuario in leer:
            index = leer.index(self.nomusuario) + 1
            contraseña_usuario = leer[index]
            if contraseña_usuario == self.asiento:
                return self.exito_login()
            else:
                return self.no_cont()
        else:
            return self.no_usuario()

    
    def exito_login(self):
        print("Ha ingresado con éxito")
        e = Comprar()
        e.seleccionar()

    
    def exito_registro(self):
        print("Registro completado con éxito")


    def no_cont(self):
        print("Error")

    
    def no_usuario(self):
        print("Usuario no encontrado")


### Tomado de: https://github.com/MarianaGb12/FinalProject_oop
