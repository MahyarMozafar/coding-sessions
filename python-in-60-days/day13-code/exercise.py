# Day 13 exercise: turn a score into a letter.
score = int(input("Score? "))
if score >= 18:
    print("A")
elif score >= 15:
    print("B")
elif score >= 12:
    print("C")
elif score >= 10:
    print("D")
else:
    print("F")
