import random
import numpy as np

n = int(input("Введите размер массива: "))
array = np.zeros(n)
for i in range (n):
    array[i]=random.randrange(300)
print("Начальный массив: ", array)
min = array[0]
min_index = 0
for i in range(n):
    if array[i]<min:
        min = array[i]
        min_index = i
array[2]=min
array[min_index]=9999
print("Преобразованный массив: ", array)
