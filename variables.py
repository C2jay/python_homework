#1 takes 2 numbers and output their sum

num_1= eval(input("Enter a number: "))
num_2= eval(input("Enter a second number: "))

print(f" {num_1} + {num_2} is", num_1+num_2)


#2 takes 2 numbers and outputs their multiplied number

num_1 = eval(input("Enter a number: "))
num_2 = eval(input("Enter a second number: "))
print(f"{num_1} x {num_2} is", num_1*num_2)




#3 takes distance in km and outputs distance in m and cm

km=eval(input("Enter a distance in kilometers: "))
meters=km*1000
cm=km*100000
print(f"{km}km = {int(meters)} meters and {int(cm)} cm")




#4 takes user name and height and outputs a sentence

name = input("What is your name?: ")
height = eval(input("How many centimeters tall are you?: "))
print(f"{name} is {height}cms tall.")