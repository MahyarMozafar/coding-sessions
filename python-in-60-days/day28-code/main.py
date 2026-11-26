# Day 28: loop over a dictionary + sum (the code from the video)
# How many hours a day on your phone, and how many days a year is that?

apps = {"Insta": 4, "YouTube": 2}   # app name (key): hours a day (value)
for name in apps:                   # for gives the keys (the app names) one by one: name = "Insta", then "YouTube"
    print(name, apps[name])         # apps[name] = the hours of that name (like gifts["Sara"] on Day 27)

# The scary answer: how many days a year?
h = sum(apps.values())              # values() gives only the hours; sum adds them up: 6
print(h * 365 / 24)                 # 6 hours x 365 days / 24 hours = 91.25 days a year!
