import random

secret = random.randint(1, 100)
guess = input("Even or odd? ")

if secret % 2 == 0:
    answer = "even"
else:
    answer = "odd"

print(f"My number was {secret}")
if guess.lower() == answer:
    print("You win!")
else:
    print("You lose!")
