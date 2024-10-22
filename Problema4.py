class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
rectangulo1 = Rectangulo(5, 3)
print("El área del rectángulo es:", rectangulo1.calcular_area())
cuadrado1 = Cuadrado(4)
print("El área del cuadrado es:", cuadrado1.calcular_area())