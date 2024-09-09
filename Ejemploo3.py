# Función para calcular el área de un rectángulo
def AreaRec(variable1, variable2):
    result = variable1 * variable2
    return result

# Función para calcular el área de un triángulo
def AreaTri(factor1, factor2):
    r = 0.5 * factor1 * factor2
    return r

# Función principal
if __name__ == "__main__":

    print("Ejercicio del rectangulo")
    x = float(print("Ingresa base del rectangulo: "))
    y = float(print("Ingrese altura del rectangulo:"))
    rect_area = f(x, y)
    print(f"Área del rectángulo:", rect_area)

    print("Ejercicio del triangulo")
    base = float(print("Ingresa base del triangulo: "))
    altura = float(print("Ingresa altura del triangulo: "))
    tri_area = g(base, altura)
    print("Área del triángulo:", tri_area)