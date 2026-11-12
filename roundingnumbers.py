# measure distance between two points
print(abs(2 - 10)) # abs() returns the absolute value of a number

# round() rounds a number to the nearest integer
import math
price = 35.542
print(round(price))
print(math.floor(price)) # floor() rounds down to the nearest integer on the floor down
print(math.ceil(price)) # ceil() rounds up to the nearest integer on the ceiling up

print(round(price, 2)) # round() can also take a second argument for the number of decimal places
print(round(price, 1))

#remove decimal places from a number
print(math.trunc(price)) # trunc() removes the decimal places from a number


