
class Animal():
    def __init__(self):
        self.isVivo = True

    def vivo(self):
       print("Está vivo")
       return self.isVivo


class Gato(Animal):
          
    def correr(self):
        print("Está corriendo!")

    def dormir(self):
        print("Está durmiendo!")

    def ronrronear(self):
       print("rrrrrrr!")

    def maullar(self):
        print("Miau")
    

mi_gato = Gato()
print(mi_gato.vivo())
mi_gato.correr()
mi_gato.dormir()
mi_gato.ronrronear()
mi_gato.maullar()
