"""
Сортировка Шелла улучшение сортировки вставками
O():best = n*log^2(n)
    worst = n^2
O_mem() = 1
"""
from random import randint
b = [randint(-20,20) for s in range(1,20)]

def Shell_sort(b):
    last_ind = len(b)
    step = len(b)//2
    while step > 0:
        for i in range(step,last_ind):
            j = i
            delta = j - step
            while delta >= 0 and b[delta] > b[j]:
                b[delta],b[j] = b[j],b[delta]
                j = delta
                delta = j - step
        step //= 2

Shell_sort(b)
print(b)