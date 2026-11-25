# Day 24: Loop over a list and in (the code from the video)
# The bakery queue, part 4 (parts 1-3 are Day 21, 22 and 23): Reza says he was always in the queue.

queue = ["Sara", "Nima", "Ali"]   # our queue (Reza left it on Day 22)
print("Reza" in queue)            # False: "is Reza in the queue?" -> no
print("Ali" in queue)             # True: Ali is in the queue

# The baker calls them one by one
queue = ["Sara", "Nima", "Ali"]
for name in queue:                # for each person in the queue; name = the name of this round
    print("Next:", name)          # pushed in (4 spaces) = inside the loop, so it runs every round

# Real example: at the party door
guests = ["Mom", "Dad", "Uncle"]
name = input("Name? ")            # asks for your name (type Uncle)
if name in guests:                # is your name in the list?
    print("Welcome!")
