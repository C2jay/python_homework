#1 is it time for moths?

moths = input("are there moths? ")
    
if moths == "yes":
    print("Get the moths!")
else:
    print("No threats detected.")

#1 using Boolean 

moths_in_house = False

if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected.")


#2 is Mitch here for moth hunting?

moths_in_house = True
mitch_is_home = False

if (moths_in_house) and (mitch_is_home):
    print("Hooman! Help me get the moths!")
elif not (moths_in_house) and not (mitch_is_home):
    print("No threats detected")
elif (moths_in_house) and not (mitch_is_home):
    print("Meeeeeoooowww! Hisssssss!")
elif (mitch_is_home) and not (moths_in_house):
    print("Climb on Mitch")




#3 red light camera algorithm

light_colour = "amber"
car_detected = True

if (light_colour =="red") and (car_detected):
    print("flash")
else:
    print("Do nothing.")

#4 height requirement

height = eval(input("How many cms tall are you?: "))

if height < 120:
    print("sorry, not today :(")
elif height >= 120:
    print("Hop on!")
