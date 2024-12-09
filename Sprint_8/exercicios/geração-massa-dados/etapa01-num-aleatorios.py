import random

random_numbers = [random.randint(1, 500) for i in range(250)]

random_numbers.reverse()

print(random_numbers)