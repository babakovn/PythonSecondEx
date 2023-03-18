# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
from random import randint


print("Задача 10")
print("Введите количество монеток:")
n = int(input())

random_list = []
for i in range(n):
    random_list.append(randint(0,1))

print("1 - герб, 0 - решка")
print(random_list)

count_r = 0
count_g = 0

i = 0
while i < n:
    if random_list[i] > 0:
        count_r = count_r + 1
    else:
        count_g = count_g + 1
    i = i + 1

print("С гербом: ", count_g, "с решкой: ", count_r)

if count_r > count_g:
    print("Надо перевернуть монеты с гербом, их меньше")
else:
    print("Надо перевернуть монеты с решкой, их меньше")

