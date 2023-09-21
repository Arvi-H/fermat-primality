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
    return (1 - 1/2**k) 

def mprobability(k):
    return (1 - 1/4**k) 

def run_fermat(N,k): 
    # Base cases for n < 3
    if N <= 1: 
        return 'composite'
    if N == 2 or N == 3: 
        return 'prime'

    # Even integers can't be prime
    if N % 2 == 0:
        return 'composite'

    # Fermat algorithm
    for _ in range(k): # do the test k times
        a = random.randint(2, N - 2) 
        if mod_exp(a, N-1, N) != 1:
            return 'composite'
    
    return 'prime'

def run_miller_rabin(N,k):
    # Base cases for n < 3
    if N <= 1: 
        return 'composite'
    if N == 2 or N == 3: 
        return 'prime'

    # Even integers can't be prime
    if N % 2 == 0:
        return 'composite'

    # Miller-Rabin Algorithm   
    r, d = 0, N - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, N - 2)
        x = pow(a, d, N)
        if x == 1 or x == N - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, N)
            if x == N - 1:
                break
        else:
            return "composite"
    return "prime"