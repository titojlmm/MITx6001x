# -*- coding: utf-8 -*-

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    result = 0
    try:
        result = item / denom
    except ZeroDivisionError:
        result = 0
           
    return result

print(fancy_divide([0, 2, 4], 0))

