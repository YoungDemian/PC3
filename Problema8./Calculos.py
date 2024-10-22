from operaciones import suma, resta, producto, division

def main():
    # Ejemplos de uso
    print("Suma:", suma(5, 3))
    print("Resta:", resta(10, 4))
    print("Producto:", producto(6, 7))
    
    # División normal
    print("División:", division(10, 2))
    
    # Intento de división por cero
    print("División por cero:", division(10, 0))

if __name__ == "__main__":
    main()
