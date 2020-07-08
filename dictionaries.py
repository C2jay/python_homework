# Q1
groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}


for item, price in groceries.items():
    item_amount = input(f"How many {item} did you buy?")
    groceries[item] = [price, item_amount]
print(groceries)


print("====== Izzy's Food Emporium ======")
total_cost = 0
for item, value in groceries.items():
    cost = float(value[0])*float(value[1])
    print(f"{item:<20} ${round(cost):.2f}")
    total_cost += cost
print("=="*17)
print(f"total amount:     ${round(float(total_cost)):.2f}")



#Q2
from collections import Counter
names = [
"Maddy", "Bel", "Elnaz", "Gia", "Izzy",
"Joy", "Katie", "Maddie", "Tash", "Nic",
"Rachael", "Bec", "Bec", "Tabitha", "Teagen",
"Viv", "Anna", "Catherine", "Catherine", "Debby",
"Gab", "Megan", "Michelle", "Nic", "Roxy",
"Samara", "Sasha", "Sophie", "Teagen", "Viv"
]

print(Counter(names))


#Q3

