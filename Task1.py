# 1.Пользователь вводит число, нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)

n = int(input('Задайте точность: '))
k = 1
sum = 0

for i in range(n):
    if i % 2 == 0:
        sum += 4 / k
    else:
        sum -= 4 / k
    k += 2
    
print(sum)

