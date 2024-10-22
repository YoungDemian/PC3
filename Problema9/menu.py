from figuras import Circulo, Rectangulo, Cuadrado

def validar_numero(numero):
    try:
        valor = float(numero)
        if valor <= 0:
            raise ValueError("El número debe ser positivo.")
        return valor
    except ValueError:
        print("Error: Ingrese un número válido y positivo.")
        return None

def menu():
    while True:
        print("\nMenu:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            radio = validar_numero(input("Ingrese el radio del círculo: "))
            if radio is not None:
                circulo = Circulo(radio)
                print(f"El área del círculo es: {circulo.area():.2f}")

        elif opcion == '2':
            base = validar_numero(input("Ingrese la base del rectángulo: "))
            altura = validar_numero(input("Ingrese la altura del rectángulo: "))
            if base is not None and altura is not None:
                rectangulo = Rectangulo(base, altura)
                print(f"El área del rectángulo es: {rectangulo.area():.2f}")

        elif opcion == '3':
            lado = validar_numero(input("Ingrese el lado del cuadrado: "))
            if lado is not None:
                cuadrado = Cuadrado(lado)
                print(f"El área del cuadrado es: {cuadrado.area():.2f}")

        elif opcion == '4':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
