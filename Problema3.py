import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2
circulo1 = Circulo(5)
circulo2 = Circulo(3.14)
area1 = circulo1.calcular_area()
area2 = circulo2.calcular_area()

print("El área del círculo 1 es:", area1)
print("El área del círculo 2 es:", area2)