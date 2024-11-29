import random

def quantity_check(quantity, min_val, max_val): # creating an additional function that checks the correctness of the quantity entered.
    while quantity < 2 or quantity > (max_val - min_val + 1): # setting while-clause
        print('Quantity must be at least 2 and fit within the range size.')
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return quantity

def get_numbers_ticket(min_val, max_val, quantity):
    ticket_list = [] # creating our ticket-list
    while min_val < 1 or max_val > 1000 or max_val - min_val + 1 < quantity: # setting while-clause
        try:
            min_val = int(input("Enter min (>= 1):"))
            max_val = int(input("Enter max (<= 1000):"))
            quantity = quantity_check(quantity, min_val, max_val)
        except ValueError:
            print("Invalid input. Please enter valid integers.")
    while len(ticket_list) < quantity: # checking if the length of the list does not exceed the required quantity
        new_number = random.randint(min_val,max_val) #creating our values for ticket
        ticket_list.append(new_number) # inserting values
        ticket_list = sorted(ticket_list) # sorting the list
    return ticket_list

ticket = get_numbers_ticket(1, 50, 5)
print("Generated ticket:", ticket)
