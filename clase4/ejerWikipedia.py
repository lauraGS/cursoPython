import requests
from lxml import html

print("Da un nombre")
nombre = input()


ruta = requests.get('https://es.wikipedia.org/wiki/'+nombre+'_(nombre)')

print(ruta.url)


tree = html.fromstring(ruta.content)

gender = tree.xpath('//a[@title="Identidad sexual"]/text()')
path_list = '//div[@class="mw-parser-output"]//table//tbody//td//text()'
listGender = tree.xpath(path_list)
footer = tree.xpath('//div[@class="action-list"]//p/text()')

nameGender = ""
for item in listGender:
    if item.strip() in ["Masculino", "Femenino"]:
        nameGender = item
        break

print("Género: " + nameGender)
