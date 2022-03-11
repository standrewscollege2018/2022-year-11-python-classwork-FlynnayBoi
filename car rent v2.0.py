#Car Rental

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

print('Welcome to the University Car Rental System')
car_rent_repeat = True
while car_rent_repeat == True:
    print('')
    print('Vehicles avaliable to rent are:')

    for i in range(len(car_list)):
        if availability[i] == True:
            av = "(Available)"
        else:
            av = "(Unavailable)"
        print(car_list[i], av)


    #Asking which car they want and getting an input
    print('')
    print('Which car would you like to rent out?')
    print('(Enter the number assigned to the car of choice)')
    print('When car selection at the end of the day has ended,')
    print('enter 0 to display final statistics for the day.')
    ask = True
    
    while ask == True:
        try:
            what_car = int(input())
            if what_car > 9 or what_car < 0:
                print('Invalid car numeral')
            else:
                ask = False
        except ValueError:
            print('Enter the assigned number')
            

        
    if what_car == 0:
        car_rent_repeat = False
    else:
        
        if availability[what_car-1] == False:
            print('Car is unavailable')
        else:
            car_number_list.append(what_car)
            availability[what_car-1] = False
              
                    

            print(f'Car is {av}')
            print('What is your name? (first and last)')

    

            check = True
            while check == True:
                try:
                    name1, name2 = input().split(" ")
                    check = False
                except:
                    print("Enter both first and last name")

                

            person = name1 + " " + name2
            person_list.append(person)        
            print(f"Thank You, {person} for booking {car_list[what_car-1]}")
            print("")
            print("")
            print("--------------------------------------------------------------------")
            print("")


if car_rent_repeat == False:
    print('')
    print('---------------------------------------------------------------')
    print('')
    print('')
    print('Daily Summary:')
    for i in range(0, len(car_number_list)):
        print(f'{person_list[i+1]}: {car_list[car_number_list[i+1]]}')
