#(2.5 puntos) Cree una función que reciba una lista de strings alfabéticos y que devuelva una nueva lista donde se hayan removido todos las consonantes de cada uno de estos strings. Finalmente, retorna un nuevo string donde se juntan todos los strings filtrados. 

#Ejemplo: dada la lista L = ["HolA", "MUndo"], la función debería retornar "oAUo". 

#(1 punto) Cree una función de filtrado para eliminar las consonantes.

#(0.5 puntos) Use funciones anónimas.

#(1 punto) Use una función de orden superior para crear el string resultante.

from functools import reduce

def function(list,pal):

    vocales = ('a', 'e', 'i', 'o', 'u')

    def N(pal,lista=''):

        for letra in pal:

            if letra.lower() in "aeiou":

                lista=lista+letra

        result= reduce(lambda x,y:x+y, lista)

        return result

    result=N(list)

    return result

frase="BuENOs DiAs"

print(f'frase: {frase} resultante: {function(frase,0)}')
                
