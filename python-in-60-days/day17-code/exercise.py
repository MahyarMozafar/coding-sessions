# Day 17 exercise: the phone lock from the video, but it says "Wrong!" after a wrong PIN.
while True:
    pin = input("PIN? ")
    if pin == "1234":
        break
    print("Wrong!")
print("Welcome!")
