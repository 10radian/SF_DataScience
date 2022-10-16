"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

count = 0
mx = 100
mn = 1

def get_secret_number():
    """Функция создает число из диапазона, которое необходимо угадать
    """

    secret_number = np.random.randint(mn, mx+1)
    str_secret_number = str(secret_number)
    return str_secret_number

def guess_number():
    """Возвращает строку догадки и секретного числа
    """
    
    secret_num = get_secret_number()
    guess = str(np.random.randint(mn, mx+1))
    
    #Создание пустого списка
    guessed = [0]*len(guess)
    
    
    #if guess == secret_num:
    #    count += 1
    
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            #правильная цифра на правильном месте
            guessed[i] += int(guess[i])
    #    elif guess[i] in secret_num:
    #        #правильная цифра в неправильном месте
    #        guessed.append(guess[i])
        
#    print(guess, secret_num)
#    print(guessed)    
 
    

guess_number()    