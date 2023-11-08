#(2.5 puntos) Cree una función que reciba una matriz de enteros positivos de NxN y devuelva la diferencia entre la sumatoria de la diagonal principal y la productoria de la diagonal secundaria.
#(0.5 puntos)  Incluya funciones internas. 
#(1 punto) Cree un closure que reciba el operador "+" o "-" y que devuelva una función para calcular la sumatoria o productoria de una lista con base en el operador recibido.  
#(1 punto) Para extraer los elementos de las diagonales use funciones recursivas.

def sumatoria(matriz,operatorList):

    larX1=len(matriz)

    larY1=larX1

    a1=0

    a2=0

    def crear_calculadora(operatorList):

        def suma(num11,num21):

            return num11+num21

        def resta(num12,num22):

            return num12-num22

        if(operatorList=='+'):

            return suma

        elif(operatorList=='-'):

            return resta

    def recorrerPrincipal(matriz,X,Y,sumaPrin=0):
    
        if X>=len(matriz) and Y>=len(matriz[0]):

            return int(sumaPrin)

        else:

            sumaPrin += int(matriz[X][Y])
            
            a=recorrerPrincipal(matriz,X+1,Y+1,sumaPrin)

        return a

    def recorrerSecundaria(matriz,X,Y,sumaPrin=0):
    
        if X>=len(matriz) and Y<=0:

            return int(sumaPrin)

        else:

            sumaPrin += int(matriz[X][Y])
            
            a=recorrerSecundaria(matriz,X+1,Y-1,sumaPrin)

        return a

    a1=recorrerPrincipal(matriz,0,0)

    a2=recorrerSecundaria(matriz,0,larY1-1)

    print(f'suma diagonal principal: {a1} \nsuma diagonal secundaria: {a2}')

    a=crear_calculadora(operatorList)

    print(f'{a1}-{a2} = {a(a1,a2)}')

    return a1,a2

#FIN DE LA FUNCIÓN

matriz=[
    [1,2,3],
    [4,5,6],
    [1,8,9]
    ]

num1,num2=sumatoria(matriz,'+')
