#Raffle yay
import time
import random
#Asking the amount being raffled
print('Raffle!')
print('What is the value of the cash prize?')



#Making an infinite loop where only a positive integer can be entered to continue
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



#Making an infinite loop where names can be entered until 'end' is inputted
name_repeat = True
name_list = []
print('Who will be entering this raffle?')
print('Type END when you are finished entering names.')


name_fix = "filler"
name_list.append(name_fix)
while name_repeat == True:
    name_append = input()
    name_append = name_append.lower()
    if name_append == "sea-am":
        name_list.append(name_append)
    elif name_append == "end":
        print('Name input ended')
        name_repeat = False
    elif name_append.isalpha():
        name_list.append(name_append)
    else:
        print('Invalid name')
name_list.append(name_fix)
print(f'List contains:{name_list}')
#Getting the length of the list of names
name_length = len(name_list)



#Start the raffle or no?
print('Initiate Raffle?')
print('Yes? or No?')
raffle_repeat = True



#Infinite loop for starting raffle or not
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



#If there's no names in the raffle, this says that nobody wins instead of outputting an error
if name_length == 0:
    print('Nobody won because there were no participants')
#Displaying the winner of the raffle by converting a random integer to the name equivalent on the list of names
else:
    random_name = random.randint(1, name_length-1)
    time.sleep(1)
    print(f'The Winner is {name_list[random_name]}')



#Completely unneccesary but saying that you can enter inputs infinitely after the raffle is done so there is no errors ever
no_break = True
while no_break == True:
    infinite_no_break = input()
