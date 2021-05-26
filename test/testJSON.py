import json
import unittest

class TestPrueba(unittest.TestCase):
    def test_method1(self):
        student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},
                    "102":{"class":'V', "Name":'David',  "Roll_no":8},
                    "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}
        self.assertEqual(student["101"], {"class":'V', "Name":'Rohit',  "Roll_no":7})
        self.assertEqual(list(student.keys()), ["101", "102", "103"])
        self.assertEqual(list(student["101"].keys()), ["class", "Name", "Roll_no"])



    def test_method2(self):
        colores = 'Red', 'Black', 'White'
        self.assertEqual(json.dumps(colores), '["Red", "Black", "White"]')