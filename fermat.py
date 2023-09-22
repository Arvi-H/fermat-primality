import random

def prime_test(N, k):
    # This is the main function connected to the Test button. You don't need to touch it.
    return run_fermat(N,k), run_miller_rabin(N,k)
 
# Time Complexity: O(n^3) | Space Complexity: O(log(y)) 
def mod_exp(x, y, N):
    if y == 0: # O(1)
        return 1
    z = mod_exp(x, y // 2, N)  # O(n^2)
    if y % 2 == 0:
        return (z * z) % N # O(n^2)
    else:
        return (x * z * z) % N # O(n^2)

def fprobability(k):
    return (1 - 1/2**k) 
 
def mprobability(k):
    return (1 - 1/4**k) 

# Time Complexity: O(N^3) | Space Complexity: O(log(y)) 
def run_fermat(N,k): 
    # Base cases for N < 3 | O(1)
    if N <= 1: 
        return 'composite'
    if N == 2 or N == 3: 
        return 'prime'

    # Even numbers | O(1)
    if N % 2 == 0:
        return 'composite'

    # Fermat algorithm
    for _ in range(k): # do the test k times | O(k)
        a = random.randint(2, N - 2) 
        if mod_exp(a, N-1, N) != 1: # O(N^3)
            return 'composite'
    
    return 'prime'

# Time Complexity: O(N^4) | Space Complexity: O(log(N))
def run_miller_rabin(N,k):
    # Base cases for n < 3 | O(1)
    if N <= 1: 
        return 'composite'
    if N == 2 or N == 3: 
        return 'prime'

    # Even numbers | O(1)
    if N % 2 == 0:
        return 'composite'

    # Miller-Rabin Algorithm   
    # exponent = the largest power of 2 that divides N - 1
    exponent, d = 0, N - 1
    while d % 2 == 0:  # O(n) # iterate and find that exponent
        exponent += 1 
        d //= 2

    for _ in range(k): # O(k)
        a = random.randint(2, N - 2)
        x = mod_exp(a, d, N)   # O(N^3)
        if x == 1 or x == N - 1:
            continue
        for _ in range(exponent - 1):  # O(exponent)
            x = mod_exp(x, 2, N) # O(N^3)
            if x == N - 1:
                break
        else:
            return "composite"
    return "prime"