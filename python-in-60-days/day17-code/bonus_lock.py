# Day 17 bonus: a phone lock that feels real.
# - What you type stays hidden, like on a real phone.
# - 3 wrong tries: the phone locks for 10 seconds, then you can try again.

import getpass
import time

pin = "1234"
tries = 0

while True:
    guess = getpass.getpass("PIN? ")
    if guess == pin:
        print("Welcome! The phone is open.")
        break

    tries = tries + 1
    if tries < 3:
        print("Wrong! Tries left:", 3 - tries)
    else:
        print("Locked! Wait 10 seconds...")
        for second in range(10, 0, -1):
            print(second)
            time.sleep(1)
        tries = 0
