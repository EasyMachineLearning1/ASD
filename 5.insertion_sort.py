"""
элементы входной последовательности просматриваются по одному, и каждый новый поступивший элемент размещается в подходящее место среди ранее упорядоченных
O():best = n
    worst = n^2
    ave = n^2
O_mem() = n
"""
from random import randint
b = [randint(-20,20) for s in range(1,20)]

def insertion_sort(b):
    for i in range(1,len(b)):
        j = i-1
        while j>=0 and b[j]>b[j+1]:
            b[j],b[j+1] = b[j+1],b[j]
            j-=1

insertion_sort(b)
print(b)