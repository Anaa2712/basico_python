#Ejercicio 1:
    # Calculadora con 4 metodos y parametros con enteros.

    # Queremos usar type() para ver como Python decide los tipos en
    # base a los valores de iniciacion que le damos

class Calculadora:

    def suma(self, a, b):
        self.verificar_enteros(a,b)
        resultado = a + b
        return resultado

    def resta(self, a, b):
        self.verificar_enteros(a, b)
        resultado = a - b
        return resultado
    def multiplicacion(self, a, b):
        self.verificar_enteros(a, b)
        resultado = a * b
        return resultado
    def division(self, a, b):
        self.verificar_enteros(a, b)
        if b!= 0:
            resultado = a /b
            return resultado
        else:
            print("Error")

    def verificar_enteros(self, a, b):
        if not (type(a) == int and type(b) == int):
            raise TypeError("Los parámetros deben ser enteros")

calculadora = Calculadora()

resultado_suma = calculadora.suma(10, 5)
print("Suma:", resultado_suma)

resultado_resta = calculadora.resta(10, 5)
print("Resta:", resultado_resta)

resultado_multiplicacion = calculadora.multiplicacion(10, 5)
print("Multiplicación:", resultado_multiplicacion)

resultado_division = calculadora.division(10, 5)
print("División:", resultado_division)