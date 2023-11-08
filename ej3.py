#Defina una función que reciba un número y retorne el promedio de todos los números que vaya recibiendo.

def function1(supper_num,cant):

    return supper_num/cant

retorno=True

cant=0

num1=0

while retorno:

    cant=cant+1

    num=input('inserte un número: ')

    num=int(num)

    num1=num1+num

    prom=function1(num1,cant)

    resp=input('\ndesea ingresar otro número? S/N: ')

    if resp =='S' or resp =='s':

        retorno=True

    else:

        print(prom)

        retorno=False