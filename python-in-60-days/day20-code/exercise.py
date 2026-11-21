# Day 20 exercise: at the end, say how many answers were right (keep a score).
score = 0
for i in range(1, 4):
    ans = int(input(f"7x{i}? "))
    if ans == 7 * i:
        print("Correct!")
        score = score + 1     # one more right answer
    else:
        print("Caught you!")
print("Right answers:", score)
