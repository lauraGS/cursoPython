
import unittest
from ejercicios.clase2.ejerClases import Gato
from ejercicios.clase2.ejerClases import Animal


class TestMetodo(unittest.TestCase):
    def test_method1(self):
        mi_gato = Gato()
        self.assertTrue((mi_gato.vivo()))
        