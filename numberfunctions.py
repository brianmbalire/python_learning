import random
print(random.random())
print(random.randint(1, 100))

# validating random numbers
x = 7.0
print(x.is_integer())

y = 7.5
print(y.is_integer())

a = 7
print(isinstance(a, int))
print(isinstance(a, float))

# generate a random number between 1 and 100 and check if it is even or odd

import random

number = random.randint(1, 100)

print("Generated number:", number)

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")