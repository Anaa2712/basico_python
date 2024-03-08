#Ejercicio2
#Calculadora con 4 metodos y parametros con decimales
#Queremos usar type() para ver como Python decide los
#tipos en base a los valores de inicialización que le damos


class Calculadora:
    def suma(self, a, b):
        self._verificar_numeros(a, b)
        resultado = a + b
        return resultado

    def resta(self, a, b):
        self._verificar_numeros(a, b)
        resultado = a - b
        return resultado

    def multiplicacion(self, a, b):
        self._verificar_numeros(a, b)
        resultado = a * b
        return resultado

    def division(self, a, b):
        self._verificar_numeros(a, b)
        if b != 0:
            resultado = a / b
            return resultado
        else:
            print("Error: No se puede dividir entre cero.")

    def _verificar_numeros(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Los parámetros deben ser números (enteros o decimales).")

calculadora = Calculadora()

resultado_suma = calculadora.suma(10.5, 5.2)
print("Suma:", resultado_suma)

resultado_resta = calculadora.resta(10.5, 5.2)
print("Resta:", resultado_resta)

resultado_multiplicacion = calculadora.multiplicacion(10.5, 5.2)
print("Multiplicación:", resultado_multiplicacion)

resultado_division = calculadora.division(10.5, 5.2)
print("División:", resultado_division)
