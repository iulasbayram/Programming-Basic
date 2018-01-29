# Student Name: Ismail Ulas Bayram
# Student ID: 220201040

greeting=raw_input("Welcome our company. What is your name?")
print "We are plaesed to meet you" , greeting

print "Our car list according to brands"

car_list=[['BMW',4,False,200],['Mercedes',3,False,250],['Renault',2,False,150],['Audi',3,False,180]]
print car_list

# Below that I used for loob and 2 parameters.
def sell_car(brand, car_list) :
    for car in car_list:
        if car[0]==brand:
            if car[1]>0:
                car[1]=car[1]-1
            else:
                print "You enter undefined brand. Please, try again."
    print "Updated car list is below"
    print car_list

# Below that I used two for loobs because i rented car easily with two for loob and I used 3 parameters.
def rent_car(selected_rent_brand, car_list):
    for car in car_list:
        for i in car:
            if i == selected_rent_brand:
                if (car[2] == False and car[1]>0 ):
                    car[2]=True
                    car[1]= car[1]-1
                    print "Updated car list is below"
                    print car_list
                elif car[1]<0 :
                    print "Unfortunately, We don't have this brand yet."
                elif car[2]== True:
                    print "This brand is rented by someone."


# Below that I used one for loob for changing situation of rent and I used 2 parameters.
def return_car(brand,car_list):
    for car in car_list:
        if car[0]==brand:
            if car[2]== True :
                car[2]= False
                car[1]=car[1]+1
            elif car[2]== False:
                print "This brand isn't rented previously."
            print car_list


# Below that I used "return" because I defined new list for executing. Apart from these, I used one for loob and 3 parameters.
# Again below that if user doesn't want to take input, He/She should write "print" before he/she calls the function.
def give_car_list(lower_horsepower,upper_horsepower,car_list):
    suggested_car=[]

    for car in car_list:
        if lower_horsepower <= car[3] <= upper_horsepower:
            suggested_car.append(car)
    return suggested_car


# Below that I used for-else loob because if given values didn't sort together, the program passed to next step. I used 3 parameters.
# Again below that I used "break" because before print of updated list, not due to execute again and again, I wrote "break".
def add_car(brand,horsepower,car_list):
    for car in car_list:
        if car[0]== brand and car[3]== horsepower:
            car[1]= car[1] + 1
            break
    else:
        car_list.append([brand, 1, False, horsepower])


print car_list

















