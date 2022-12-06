# Вычислить число c заданной точностью d

n = int(input("Введите число, задающее точность: "))
a = float(input("Введите вещественное число: "))
template = '{:.' + str(n) + 'f}'
print(template.format(a))