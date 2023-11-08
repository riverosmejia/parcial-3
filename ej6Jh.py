#Defina una función crear_contador que retorna una función que cuenta
# la cantidad de veces que ha sido llamada. La función retornada
# debe tener un atributo contador que almacena la cantidad de veces que ha sido llamada.

def crear_contador():
  cont = 0
  def conteo():
    nonlocal cont
    cont += 1 #cont = cont + 1
    return cont
  return conteo

c = crear_contador()
c()
c()
c()
c()
c()
c()