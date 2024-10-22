import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

    def distancia(self, otro):
        """Calcula la distancia entre este punto y otro punto."""
        return math.sqrt((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2)

    def mover(self, dx, dy):
        """Mueve el punto por una distancia dx y dy."""
        self.x += dx
        self.y += dy

if __name__ == "__main__":
    p1 = Punto(2, 3)
    p2 = Punto(5, 7)

    print(f"Coordenadas del primer punto: {p1}")
    print(f"Coordenadas del segundo punto: {p2}")

    distancia = p1.distancia(p2)
    print(f"La distancia entre {p1} y {p2} es: {distancia:.2f}")

    p1.mover(1, -1)
    print(f"Nuevo valor de p1 tras moverlo: {p1}")
