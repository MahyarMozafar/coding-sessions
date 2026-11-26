# Day 25: zip and enumerate (the code from the video)
# The dinner bill: three friends, one bill. Who pays how much?

names = ["Ali", "Sara", "Nima"]   # line 1: the friends
pay = [120, 80, 95]               # line 2: what each one ate, in the same order (thousand toman)
for n, p in zip(names, pay):      # zip pairs the two lists: first with first, second with second
    print(n, p)                   # each round: n = the name, p = the money

# The bill gets numbers
food = ["Pizza", "Salad", "Kebab"]
for i, f in enumerate(food):      # enumerate gives each item a number: i = the number, f = the food
    print(i + 1, f)               # Python counts from 0, so + 1 makes the bill start at 1
