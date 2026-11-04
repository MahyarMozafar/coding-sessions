name = input("Name? ")
print(f"Hi {name}!")

# careful: input() always gives text, so this line would be an error:
# age = input("Age? ")
# print(age + 1)   # TypeError (fixed on Day 8 with int())

# a real example
food = input("Food? ")
print(f"Got {food}!")
