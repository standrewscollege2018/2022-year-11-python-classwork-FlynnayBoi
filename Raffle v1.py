import random
print('Raffle!')
print('What is the value of the cash prize?')
prize_repeat = True
while prize_repeat == True:
    try:
        prize = int(input())
        prize_repeat = False
    except ValueError:
        print('Enter a valid amount (no $ symbol)')
print(f'Cash Prize: ${prize}')
