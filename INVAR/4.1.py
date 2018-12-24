4.1 Создание программы по заполнению массивов случайными значениями.
Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.


import numpy as np
import numpy.random 

"""создание массива со случайными целыми числами"""
array = np.random.randint(0, 10, 10)
a = np.arange(10)

sort_array = sorted(array)
reverse_array = sorted(array, reverse = True)

choice_array = np.random.choice(a, 10, replace = True)
permutation_array = np.random.permutation(array)

print('Рандомный массив')
print(array)

print('Сортировака по возрастанию')
print(sort_array)

print('Сортировка по убыванию')
print(reverse_array)

print('Выборка с помощью функции choice')
print(choice_array)

print('С помощью функции permutation')
print(permutation_array)

"""Метод простой вставки"""
def Just_insert(lst = np.random.randint(0, 10, 10)):
    for i in range(len(lst) - 1):
        j = i - 1 
        key = lst[i]
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst
print('Метод простой вставки')
print(Just_insert(array))


"""Метод плавной сортировки"""
def Smooth_Sort(lst):
    def downHeap(lst, k, n):
        new_elem = lst[k]
        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and lst[child] < lst[child+1]:
                child += 1
            if new_elem >= lst[child]:
                break
            lst[k] = lst[child]
            k = child
        lst[k] = new_elem
    size = len(lst)
    for i in range(size//2-1,-1,-1):
        downHeap(lst, i, size)
    for i in range(size-1,0,-1):
        temp = lst[i]
        lst[i] = lst[0]
        lst[0] = temp
        downHeap(lst, 0, i)
    return lst

print('Метод плавной сортировки')
print(Smooth_Sort(array))
