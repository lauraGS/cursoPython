
from calculadoraClass import Calculadora

miCalc = Calculadora()

n1 = float(input("Introduce tu primer número: "))
n2 = float(input("Introduce tu segundo número: "))

opcion = 0

while True:
    print("""
    Opciones:
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Seguir con la calculadora
    5) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print(" ")
        resultado = miCalc.suma(n1, n2)
        print("RESULTADO: La suma de", n1, "+", n2, "es igual a", resultado)
    elif opcion == 2:
        print(" ")
        resultado = miCalc.resta(n1, n2)
        print("RESULTADO: La resta de", n1, "-", n2, "es igual a", resultado)
    elif opcion == 3:
        print(" ")
        resultado = miCalc.multiplicacion(n1, n2)
        print("RESULTADO: El producto de", n1, "*", n2, "es igual a", resultado)
    elif opcion == 4:
        n1 = float(input("Introduce tu primer número: "))
        n2 = float(input("Introduce tu segundo número: "))
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")

    print(" ")
    print(" ")
