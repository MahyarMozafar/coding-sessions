# Day 27: dictionaries (the code from the video)
# The wedding gift notebook: who gave how much? (in thousand toman)

gifts = {"Ali": 500, "Sara": 300}   # { } makes a dictionary: every name (key) has a value
print(gifts["Sara"])                # give the name, get its value: 300

# Who gave no gift? in asks: is this name in the notebook?
print("Ali" in gifts)               # True: Ali is in it
print("Reza" in gifts)              # False: Reza gave no gift!
