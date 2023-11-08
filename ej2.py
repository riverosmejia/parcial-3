#Defina una función contar_letras que recibe una cadena y retorna una función que cuenta la cantidad de veces que aparece una letra pasada como argumento en la cadena.

def contar_letras(lista1):

    cadena=list(filter(lambda x:x=='o',lista1))

    return len(cadena)

print(contar_letras('hola buenos días'))