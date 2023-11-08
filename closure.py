#Ejemplo 1
def generate_power(exponent): #2
  def power(base): #
      return base ** exponent
  return power

#Cómo lo uso?
pt2 = generate_power(2)
pt3 = generate_power(3)
pt2(10)
pt3(10)