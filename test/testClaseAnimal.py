
import unittest


class Animal():
    def __init__(self):
        self.isVivo = True

    def vivo(self):
        return self.isVivo


class Gato(Animal):
          
    def correr(self):
        return("Está corriendo!")

    def dormir(self):
        return("Está durmiendo!")

    def ronrronear(self):
        return("rrrrrrr!")

    def maullar(self):
       return("Miau")



class TestMetodo(unittest.TestCase):
    def test_method1(self):
        mi_gato = Gato()
        self.assertTrue((mi_gato.vivo()))
        