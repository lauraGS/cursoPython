import requests
from lxml import html

print("Da un nombre")
nombre = input()


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