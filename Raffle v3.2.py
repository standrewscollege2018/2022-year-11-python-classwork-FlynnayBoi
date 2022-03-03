#Raffle yay
import time
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
print('Type END when you are finished entering names.')

while name_repeat == True:
    name_append = input()
    name_append = name_append.lower()
    if name_append == "end":
        print('Name input ended')
        name_repeat = False
    elif name_append.isalpha():
        name_list.append(name_append)
    else:
        print('Invalid name')
print(f'List contains:{name_list}')
name_length = len(name_list)


print('Initiate Raffle?')
print('Yes? or No?')
raffle_repeat = True

while raffle_repeat == True:
    raffle_run = input()
    raffle_run = raffle_run.lower()
    if raffle_run == "yes":
        print('Raffling!')
        raffle_repeat = False
    elif raffle_run == "no":
        print('Bruh')
        time.sleep(2)
        print('Start Raffle? Yes? or No?')
    else:
        print('Start Raffle? Yes? or No?')


if name_length == 0:
    print('Nobody won because there were no participants')
else:
    random_name = random.randint(0, name_length)
    time.sleep(1)
    print(f'The Winner is {name_list[random_name]}')


no_break = True
while no_break == True:
    infinite_no_break = input()
