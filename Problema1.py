def obtener_porcentaje_combustible():
    while True:
        try:
            fraccion = input("Ingresa la fracción de combustible (X/Y): ")
            X, Y = map(int, fraccion.split('/'))
            
            if Y == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            if X > Y:
                raise ValueError("X debe ser menor o igual a Y.")
            porcentaje = round((X / Y) * 100)
            if porcentaje <= 1:
                print("E")
            elif porcentaje >= 99:
                print("F")
            else:
                print(f"{porcentaje}%")
            
            break 
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar números enteros en el formato X/Y donde X <= Y.")
        except ZeroDivisionError:
            print("Error: División por cero. Inténtalo de nuevo.")
obtener_porcentaje_combustible()
