import random

def flip():
    coin = random.randrange(2)
    if coin == 0:
        print("Heads.")
    else:
        print("Tails.")

for i in range(10):
    flip()
    
