# Q1

def f_to_c_convert():
    temp_f=input("enter a temp in F: ")
    celcius = ((float(temp_f)-32)*5 / 9)
    print(f"That's {celcius} degrees in Celcius!")
    
f_to_c_convert()


#Q2 
def calculate_mean(total_sum, num_items):
    mean = total_sum / num_items
    return mean

def mean_machine():
    number_list = []
    while True:
        number_entry = input("Enter a number: ")
        if number_entry == '':
            break
        number_list.append(int(number_entry))
    num_items = len(number_list)
    total_sum = sum(number_list)
    mean = calculate_mean(total_sum, num_items)
    print(f"the mean of {number_list} is {mean}")

mean_machine()


# Q3




