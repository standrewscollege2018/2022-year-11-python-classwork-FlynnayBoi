#Car Rental
import time

# Set lists for cars, availability and renters
car_list = ["1. Suzuki Van - 2 Seats ",
                "2. Toyota Corolla - 4 Seats ",
                "3. Honda CRV - 4 Seats ",
                "4. Suzuki Swift - 4 Seats ",
                "5. Mitzubishi Airtrek - 4 Seats ",
                "6. Nissan DC Ute - 4 Seats ",
                "7. Toyota Previa - 7 Seats ",
                "8. Toyota HI Ace 1 - 12 Seats ",
                "9. Toyota HI Ace 2 - 12 Seats "]
availability = [True, True, True, True, True, True, True, True, True]
car_number_list = []
person_list = []

#Wecoming and creating while loops for the rest of the system
print('Welcome to the University Car Rental System')
car_rent_repeat = True
while car_rent_repeat == True:
    print('')
    print('Vehicles avaliable to rent are:')

    #Getting length of the list of cars and determining whether they can be
    #rented or not
    for i in range(len(car_list)):
        if availability[i] == True:
            av = "(Available)"
        else:
            av = "(Unavailable)"
        print(car_list[i], av)


    #Asking which car they want
    print('')
    print('Which car would you like to rent out?')
    print('(Enter the number assigned to the car of choice)')
    print('When car selection at the end of the day has ended,')
    print('enter 0 to display final statistics for the day.')
    ask = True

    #Making a while loop and checking if the number car selected is real or
    #not, grabbing an input to study
    while ask == True:
        try:
            what_car = int(input())
            if what_car > 9 or what_car < 0:
                print('Invalid car numeral')
            else:
                ask = False
        except ValueError:
            print('Enter the assigned number')
            

    #Just saying that if car selected is 0 then the renting loop ended
    if what_car == 0:
        car_rent_repeat = False
    else:
        #Determining what car is selected and if it is available
        if availability[what_car-1] == False:
            print('Car is unavailable')
        else:
            car_number_list.append(what_car-1)
            availability[what_car-1] = False
              
                    
            #Asking for name and stating what car has been selected
            print(f'Car is {av}')
            print('What is your name? (first and last)')

    
            #Assigning name to a variable and checking if two names were entered
            check = True
            while check == True:
                try:
                    name1, name2 = input().split(" ")
                    check = False
                except:
                    print("Enter both first and last name")

                
            #Combining names into one and adding it to a list and thanking the user
            person = name1 + " " + name2
            person_list.append(person)        
            print(f"Thank You, {person} for booking {car_list[what_car-1]}")
            time.sleep(2)
            print("")
            print("")
            print("--------------------------------------------------------------------")
            print("")

#If the car selected is 0, it prints the daily summary of what cars have been rented
if car_rent_repeat == False:
    print('')
    print('---------------------------------------------------------------')
    print('')
    print('')
    print('Daily Summary:')
    for i in range(0, len(car_number_list)):
        print(f'{person_list[i]}: {car_list[car_number_list[i]]}')
