import random
import time
import os

# this funcion open the words file
def openFile ():
    try:
        with open('words.txt', 'r', encoding="utf-8") as db_words:
            w_list = db_words.read().split('\n')
            return w_list
    except FileNotFoundError:
        print('File not found.')
        return ''

# this function clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# this function welcomes
def welcome():
    clear_screen()
    print('Welcome to memory sort word game! look at the words below and memorize them!')
    time.sleep(2)
    clear_screen()

# this function save records
def save_records(name, points):
    with open('records.txt', 'a') as records:
        records.write(f'player name: {name}, record: {points}\n')

# this functions starts the game
def start(n_words, multiplier, points, delay):
    while True:
        if len(db) == 0: break
        sort = random.sample(db, n_words)
        for i in sort:
            print(f'{i} ', end='')
        print()
        time.sleep(delay)
        clear_screen()
        word = input('Enter the words: ').split(' ')
        if word == sort:
            points += 1
            print('that\'s right!')
            time.sleep(1)
            print(f'you earned {points} points')
            time.sleep(1)
            clear_screen()
            if points % multiplier == 0:
                delay += 0.1
                if n_words <= len(db):
                    n_words += 1
        else:
            print('You loose!')
            print(f'the correct way is {sort}')
            print(f'{points=}!')
            save_records(input('your name to save record: '), points)
            time.sleep(2)
            break

# Entry Point
# program constants

points = 0  # player points
delay = 2   # delay initial
n_words = 2 # initial amount of drawn words
multiplier = 5  # amount of points needed to level up

db = [] # Array of words.

welcome()
db = openFile()
start(n_words, multiplier, points, delay)