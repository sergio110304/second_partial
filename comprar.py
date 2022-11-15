from VIP import VIP
from Regular import Regular

class Comprar():    

    def seleccionar(self):

        print('1- Entrada VIP')
        print('2- Entrada regular')
        self.peli = int(input(print('Escoja un tipo de entrada: ')))

        if self.peli == 1:
            self.x1 =   VIP()
            self.x1.comprar()

        elif self.peli == 2:
            self.x2 = Regular()
            self.x2.comprar()
