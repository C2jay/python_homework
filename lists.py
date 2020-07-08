# lists
#Q1

foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]
print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print (foods[6][-1])


#Q2

mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park",]
]

for pets in mailing_list:
    print(f"{pets[0]}: {pets[1]}")


#Q3

def name_generator():
    name_list = []
    for i in range(3):
        name = input("Enter a name: ")
        name_list.append(name)
    print(name_list)
    
name_generator()



#Q4
sentence = input("Write me a sentence!: ")
string_list = []
words = sentence.split()
print(len(words), words)
for letter in sentence:
    string_list.append(letter)
print(len(string_list), string_list)
