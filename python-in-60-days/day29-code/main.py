# Day 29: a list of dictionaries (the code from the video)
# Your budget is 150 million toman: which phone on Divar can you buy?

ad1 = {"name": "A57", "price": 160}     # one ad = one dictionary (a card): name + price (million toman)
ad2 = {"name": "Redmi", "price": 140}
ads = [ad1, ad2]                        # the whole Divar page = a list of cards
print(len(ads))                         # 2 ads in the list

# Python searches for you
for ad in ads:                          # for brings the ads one by one
    if ad["price"] < 150:               # is its price under 150?
        print(ad["name"])               # yes: print its name -> Redmi
