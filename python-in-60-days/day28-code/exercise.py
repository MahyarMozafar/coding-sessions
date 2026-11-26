# Day 28 exercise: put your own phone hours in a dictionary,
# then find how many days a year that is. (Change the numbers to yours!)

apps = {"Instagram": 5, "Telegram": 2, "YouTube": 3, "Games": 2}
h = sum(apps.values())
print(h * 365 / 24)
