# Day 20: Mini project: a times-table quiz that catches a wrong answer (the code from the video)

# one question: Python does not remember the answer, it works out 7 * 8 by itself
ans = int(input("7x8? "))
if ans == 7 * 8:
    print("Correct!")      # one Tab (4 spaces) in: this line belongs to the if
else:
    print("Caught you!")   # this line belongs to the else

# the whole 7 table: the same idea inside a for loop
for i in range(1, 4):
    ans = int(input(f"7x{i}? "))
    if ans != 7 * i:       # != means "not equal"
        print("Caught you!")
