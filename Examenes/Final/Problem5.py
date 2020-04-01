# -*- coding: utf-8 -*-
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    inter = {}
    diff = {}
    for clave1 in d1.keys():
        if clave1 in d2.keys():
            inter[clave1] = f(d1[clave1], d2[clave1])
        else:
            diff[clave1] = d1[clave1]
    for clave2 in d2.keys():
        if clave2 not in d1.keys():
            diff[clave2] =  d2[clave2]
    return (inter, diff)
    
# =============================================================================
# The function will return a tuple of two dictionaries: 
#   a dictionary of the intersect of d1 and d2 and a dictionary of the 
#   difference of d1 and d2, calculated as follows:
# 
# intersect: The keys to the intersect dictionary are keys that are common 
#            in both d1 and d2. To get the values of the intersect dictionary, 
#            look at the common keys in d1 and d2 and apply the function f to 
#            these keys' values -- the value of the common key in d1 is the 
#            first parameter to the function and the value of the common key in
#            d2 is the second parameter to the function. Do not implement f 
#            inside your dict_interdiff code -- assume it is defined outside.        
# difference: a key-value pair in the difference dictionary is (a) every 
#             key-value pair in d1 whose key appears only in d1 and not in d2 
#             and (b) every key-value pair in d2 whose key appears only in d2 
#             and not in d1.
#
# Here are two examples:
# 
# If f(a, b) returns a + b
# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
# If f(a, b) returns a > b
# d1 = {1:30, 2:20, 3:30}
# d2 = {1:40, 2:50, 3:60}
# then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})
# 
# =============================================================================

# def f(a, b):
#     return a+b

def f(a, b):
    return a>b

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print(dict_interdiff(d1, d2))

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print(dict_interdiff(d1, d2))