#Ejercicio2
#Calculadora con 4 metodos y parametros con decimales
#Queremos usar type() para ver como Python decide los
#tipos en base a los valores de inicialización que le damos



def suma(a, b):
    resultado = a + b
    return resultado

def resta(a, b):
    resultado = a - b
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    return resultado

def division(a, b):
    if b != 0:
        resultado = a / b
        return resultado
    else:
        print("Error: No se puede dividir entre cero.")

def _verificar_numeros(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Los parámetros deben ser números (enteros o decimales).")


resultado_suma = suma(10.5, 5.2)
print("Suma:", resultado_suma)

resultado_resta = resta(10.5, 5.2)
print("Resta:", resultado_resta)

resultado_multiplicacion = multiplicacion(10.5, 5.2)
print("Multiplicación:", resultado_multiplicacion)

resultado_division = division(10.5, 5.2)
print("División:", resultado_division)
