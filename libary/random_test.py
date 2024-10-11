'''import random

coin = random.choice(["head", "tails"])
print(coin)
'''
# another way to write the code is 
from random import choice
import random 
coin=choice(["Head","Tail"])# we can change the probability

print(coin)
value=random.randint(1,10)
print(value)
cards=["King","Queen ","Jack"]
random.shuffle(cards)
for card in cards:
    print(card)