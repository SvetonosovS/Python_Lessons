# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

n = int(input('Введите число N: '))

temp_num = 1
for i in range (n):
    temp_num *= i + 1
    print(temp_num, end= ' ')

# способ 2

num = int(input('Введите число N: '))
sum_dig = 1
new_list = []

for i in range(num):
    sum_dig *= i + 1
    new_list.append(sum_dig)
print(new_list)