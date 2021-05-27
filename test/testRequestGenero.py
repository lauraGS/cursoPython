import requests
from lxml import html
import unittest



class TestPrueba(unittest.TestCase):
      def test_method1(self):

            #print("Da un nombre")
            #nombre = input()
            nombre = "Pedro"

            ruta = requests.get('https://es.wikipedia.org/wiki/'+nombre+'_(nombre)')

            print(ruta.url)


            tree = html.fromstring(ruta.content)

            gender = tree.xpath('//a[@title="Identidad sexual"]/text()')
            listGender = tree.xpath('//div[@class="mw-parser-output"]//table//tbody//td//text()')
            footer = tree.xpath('//div[@class="action-list"]//p/text()')

            nameGender = ""
            for item in listGender:
                if item in ["\nMasculino", "\nFemenino"]:
                    nameGender = item
                    break
            
            print("Género: " + nameGender)
            self.assertTrue(not nameGender)