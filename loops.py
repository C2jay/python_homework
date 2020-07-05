# Q1

number_list = []
while True:
    number_entry = input("Enter a number: ")
    if number_entry == '':
        break
    number_list.append(int(number_entry))
total_sum = sum(number_list)
print(f"the sum of {number_list} is {total_sum}")



# Q2

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

counter = 0
name_list = []
while counter < 3:
    names = input("Enter a name: ")
    name_list.append(names)
    counter += 1
for name in name_list:
    print(name)


# Q4
groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

for item in groceries:
    item_amount = input(f"How many {item[0]} did you buy?")
    item.append(item_amount)

total_cost = 0

print("====== Izzy's Food Emporium ======")
for item in groceries:
    cost = item[1]*float(item[2])
    total_cost += cost
    print(f"{item[0]:<20} ${round(float(cost)):.2f}")
print("=="*17)
print(f"total amount:     ${round(float(total_cost)):.2f}")
