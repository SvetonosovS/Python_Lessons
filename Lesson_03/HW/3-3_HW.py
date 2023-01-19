# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

input_num = int(input("введите число: "))

def Convertation (number):
    if int(number) >= 2:
        return str(Convertation(int(number/2))) + str(number % 2)
    if int(number) == 1:
        return '1'

print (Convertation(input_num))

# Способ 2

def conv_bin(num: int):
    list_nums = []

    while num > 0:
        list_nums.insert(0, num % 2)
        num //= 2

    print(*list_nums, sep="")


conv_bin(int(input()))