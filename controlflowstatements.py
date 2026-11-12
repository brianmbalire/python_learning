# boolean values
print(True)
print(False)

print(bool(1)) # True
print(bool(0)) # False
print(bool(-1)) # True
print(bool("")) # False
print(bool(None)) # False

email = "brian@example.com"
phone = "1234567890"
username = "brian123"

# allows registration if any of the fields are filled

print(any([email, phone, username])) # True if any of the values are True

# allows registration if all of the fields are filled
print(all([email, phone, username])) # True if all of the values are True

print("Hello World".startswith("Hello")) # True
print("Hello World".endswith("World")) # True   
