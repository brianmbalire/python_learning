print(3>1 and 5<1)
print(3>1 or 5<1)

cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)

email = True
password = False

print(email and password)

# not operator, reverse the truth

print(not 3>1)
print(not email)
print(not password)
print(not not False) # double not operator, returns the original value


# allow access if the user is logged in or they are guest user but they must not be banned

is_logged_in = True
is_guest_user = False
is_banned = False

print(is_logged_in or is_guest_user and not is_banned)


is_logged_in = True
is_guest_user = False
is_banned = True

print((is_logged_in or is_guest_user) and not is_banned)

