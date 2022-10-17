#Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.


n = int(input('Введите n:'))
sum = 0
if n < 1:
        start = n; finish = 1
else:
        start = 1; finish = n
while start <= finish:
    if start % 2 == 0:
        sum = sum + start
        start = start + 1
    else:
        start = start + 1
print(f'Сумма четных чисел от 1 до {n} = {sum}')

