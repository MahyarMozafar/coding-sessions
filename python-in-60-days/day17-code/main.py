n = 3
while n > 0:
    print(n)
    n = n - 1
print("Go!")

# break: leave the loop
while True:
    pin = input("PIN? ")
    if pin == "1234":
        break
print("Welcome!")

# continue: skip one round
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
