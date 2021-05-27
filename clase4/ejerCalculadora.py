n1 = float(input("Introduce tu primer número: "))
n2 = float(input("Introduce tu segundo número: "))

opcion = 0

print("""
Opciones:
1) Sumar los dos números
2) Restar los dos números
3) Multiplicar los dos números
""")
opcion = int(input("Elige una opción: "))

if opcion == 1:
    print(" ")
    print("RESULTADO: La suma de", n1, "+", n2, "es igual a", n1+n2)
elif opcion == 2:
    print(" ")
    print("RESULTADO: La resta de", n1, "-", n2, "es igual a", n1-n2)
elif opcion == 3:
    print(" ")
    print("RESULTADO: El producto de", n1, "*", n2, "es igual a", n1*n2)
else:
    print("Opción incorrecta")
