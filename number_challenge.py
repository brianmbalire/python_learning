#check if a user's name is not empty and age is a number greater than or equal to 18
name = "John"
age = 25
print(name != "" and isinstance(age, int) and age >= 18)  # True


name = "Brian"
age = 25

if name != "" and age >= 18:
    print("Valid user")
else:
    print("Invalid user")


    
#chcek if password is at least 8 characters long and contains at least one uppercase letter, one lowercase letter, and one number
password = "Password123"
if len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
    print("Valid password")

password = "Brian123"

if (len(password) >= 8
    and any(char.isupper() for char in password)
    and any(char.islower() for char in password)
    and any(char.isdigit() for char in password)):

    print("Strong password")
else:
    print("Weak password")




#check if a user's email address is valid, it must contain an "@" symbol and end with a valid domain name (e.g. .com, .org, .net)
email = "john@example.com"
if "@" in email and any(email.endswith(domain) for domain in [".com", ".org", ".net"]):
    print("Valid email")


email = "brian@gmail.com"

if ("@" in email
    and email.endswith((".com", ".org", ".net"))):

    print("Valid email")
else:
    print("Invalid email")




#check if a username is a string, is not none and is longer than 5 characters
username = "john_doe"
if isinstance(username, str) and username is not None and len(username) > 5:
    print("Valid username")


username = "BrianMbalire"

if (username is not None
    and isinstance(username, str)
    and len(username) > 5):

    print("Valid username")
else:
    print("Invalid username")

#check if the user is either an admin or a moderator, and either theyre not banned or theyve veirfied their email address

role = "admin"
is_banned = True
email_verified = True

if ((role == "admin" or role == "moderator")
    and (not is_banned or email_verified)):

    print("Access granted")
else:
    print("Access denied")


