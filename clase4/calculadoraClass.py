class Calculadora:
    def __init__(self):
        pass

    def suma(self, n1:float, n2:float) -> float:
        return (n1+n2)

    def resta(self, n1:float, n2:float) -> float:
        return (n1-n2)

    def multiplicacion(self, n1:float, n2:float) -> float:
        return (n1 * n2)

    def dividir(self, n1: float, n2: float) -> float:
        try:
            return (n1 / n2)
        except ZeroDivisionError:
            print("Nuestro calculador no permite dividir por cero, intenta otro calculo!")
            return 0
