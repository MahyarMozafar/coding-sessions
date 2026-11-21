# Day 21: Lists (the code from the video)
# A list is like a queue: the number in [ ] is how many steps from the front, so the first one is 0.

queue = ["Sara", "Reza", "Nima"]
print(queue[0])       # Sara: 0 steps from the front
print(len(queue))     # 3: how many people are in the queue

# The famous mistake: there is no number 3 in a queue of 3 (only 0, 1, 2).
# Don't panic at an error: read its last line.
#   IndexError: list index out of range
# print(queue[3])
print(queue[-1])      # Nima: -1 is the last one

# Real example: a music playlist
songs = ["Hello", "Faded", "Home"]
print("Now:", songs[0])
print("Last:", songs[-1])
