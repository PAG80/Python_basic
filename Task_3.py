numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

# Проверяем условие
def is_odd_and_gt_50(x):
    return x > 50 and x % 2 != 0

# Используем filter() с нашей функцией
filtered_numbers = filter(is_odd_and_gt_50, numbers)

# Преобразуем результат в список и выводим
print(list(filtered_numbers))