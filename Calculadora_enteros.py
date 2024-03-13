#Ejercicio 1:

#Calculadora con 4 metodos y parametros con enteros.

#Queremos usar type() para ver como Python decide los tipos en
#base a los valores de iniciacion que le damos


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
    if b!= 0:
        resultado = a /b
        return resultado
    else:
        print("Error")

def _verificar_enteros(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Los parametros deben ser números enteros.")



resultado_suma = suma(10, 5)
print("Suma:", resultado_suma)

resultado_resta = resta(10, 5)
print("Resta:", resultado_resta)

resultado_multiplicacion = multiplicacion(10, 5)
print("Multiplicación:", resultado_multiplicacion)

resultado_division = division(10, 5)
print("División:", resultado_division)