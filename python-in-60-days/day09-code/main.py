name = "mahyar"
print(name.upper())
print(name.title())
print(len(name))

# slicing: counting starts at 0
print(name[0])
print(name[0:3])

# the messy name from the start of the video
print("  mAhYaR  ".strip().title())

# a real example
user = "  SARA  "
clean = user.strip()
print(clean.lower())
