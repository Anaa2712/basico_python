#Crear dos diccionarios y unirlos

'''diccionario1 = {'a' : 6,
                'b' : 53,
                'c' : 34,
                'd' : 2,
                'e' : 41}'''

'''for dato1 in diccionario1:
    #print(diccionario1)
    #print(dato1)
    #print(dato1, diccionario1)
    print(dato1, diccionario1[dato1])'''

'''diccionario2 = {'a' : 3,
                'b' : 26,
                'c' : 70,
                'd' : 58,
                'e' : 19}'''
'''for dato2 in diccionario2:
    print(diccionario2)
    #print(dato2)
    #print(dato, diccionario1[dato])'''


#UNIR LOS DICCIONARIOS
dic1 = {'a' : 6,
        'b' : 53,
        'c' : 34,
        'd' : 2,
        'e' : 41}

dic2 = {'a' : 3,
        'b' : 26,
        'c' : 70,
        'd' : 58,
        'e' : 19}

dic3 = {**dic1, **dic2}
print(dic3)

