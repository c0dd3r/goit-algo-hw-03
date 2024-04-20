import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers
