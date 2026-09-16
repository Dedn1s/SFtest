"""Игра по угадыванию числа
   компьютер сам загадывает и угадывает
   новая ветка"""

import numpy as np

start = 1
finish = 101
number = np.random.randint(start, finish)

count = 0

while True:
    predict_number = np.random.randint(start, finish)
    count+=1
    
    if predict_number < number:
        start = predict_number + 1
    elif predict_number > number:
        finish = predict_number
    else:
        print(f"Компьютер угадал число за {count} попыток. Это было число {number}. Тест корректности - {predict_number}")
        break