# Day 14 exercise: ticket price by age.
age = int(input("Age? "))
price = 100000
if age < 12 or age >= 65:
    price = price / 2
print(price)
