import random


def prime_test(N, k):
    # This is the main function connected to the Test button. You don't need to touch it.
    return run_fermat(N,k), run_miller_rabin(N,k)
 
def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, y // 2, N)   
    if y % 2 == 0:
        return (z * z) % N
    else:
        return (x * z * z) % N

def fprobability(k):
    # You will need to implement this function and change the return value.   
    return 0.0


def mprobability(k):
    # You will need to implement this function and change the return value.   
    return 0.0

def run_fermat(N,k): 
    if N <= 1:
        return 'composite'
    if N == 2 or N == 3:
        return 'prime'

    for _ in range(k):
        a = random.randint(2, N - 2)
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'
    
    return 'prime'

def run_miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    return 'composite'
