#otra solución para el primero
from functools import reduce
def even_list_average(list_):
    def is_even(number):
        return number % 2 == 0
    def list_average(list_):
        return reduce(lambda x, y: x+y, list_) / len(list_)

    even_numbers = list(filter(is_even, list_))
    return list_average(even_numbers)

even_list_average([2,3,4,5,6,7,8,10])