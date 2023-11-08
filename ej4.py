#Defina una función crear_calculadora que recibe una cadena con un operador (+, -, *, /) y retorna una función que aplica ese operador a dos números pasados como argumentos. Si el operador no es válido, la función debe retornar None.

def crear_calculadora(operatorList):

    def suma(num11,num21):

        return num11+num21

    def resta(num12,num22):

        return num12-num22

    def mult(num13,num23):

        return num13*num23
    
    def div(num14,num24):

        return num14/num24

    if(operatorList=='+'):

        return suma

    if(operatorList=='-'):

        return resta

    if(operatorList=='*'):

        return mult

    if(operatorList=='/'):

        return div

a=crear_calculadora('+')

print(a(2,3))