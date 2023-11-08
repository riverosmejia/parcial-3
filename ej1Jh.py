#Defina una función para calcular el promedio de los números pares de una lista de enteros
from functools import reduce

def promedio_pares_lista(lista):
  def es_par(num):
    return num%2 == 0 #return True o False

  def filtrar_num_pares(lista_numeros):
    return list(filter(es_par, lista_numeros)) #función y colección

  def sumatoria_valores(lista_numeros):
    return reduce(lambda x,y: x+y, lista_numeros)

  def promedio(lista_numeros):
    return sumatoria_valores(lista_numeros) / len(lista_numeros)

  return promedio(filtrar_num_pares(lista)) #848

lista_original = [2,3,4,43,63,4562,34,523,452,34]
promedio_pares_lista(lista_original)