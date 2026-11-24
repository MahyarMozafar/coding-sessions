# Day 23: Sort and pop (the code from the video)
# The bakery queue, part 3 (part 1 is Day 21, part 2 is Day 22): a fight over the turn.

tickets = [3, 1, 2]     # the ticket numbers, in the order the people stand
tickets.sort()          # sort = put in order, small to big
print(tickets)          # [1, 2, 3]

# The baker calls: "Next!"
tickets = [1, 2, 3]
served = tickets.pop(0) # pop = take out; 0 = the first one in the queue
print(served)           # 1  (pop gives back what it took, so we keep it in served)
print(tickets)          # [2, 3]
# remove needs the NAME (the value); pop needs the PLACE number (the index).

# Real example: the contacts on your phone
contacts = ["Reza", "Ali", "Sara"]
contacts.sort()         # names are sorted from A to Z
print(contacts)         # ['Ali', 'Reza', 'Sara']
