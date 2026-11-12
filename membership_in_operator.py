print("hello" in "hello world") # True
print("hello" not in "hello world") # False
print(3 in [1, 2, 3, 4, 5]) # True
print(6 not in [1, 2, 3, 4, 5]) # True


# validate that the domain is not on the list of blocked domains
domain = "example.com"
blocked_domains = ["blocked.com", "spam.com", "malware.com", "fake.com", "bot.net"]
print(domain not in blocked_domains)



# identity operators, check if two variables point to the same object in memory
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # False
print(a is c)  # True
print(a is not b)  # True

x = ["a", "b", "c" ]
y = ["a", "b", "c" ]
print(x is y)  # False
print(x==y)  # True


x = 5
y = 5   
print(x is y)  # True   
print(x==y)  # True

# validate the email address, it must be filled in and not empty
email = ""
print(email is not None and email != "") # False


email = "user@example.com"
print(email is not None and email != "") # True
