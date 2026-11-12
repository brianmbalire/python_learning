price = "1234,56"
print(price.replace(",","."))

phone = "176/1234/56"
print(phone.replace("/",""))

price = "$1,299.99"
print(price.replace("$", "").replace(",", ""))


phone = "+49(176)123-4567"
print(phone.replace("+", "00").replace("(", "").replace(")", "").replace("-", ""))
