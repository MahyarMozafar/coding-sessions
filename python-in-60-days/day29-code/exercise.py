# Day 29 exercise: add one more ad to the list, then run the same search.

ad1 = {"name": "A57", "price": 160}
ad2 = {"name": "Redmi", "price": 140}
ad3 = {"name": "Poco", "price": 95}     # the new ad (use any phone and price you like)
ads = [ad1, ad2, ad3]

for ad in ads:
    if ad["price"] < 150:
        print(ad["name"])
