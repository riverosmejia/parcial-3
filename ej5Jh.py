#Defina una función crear_calculadora que recibe una cadena con un operador (+, -, *, /)
#y retorna una función que aplica ese operador a dos números pasados como argumentos.
#Si el operador no es válido, la función debe retornar None.

def calculadora(operador):
  def sumar(n1, n2):
    return n1 + n2
  def restar(n1, n2):
    return n1 - n2
  def multiplicar(n1, n2):
    return n1 * n2
  def dividir(n1, n2):
    return n1 / n2

  #a preguntar por tipo de operador
  if(operador == "+"):
    return sumar
  elif(operador == "-"):
    return restar
  if(operador == "*"):
    return multiplicar
  elif(operador == "/"):
    return dividir
  else:
    return None

suma = calculadora("+")
resta = calculadora("-")
mult = calculadora("*")
div = calculadora("/")
