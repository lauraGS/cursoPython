
import unittest
from clase2.ejerClases import Gato
from clase2.ejerClases import Animal


class TestMetodo(unittest.TestCase):
    def test_method1(self):
        mi_gato = Gato()
        self.assertTrue((mi_gato.vivo()))
        
