# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in    7
# out   [4, 5, 3, 3, 4, 1, 2]
#       [5, 1, 2]

# in -1
# out   Negative value of the number of numbers!
#        []

# in 10
# out   [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
#       [6, 2, 3, 0, 9]


from random import randint

def random_num(amount):
    new_list = []
    if amount > 0:
        new_list = [randint(1, 10) for i in range(amount)] 
        return(new_list)
    else:
        print('Negative value of the number of numbers!')
        
num_list = random_num(int(input('Введите колличество чисел - ')))
print(num_list)

def dubl_filter(num_list):
    result = list(filter(lambda x: num_list.count(x) < 2, num_list))
    print(result)


dubl_filter(num_list) if (not num_list == []) else dubl_filter()