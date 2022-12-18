# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

number_quarter = int(input('Введите номер четверти: '))
if number_quarter == 1:
    print(number_quarter, '-> x > 0, y > 0')
elif number_quarter == 2:
    print(number_quarter, '-> x < 0, y > 0')
elif number_quarter == 3:
    print(number_quarter, '-> x < 0, y < 0')
elif number_quarter == 4:
    print(number_quarter, '-> x > 0, y < 0')
else:
    print(number_quarter, '-> нет такой четверти')