#Calculadora en una clase

class Calculadora:
    def sumar(a,b):
        return a + b
    def restar(a,b):
        return a + b
    def multiplicar(a, b):
        return a * b
    def dividir (a, b):
        return a / b
print("La suma de 5 más 8 es:" , Calculadora.sumar(5,8))
print("La resta de 10 menos 4 es:", Calculadora.restar(10,4))
print("La multiplicación de 2 por 8 es:" , Calculadora.multiplicar(2,8))
print("La división de 225 entre 5 es:" , Calculadora.dividir(225, 5))

