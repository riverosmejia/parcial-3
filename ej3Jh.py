#Defina una función contar_letras que recibe una cadena y retorna una función que cuenta
#la cantidad de veces que aparece una letra pasada como argumento en la cadena.

def contar_letras(cadena):
  def contar_letra(letra):
    return cadena.count(letra)

  return contar_letra

contar = contar_letras("hola")
print(contar("a")) #--> cuántas "a's" hay? --> en la cadena original "hola"
print(contar("b")) #--> cuántas "b's" hay? --> en la cadena original "hola"
print(contar("c")) #--> cuántas "c's" hay? --> en la cadena original "hola"

contar = contar_letras("lenguajes de programación")
print(contar("a")) #--> cuántas "a's" hay? --> en la cadena original "lenguajes de programación"
print(contar("b")) #--> cuántas "b's" hay? --> en la cadena original "lenguajes de programación"
print(contar("c")) #--> cuántas "c's" hay? --> en la cadena original "lenguajes de programación"