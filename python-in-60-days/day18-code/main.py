# Day 18: Nested loops (the code from the video)

# a small cinema: 2 rows, 3 seats in each row
for row in range(1, 3):
    for seat in range(1, 4):
        print(row, seat)

# the real cinema: 10 rows, 20 seats = 200 seats
# (it prints 200 lines: 1 1, 1 2, ... 10 20)
for row in range(1, 11):
    for seat in range(1, 21):
        print(row, seat)
