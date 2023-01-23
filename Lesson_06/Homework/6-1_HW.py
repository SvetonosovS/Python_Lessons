# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# 
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]


# 1. Представлен список чисел. Необходимо вывести элементы
#    исходного списка, значения которых больше предыдущего элемента.
#    Use comprehension.

# 1. Представлен список чисел. Необходимо вывести элементы
#    исходного списка, значения которых больше предыдущего элемента.
#    Use comprehension.

from random import sample

def more_then(num):
    count = 3
    my_list = sample(range(num * count), num)
    print(my_list)
    return [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]


print(more_then(int(input("Введите количество чисел: "))))

#  ------------------------------------------- вариант решения ---------------------------------------------------------

from random import randint


def more_then(num):
    original_list = [randint(0, 1000) for _ in range(num)]
    print(original_list)
    return [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]


print(more_then(int(input("Введите количество чисел: "))))

