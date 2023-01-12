# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число n: '))

multiples = []
div = 2

while(n > 1):
    if n % div == 0:
        multiples.append(div)
        n = n / div
    else:
        div += 1
        
print(multiples)
    