# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень k: '))

list_koef = [randint(0, 100) for i in range(k + 1)] 

polynomial = '+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(list_koef ) if j][::-1])

polynomial=polynomial.replace('x^1+', 'x+')
polynomial=polynomial.replace('x^0', ' = 0')
polynomial+=('','1')[polynomial[-1]=='+']
polynomial=(polynomial, polynomial[:-2])[polynomial[-2:]=='^1']
print(polynomial)
f = open("polynomial.txt", "w")
f.write(polynomial)
f.close()
