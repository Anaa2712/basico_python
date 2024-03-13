#Crear un array con números y sumar sus valores

#Caso 1
'''def suma_array(bb):
    resu=0
    for elemento in bb:
        resu += elemento
    return resu
a = [1,2,3,4]
#print(suma_array(a))'''

#Caso 2
'''a = [1,2,3,4]
suma = sum(a)
print("Array:", a)
print("Suma de los valores del array:", suma)'''

#Caso3
a = [12, 2.66666, 67, 4, ]
suma = sum(a)
for dato in a:
    if type(dato == int or dato == float):
        suma += dato

print("Array:", a)
print("Suma de los valores de tipo entero:", suma)







