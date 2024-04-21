import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []  
    
    unique_numbers = set()
    
    while len(unique_numbers) < quantity:
        number = random.randint(min, max)
        unique_numbers.add(number)
    sorted_numbers = sorted(unique_numbers)
    
    return sorted_numbers


lottery_numbers = get_numbers_ticket(10, 20, 5)
print("Ваші лотерейні числа:", lottery_numbers)
