def obtener_calificaciones():
    while True:
        try:
            entrada = input("Ingresa una lista de calificaciones separadas por comas: ")
            lista_calificaciones = entrada.split(',')
            calificaciones = [int(calificacion.strip()) for calificacion in lista_calificaciones]
            
            print("Calificaciones convertidas:", calificaciones)
            break 
        except ValueError:
            print("Error: Una o más calificaciones no son válidas. Asegúrate de ingresar solo números enteros.")
obtener_calificaciones()
