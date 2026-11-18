n = 3
while n > 0:
    print(n)
    n = n - 1
print("Go!")

# break: leave the loop (the phone lock)
while True:
    pin = input("PIN? ")
    if pin == "1234":
        break
print("Welcome!")
