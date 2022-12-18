# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1
#
# out
# # 5.099

coord_x1 = int(input('Введите X первой точки: '))
coord_y1 = int(input('Введите Y первой точки: '))
coord_x2 = int(input('Введите X второй точки: '))
coord_y2 = int(input('Введите Y второй точки: '))

# Первый вариант решения, через обьявление новой переменной:
# distance = round(((coord_x2 - coord_x1) ** 2 + (coord_y2 - coord_y1) ** 2) ** 0.5, 4)
# print(distance)

# Второй вариант решения, через создание функции:
# def distance(x1, y1, x2, y2):
#     return round(((coord_x2 - coord_x1) ** 2 + (coord_y2 - coord_y1) ** 2) ** 0.5, 4)
# print(f'{distance(coord_x1, coord_x2, coord_y1, coord_y2)}')

# Третий вариант решения, формула в выводе:
print(round(((coord_x2 - coord_x1) ** 2 + (coord_y2 - coord_y1) ** 2) ** 0.5, 4))