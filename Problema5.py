class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print(f"Notas: {self.notas}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.notas.append(nota)
def crear_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    numero_registro = input("Ingrese el número de registro: ")
    alumno = Alumno(nombre, numero_registro)

    edad = input("Ingrese la edad del alumno: ")
    alumno.setAge(int(edad))

    while True:
        nota = input("Ingrese una nota (o 'fin' para terminar): ")
        if nota.lower() == 'fin':
            break
        alumno.setNota(float(nota))

    return alumno
alumno1 = crear_alumno()
alumno1.display()
