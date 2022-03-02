#Raffle yay
import random
print('Raffle!')
print('What is the value of the cash prize?')
prize_repeat = True
while prize_repeat == True:
    try:
        prize = int(input())
        if prize < 0:
            print('Enter a valid amount (can\'t be negative)')
        if prize >= 0:
            prize_repeat = False
    except ValueError:
        print('Enter a valid amount (no $ symbol)')
print(f'Cash Prize: ${prize}')


name_repeat = True
name_list = []
print('Who will be entering this raffle?')
print('Type end or End when you are finished entering names.')
while name_repeat == True:
    name_append = input()
    if name_append == "end" or name_append == "End":
        print('Name input ended')
        name_repeat = False
    elif name_append.isalpha():
        name_list.append(name_append)
    else:
        print('Invalid name')
print(f'List contains:{name_list}')
