import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0, 1], 10000, p=[1-p1, p1])
    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    amount = 0
    for i in range(0, len(seq)-4):
        if seq[i] == 1 and seq[i+1] == 1 and seq[i+2] == 1 and seq[i+3] == 1 and seq[i+4] == 1:
            amount += 1
    return amount

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
