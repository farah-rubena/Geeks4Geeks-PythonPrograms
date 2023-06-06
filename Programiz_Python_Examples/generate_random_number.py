'''WAPP to generate a Random Number
using the random module'''

import random

random_number = random.randint(1,100)
print(random_number)

#To generate a random float betwwen 0 and 1 use random.random

random_float = random.random()
print(f"{random_float:.2f}")