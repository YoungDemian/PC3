class Producto:
    def __init__(self, nombre, año, precio, categoria, marca):
        self.nombre = nombre
        self.año = año
        self.precio = precio
        self.categoria = categoria
        self.marca = marca

    def __str__(self):
        return (f"Nombre: {self.nombre}, Año: {self.año}, Precio: ${self.precio:.2f}, "
                f"Categoría: {self.categoria}, Marca: {self.marca}")

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el catálogo.")
            return
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        filtrados = [producto for producto in self.productos if producto.año == año]
        return filtrados

    def filtrar_por_categoria(self, categoria):
        filtrados = [producto for producto in self.productos if producto.categoria.lower() == categoria.lower()]
        return filtrados
if __name__ == "__main__":
    catalogo = Catalogo()
    producto1 = Producto("Frenos", 2022, 150.00, "Seguridad", "Toyota")
    producto2 = Producto("Aceite de motor", 2023, 30.00, "Mantenimiento", "Nissan")
    producto3 = Producto("Batería", 2021, 200.00, "Electricidad", "Subaru")
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    print("Lista de productos en el catálogo:")
    catalogo.mostrar_productos()

    print("\nProductos del año 2023:")
    productos_2023 = catalogo.filtrar_por_año(2023)
    for producto in productos_2023:
        print(producto)

    print("\nProductos de categoría 'Mantenimiento':")
    productos_mantenimiento = catalogo.filtrar_por_categoria("Mantenimiento")
    for producto in productos_mantenimiento:
        print(producto)

