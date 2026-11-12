#whitespace cleaning

text = " Engineering".lstrip()
text = "Engineering ".rstrip()
text = " Engineering ".strip()


print(text)


search = "Email".lower().strip()
data = "eMAil".lower().strip()

print(search == data)


messy = "968-Maria, ( D@ta Engineer );; 27y"

# 1. Remove the ID and hyphen
# 2. Extract and clean the name
# 3. Remove unwanted symbols and clean the role
# 4. Remove the y from the age
# 5. Format the final summary

print(messy.strip().lower())