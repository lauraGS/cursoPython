import unittest

class TestListas(unittest.TestCase):
    def test_method1(self):
        lista = ["apple", "banana", "cherry", "orange", "kiwi"]
        milista2 = sorted(lista, key=str.lower)
        self.assertEqual((milista2), ['apple', 'banana', 'cherry', 'kiwi', 'orange'])
        lista.insert(2, "mango")
        self.assertEqual(lista, ['apple', 'banana', 'mango', 'cherry', 'orange', 'kiwi'])
        lista.remove("banana")
        lista.remove("cherry")
        self.assertEqual(lista,['apple', 'mango', 'orange', 'kiwi'])
        lista.extend(["banana", "cherry"])
        self.assertEqual(lista,['apple', 'mango', 'orange', 'kiwi', 'banana', 'cherry'])
        del lista[0]
        lista.pop(0)
        self.assertEqual(lista, ['orange', 'kiwi', 'banana', 'cherry'])
        self.assertEqual(lista[-1], 'cherry')
