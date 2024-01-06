import random

# coin = random.choice(["heads", "talis"])
# print(coin)

# from random import choice

# coin = choice(["heads", "talis"])
# print(coin)

# number = random.randint(1, 10)
# print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)