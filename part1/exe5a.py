import random
import math


def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing
    # exp((S_new - S_old) / T)
    
    prob = 0.0
    if S_new > S_old:
        prob = 1.0
    else:
        prob = math.exp((S_new - S_old) / T)
    return prob


# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)
