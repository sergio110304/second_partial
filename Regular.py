from abstract import Entrada_peli

class Regular(Entrada_peli):

    def selec_hora(self):
        print('1- 1:00 pm')
        print('2- 3:00 pm')
        print('3- 4:00 pm')
        print('4- 5:00 pm')
        print('5- 7:00 pm')
        self.hora = int(input(print('Elija entre unas de las horas: ')))
        if self.hora == 1:
            self.hora = str('1:00 pm')
        elif self.hora == 2:
            self.hora = str('3:00 pm')
        elif self.hora == 3:
            self.hora = str('4:00 pm')
        elif self.hora == 4:
            self.hora = str('5:00 pm')
        elif self.hora == 5:
            self.hora = str('7:00 pm')
        return self.hora

    def selec_cantidad(self):
        self.cant = int(input(print('Ingrese la cantidad de entradas que desea: ')))
        # El precio por entrar es de 5 pesos
        self.total = 5 * self.cant
        return self.total
        
    def selec_asiento(self):
        print('A1 | A2 | A3 | A4 | A5')
        print('B1 | B2 | B3 | B4 | B5')
        print('C1 | C2 | C3 | C4 | C5')
        print('D1 | D2 | D3 | D4 | D5')
        print('E1 | E2 | E3 | E4 | E5')
        self.asiento = str(input(print('Escriba el asiento seleccionado: ')))
        return self.asiento

    def comprar(self):
        self.p = self.selec_pelicula()
        self.h = self.selec_hora()
        self.c = self.selec_cantidad()
        self.a = self.selec_asiento()
        print('---FACTURA---')
        print('Pelicula: ',self.p)
        print('Hora de función: ',self.h)
        print('Asiento escogido: ',self.a)
        print('Total a pagar: ',self.c, ' pesos')
        nose = int(input(print('Realizar compra: 1.Si 2.No')))
        if nose == 1:
            print('Compra realizada')
        else:
            print('Vuelva pronto.')
