# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

# Первый способ
num = input('Введите число: ')
sum = 0
for a in num:
    if a.isdigit():
        sum += int(a)
print(f'- {num} -> {sum}')

# Второй способ
num = float(input('Введите число n: '))
m = len(str(num))
n = num * 10 ** (m-2)
print(n)
n = int(n)

def SumDigits (n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum

print(f'{num} -> {SumDigits(n)}')
