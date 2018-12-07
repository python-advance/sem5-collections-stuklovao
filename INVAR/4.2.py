4.2  Создание программы по распределению списка с случайными значениями на два списка по определенному критерию 
(четность/нечетность, положительные/отрицательные числа).

import random
array = []

for i in range(10):
    array.append(int(random.random() * 10) - 5)

plus_num = []
minus_num = []

for i in array:
    if i < 0:
        minus_num.append(i)
    elif i > 0:
        plus_num.append(i)
print('Рандомный список')       
print(array)
print('Положительный список') 
print(plus_num)
print('Отрицательный список') 
print(minus_num)
print()

chetn_array = []
nechetn_array = []

for i in array:
  if array[i]%2 == 0:
		    chetn_array.append(array[i])
  else:
        nechetn_array.append(array[i])
       
print("Четный список")
print(chetn_array)
print("Нечетный список")
print(nechetn_array)
