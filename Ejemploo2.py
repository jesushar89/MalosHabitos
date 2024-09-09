def calcular(factor1, factor2, factor3):
    opercion = factor1 * factor2 + factor3
    return opercion

if __name__ == "__main__":
    digito1 = float(input("Ingrese el primer numero: "))
    digito2 = float(input("Ingrese el segundo numero: "))
    digito3 = float(input("Ingrese el tercer numero: "))
    resultado = calcular(digito1, digito2, digito3)
    print(f"El resultado de la operacion {digito1} * {digito2} + {digito3} es: {resultado}")



