def flip(n):
    odds = 1.0         # start with 50% chance of the magic coin, which is the same as odds = 1:1
    for i in range(n):
        odds = odds * 0.5
    r = 1 / odds
    print(r)

n = 1
flip(n)
