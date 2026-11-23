# Day 22: Add and remove in a list (the code from the video)
# The bakery queue, part 2 (part 1 is Day 21): Reza leaves, Ali comes.

queue = ["Sara", "Reza", "Nima"]   # the same queue as yesterday
queue.remove("Reza")               # remove = delete; Reza leaves the queue
queue.append("Ali")                # append = add; Ali goes to the END of the queue
print(queue)                       # ['Sara', 'Nima', 'Ali']
# The dot . means: tell THIS list to do something.

# The famous mistake: a small r.
# For Python, "Reza" and "reza" are not the same, so this gives an error:
#   ValueError: list.remove(x): x not in list
# Don't panic at an error: read its last line. "x not in list" = it is not in the list.
# queue.remove("reza")

# Real example: the family group chat
family = ["Mom", "Dad", "Sara"]
family.append("Uncle")    # Uncle joined
family.remove("Sara")     # Sara left the group
print(family)             # ['Mom', 'Dad', 'Uncle']
