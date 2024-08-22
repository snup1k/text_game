from random import randint
from time import sleep
from unittest import result
from heplers import *
from data import *

name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0

def earn():
    print('Добро пожаловать на завод! У тебя есть 66.66% шанс заработать 500 монет. Соответственно, 33.33% чтобы их потерять')
    result = randint(1, 100)
    sleep(1.5)
    print('Результат....')
    sleep(1.5)
    print('Страшно?!')
if result < 67:
        print('Вы выиграли 500 монет!')
        player['money'] += 500
else:
        print('Вы проиграли 500 монет :(')
        player['money'] -= 500
print()
print(f'Осталось монет: {player["money"]}')
print()
while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка
3 - Магазин
4 - Показать инвентарь
5 - Информация об игроке
6 - Информация о текущем противнике
7 - Показать items
8 - Завод
''')
    if action == '1':
        current_enemy = fight(current_enemy)
        if current_enemy == 3:
            break
    elif action == '2':
        training_type = input('''1 - тренировать атаку
2 - тренировать оборону
''')
        training(training_type)
    elif action == '3':
        shop()
    elif action == '4':
       display_inventory()
    elif action == '5':
        display_player()
    elif action == '6':
        display_enemy(current_enemy)
    elif action == '7':
        get_items()
    elif action == '8':
        earn()