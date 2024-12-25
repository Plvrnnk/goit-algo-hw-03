import random

def get_numbers_ticket(min, max, quantity):
    ticket_list = []
    if min < 1:
        return ticket_list
    if max > 1000:
        return ticket_list
    if (max - min + 1) < quantity:
        return ticket_list
    while len(ticket_list) < quantity:
        new_number = random.randint(min, max)
        if new_number not in ticket_list: 
            ticket_list.append(new_number)
    return sorted(ticket_list)
    
ticket = get_numbers_ticket(10,14,6)
print("Generated ticket:", ticket)
