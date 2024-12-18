# сортировка расческой
from random import randint
b = [randint(-20,20) for s in range(1,20)]

def comb_sort(b):
    step = int(len(b)/1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(b):
            if b[i] > b[i+step]:
                b[i],b[i+step] = b[i+step],b[i]
                swap+=1
            i += 1
        if step > 1:
            step = int(step/1.247)

comb_sort(b)
print(b)