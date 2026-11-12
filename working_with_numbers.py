x = 5
y = 5.7
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

#converting data to numerical values
x = "5"
print(type(x))
x = int(x)
print(type(x))
print(x + 5)

a = 5
print(float(a))

x = 3 # real
y =4 # imaginary
print(complex(x,y))



# Math operators
print(5 + 3)
print(5 - 3)    
print(5 * 3)
print(5 / 3)
print(5 // 3) # floor division
print(5 % 3) # modulus, you get the leftover part after the division
print(5 ** 3) # exponentiation, 5 to the power of 3

# shorthand operators
x = 5   
x = x + 3
print(x)
x += 3  # equivalent to x = x + 3
x -= 3  # equivalent to x = x - 3
x *= 3  # equivalent to x = x * 3
x /= 3  # equivalent to x = x / 3