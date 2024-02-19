import os
os.system('cls')

"""
Enunciado:
Dada una lista de 5 elementos, invertirla sin aplicar funciones propias de python. ([1,2,3,4,5] --> [5,4,3,2,1])
"""

def reverse_list(my_list):

    n = len(my_list) - 1

    for i in range ((n//2)):
        my_list[i], my_list[n-i] = my_list[n-i], my_list[i] # one-line swap
    
    return my_list


my_list = [1,2,3,4,5]
print(my_list)
my_list = reverse_list(my_list)
print(my_list)



