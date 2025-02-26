def find_numbers_optimized(x):
    # Вычисляем все степени 3, 5 и 7, которые меньше или равны x
    powers_of_3 = []
    power = 1
    while power <= x:
        powers_of_3.append(power)
        power *= 3

    powers_of_5 = []
    power = 1
    while power <= x:
        powers_of_5.append(power)
        power *= 5

    powers_of_7 = []
    power = 1
    while power <= x:
        powers_of_7.append(power)
        power *= 7

    # Используем множество для хранения уникальных результатов
    result = set()

    # Перебираем все комбинации степеней
    for p3 in powers_of_3:
        for p5 in powers_of_5:
            if p3 * p5 > x:
                break  # Прерываем, если произведение уже превышает x
            for p7 in powers_of_7:
                xi = p3 * p5 * p7
                if xi > x:
                    break  # Прерываем, если произведение превышает x
                result.add(xi)

    return sorted(result)

# Пример использования
x = 100
print(find_numbers_optimized(x))