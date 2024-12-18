"""
Сортировка выбором: selection sort
O():best = n^2
    worst = n^2
    ave = n^2
O_mem() = 1
"""
from random import randint
b = [randint(-20,20) for s in range(1,20)]

def selection_sort(b):
    for i in range(len(b)-1):
        min = i
        for j in range(i+1,len(b)):
            if b[j] < b[min]:
               min = j
        b[i],b[min] = b[min],b[i]

selection_sort(b)
print(b)