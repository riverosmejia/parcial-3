#Defina una función para calcular el promedio de los números pares de una lista de enteros
def function1(lista):

    def promedio( num, cont):

        return num/cont

    cont=0

    def suma(lista1):

        suma=0

        for i in lista1:

            suma=suma+i

        return suma

    for i in range (len(lista)):

        num=suma(lista)

        prom=0

        cont=i+1

        prom=promedio(num, cont)

        print(f'promedio: {prom}')
    
list = [1,2,3,4,5]

function1(list)