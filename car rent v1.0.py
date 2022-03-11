#Car Rental
print('Welcome to the University Car Rental System')
print('')
print('Vehicles avaliable to rent are:')
car_list = ["1. Suzuki Van - 2 Seats - ",
            "2. Toyota Corolla - 4 Seats - ",
            "3. Honda CRV - 4 Seats - ",
            "4. Suzuki Swift - 4 Seats - ",
            "5. Mitzubishi Airtrek - 4 Seats - ",
            "6. Nissan DC Ute - 4 Seats - ",
            "7. Toyota Previa - 7 Seats - ",
            "8. Toyota HI Ace 1 - 12 Seats - ",
            "9. Toyota HI Ace 2 - 12 Seats - "]
availability = [True, True, True, True, True, True, True, True, True]
for i in range(len(car_list)):
    if availability[i] == True:
        av = "Available"
    else:
        av = "Unavailable"
    print(car_list[i], av)


#Asking which car they want and getting an input
print('')
print('Which car would you like to rent out?')
print('(Enter the number assigned to the car of choice')
ask = True
while ask == True:
    try:
        what_car = int(input())
        if availability[what_car-1] == False:
            print('Car is unavailable')
        else:
            availability[what_car-1]=False
            for i in range(len(car_list)):
                if availability[i] == True:
                    av = "Available"
                else:
                    av = "Unavailable"
            print(car_list[what_car-1], av)
            ask = False
    except ValueError:
        print('Enter the assigned number')

print('Car is available')
print('What is your name? (first and last)')
