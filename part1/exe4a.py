import random

def main():
    prob = random.random()
    favourite = ['dogs', 'cats', 'bats']  # change this
    if prob > 0.2:
        n = 0
    elif 0.1 < prob <= 0.2:
        n = 1
    else:
        n = 2
    print("I love " + favourite[n]) 



main()
