#* 4. Напишите программу, которая принимает на вход 2 числа.
#Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
#Найдите произведение элементов на указанных позициях(не индексах).
#Enter the value of N: 5
#Position one: 1
#Position two: 2
#-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#-> 20

#Enter the value of N: 4
#Position one: 20
#Position two: 22
#-> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
#-> There are no values for these indexes!

num = int(input('Enter the value of N: '))
n_1 = int(input('Position one: '))
n_2 = int(input('Position two: '))

nums_list = list(range(-num, num + 1))

print(nums_list)
len_list = len(nums_list)

if len_list >= n_1 > 0 and len_list >= n_2 > 0:
    print(nums_list[n_1 - 1] * nums_list[n_2 - 1])
else:
    print('There are no values for these indexes!')