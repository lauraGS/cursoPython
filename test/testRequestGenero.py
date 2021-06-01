import requests
from lxml import html
import unittest


class TestPrueba(unittest.TestCase):

    def test_method1(self):

        nombre = "Pablo"
        path_ruta = 'https://es.wikipedia.org/wiki/'+nombre+'_(nombre)'
        ruta = requests.get(path_ruta)
        tree = html.fromstring(ruta.content)
        gender = tree.xpath('//a[@title="Identidad sexual"]/text()')
        pathList = '//div[@class="mw-parser-output"]//table//tbody//td//text()'
        listGender = tree.xpath(pathList)
        footer = tree.xpath('//div[@class="action-list"]//p/text()')
        nameGender = ""
        for item in listGender:
            if item.strip() in ["Masculino", "Femenino"]:
                nameGender = item.strip()
                break
        print("Género: " + nameGender)
        self.assertFalse(not nameGender)
