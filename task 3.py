# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list_data = [int(i) for i in input('Введите список из нескольких чисел через пробел: ').split()]
list_non_repeating = []
for i in range(len(list_data)):
    if list_data.count(list_data[i]) == 1:
        list_non_repeating.append(list_data[i])
print(list_non_repeating)
