import yaml

class FormasYaml:
    def __init__(self):
        pass

    def methodRead1(self, nombreFich):
        fichero = open(nombreFich, 'r')
        listFruits = yaml.load(fichero, Loader=yaml.FullLoader)
        print(listFruits)
        sort_file = yaml.dump(listFruits, sort_keys=True)
        print(sort_file)

    def methodRead2(self, nombreFich):
        with open(nombreFich, 'r') as file:
            documents = yaml.full_load(file)
            for item, doc in documents.items():
                print(item, ":", doc)

    def methodWrite(self, nombreFich, datos):
        with open(nombreFich, 'w') as file:
            documents = yaml.dump(datos, file)


claseYaml = FormasYaml()
claseYaml.methodRead1("../files/fruits.yaml")
claseYaml.methodRead2("../files/categories.yaml")

datosFile = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]
claseYaml.methodWrite("../files/respuestaYaml.yaml", datosFile)