def function(lista,palabra):

    palabras=lista.split()

    cont=0

    for i in palabras:

        if i==palabra:
            cont+=1

    diccionario={f'{palabra}':cont}

    return diccionario

print(function("hola mundo hola buenos días","hola"))