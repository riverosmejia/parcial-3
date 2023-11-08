#Defina una función que reciba un número
#y retorne el promedio de todos los números que vaya recibiendo.

def promedio_llamados():
  suma = 0
  contador = 0
  #numeros = []
  def promedio(numero):
    nonlocal suma
    nonlocal contador
    suma += numero #suma = suma + numero
    contador += 1
    return suma / contador

  return promedio

promedio = promedio_llamados()
print(promedio(5))
print(promedio(6))
print(promedio(7))
print(promedio(10))
print(promedio(8))
print(promedio(70))
print(promedio(700))