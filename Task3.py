# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

numbers = []

while(True):
        n = int(input('Введите следующее число. Для выходя введите "-1": '))   
        if n == -1:
            break
        else:
            numbers.append(n)
            
print(numbers)

unique_numbers = []

for i in range(len(numbers)):
    if numbers.count(numbers[i]) == 1:
        unique_numbers.append(numbers[i])

print(unique_numbers)