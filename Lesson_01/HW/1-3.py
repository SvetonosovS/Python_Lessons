# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), .причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

coord_x = int(input('Введите координату X: '))
coord_y = int(input('Введите координату Y: '))
if coord_x > 0 and coord_y > 0:
    print('1')
elif coord_x < 0 and coord_y > 0:
    print('2')
elif coord_x < 0 and coord_y < 0:
    print('3')
elif coord_x > 0 and coord_y < 0:
    print('4')
elif coord_x == 0 and coord_y == 0:
    print('Точка в начале координат')
elif coord_x == 0:
    print('лежит на оси X')
elif coord_y == 0:
    print('лежит на оси Y')