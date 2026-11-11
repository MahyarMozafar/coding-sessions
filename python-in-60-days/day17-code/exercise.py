# Day 17 exercise: ask for the password until it is right.
password = "python"
guess = input("Password? ")
while guess != password:
    print("Wrong, try again")
    guess = input("Password? ")
print("Welcome!")
