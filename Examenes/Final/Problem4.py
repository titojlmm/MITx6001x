# -*- coding: utf-8 -*-
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Temporal Dictionary
    tmp = {}
    for element in L:
       valor = tmp.get(element, 0)
       tmp[element] = valor+1
       
    # Recorremos las claves del diccionario y nos quedamos con el mayor de los impares
    mayor = None
    for clave in tmp.keys():
        if (tmp[clave] % 2 == 1) and (mayor==None or clave>mayor):
            mayor=clave
    return mayor


print(largest_odd_times([2,2,4,4]))

print(largest_odd_times([]))

print(largest_odd_times([3,9,5,3,5,3]))

print(largest_odd_times([-1, -1]))

print(largest_odd_times([-1, -3]))

