# Day 26: sets and tuples (the code from the video)
# How rond is your phone number? Fewer different digits = more rond.

a = "09121111111"        # line 1: a rond number (as text, in quotes)
b = "09123456789"        # line 2: a normal number
print(len(set(a)))       # set keeps one of each digit (0, 9, 1, 2); len counts them: 4
print(len(set(b)))       # all 10 digits are different: 10

# What nobody can change: a tuple
birthday = (1375, 6, 12) # brackets ( ) make a tuple: a locked list (year, month, day)
birthday[0] = 1385       # try to be 10 years younger -> TypeError: a tuple can't be changed
