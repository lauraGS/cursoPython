import unittest
import yaml


class TestYaml(unittest.TestCase):
    def test_read(self):
        fichero = open("../files/fruits.yaml", 'r')
        listFruits = yaml.load(fichero, Loader=yaml.FullLoader)
        self.assertEqual(len(listFruits.items()), 5)



if __name__ == '__main__':
    unittest.main()
