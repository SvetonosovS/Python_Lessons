# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def words_list(num, word='абв'):
    w_list = [] 
    for i in range(num):
        m = sample(word, k=3)
        w_list.append("".join(m))
    return w_list

number = int(input('Введите колличество слов: '))

txt = words_list(number)
print(' '.join(txt))

find_txt = 'абв'

lst = [i for i in txt if find_txt not in i]
print(" ".join(lst))