# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

input_num = int(input("введите число: "))

list = [0 , 1]

for i in range(2, input_num+1):
    list.append(list[i-1]+list[i-2])

for i in range(1, input_num+1):
    list.insert(0, ((-1)**(i+1))*(list[i*2-1])) # ((-1)**(i+1)*Fi)

print (*list)


#-----------------------------------------------------------------
def neg_fib(num: int):
    a, b = 1, 1
    list_nums = [0]

    for i in range(num):
        list_nums.append(a)
        list_nums.insert(0, a * (-1) ** i)
        a, b = b, b + a

    return list_nums


print(*neg_fib(int(input())))