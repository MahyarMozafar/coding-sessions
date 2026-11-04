name = input("Name? ")
born = input("Born? ")
age = 1405 - int(born)
print(f"{name}: {age}")

# make it better: the age in months
months = age * 12
print(f"{months} months")
