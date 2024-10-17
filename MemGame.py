import random
import time
import os

points = 0
difficulty = 1
delay = 1

db = []

with open('words.txt', 'r', encoding="utf-8") as db_words:
    db = db_words.read().split('\n')

while True:
    sort = random.sample(db, 2)
    for i in sort:
        print(f'{i} ', end='')
    time.sleep(delay)
    os.system('cls')
    word = input('Enter the words: ').split(' ')
    if word == sort:
        points += 1
        if points % 10 == 0:
            if difficulty <= len(db):
                difficulty += 1
                delay += 0.1
    else:
        print('You loose!')
        print(f'the correct way is {sort}')
        print(f'{points=}!')
        break