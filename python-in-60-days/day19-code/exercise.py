# Day 19 exercise: remove the hidden spaces from this password with Python.
# It has 3 spaces: one at the start, one in the middle and one at the end.
for ch in " Moha dese ":
    if ch == " ":
        continue
    print(ch, end="")
print()
