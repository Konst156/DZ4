# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число N: "))
i = 2
list_multiplier = []
while i * i <= n:
    while n % i == 0:
        list_multiplier.append(i)
        n = n / i
    i = i + 1
if n > 1:
    list_multiplier.append(int(n))
print(list_multiplier)