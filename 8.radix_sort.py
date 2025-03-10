"""Поразрядная сортировка
O():worst = w*n, w - количество бит,требуемых для хранения каждого ключа.
O_mem(): w+n
"""
from random import randint
b = [randint(0,40000) for s in range(1,20)]



def get_number_of_digits(number):
    return len(str(number))

def get_digit(number,i):
    return (number % (10**(i+1)))//(10**i)

def max_number_of_digits(numbers):#для выравнивания
    number_of_digits = 1
    for number in numbers:
        cur_digits = get_number_of_digits(number)
        number_of_digits = max(number_of_digits,cur_digits)
    return number_of_digits

def counting_sort(sequince,position):
    min_key = min([get_digit(x,position) for x in sequince])
    max_key = max([get_digit(x,position) for x in sequince])
    n = max_key - min_key + 1
    support = [0 for i in range(n)]
    for el in sequince:
        support[get_digit(el,position)-min_key] += 1
    size = len(sequince)
    for i in range(n-1,-1,-1):
        size -=support[i]
        support[i] = size
    result = [None for i in range(len(sequince))]
    for el in sequince:
        result[support[get_digit(el,position)-min_key]] = el
        support[get_digit(el,position)-min_key]+=1
    return result

def radix_sort(sequince):
    number_of_digits = max_number_of_digits(sequince)
    for i in range(number_of_digits):
        sequince = counting_sort(sequince,i)
    return sequince

print(b)
print(radix_sort(b))    

