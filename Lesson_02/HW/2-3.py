# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071


num = int(input('Введите число N: '))
sum_num = 0
list_nums =[]

for i in range(1, num + 1):
    result = round((1 + 1 / i) ** i, 3)
    list_nums.append(result)
    sum_num += result

print(list_nums)
print(sum_num)

#
exit()
user_number = int(input('Введите число n: '))
print(f'n= {user_number} ', end='[')

for i in range(1, user_number):
    print(round((1 + 1 / i) ** i, 3), end=', ')
print(f'{round((1 + 1 / user_number) ** user_number, 3)}]')