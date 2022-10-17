# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.


from random import randint
print('Введите n:')
n = int(input())
numbers = []
for i in range(n):
    numbers.append(randint (-n,n))
print(f'Список из {n} элементов в промежутке [-{n}; {n}] ')
print(numbers)
list = [3, 6, 9]
result = numbers[list[0]] * numbers[list[1]] * numbers[list[2]]
print(f'Произведение элементов на индексах [{list[0]}, {list[1]}, {list[2]}] = {result}')