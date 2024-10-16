#Formula de Bhaskara
import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Não há raízes reais.")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print("A raiz real é:", x1)
    else:
        print("As raízes reais são:", x1, "e", x2)
