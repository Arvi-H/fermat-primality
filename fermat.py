import random

def prime_test(N, k):
    # This is the main function connected to the Test button. You don't need to touch it.
    return run_fermat(N,k), run_miller_rabin(N,k)
 
# Time Complexity: O(log(y)) | Space Complexity: O(log(y)) 
def mod_exp(x, y, N):
    if y == 0: # O(1)
        return 1
    z = mod_exp(x, y // 2, N)  # O(log(y))
    if y % 2 == 0:
        return (z * z) % N
    else:
        return (x * z * z) % N

# Time Complexity: O(1) | Space Complexity: O(1) 
def fprobability(k):
    return (1 - 1/2**k) 

# Time Complexity: O(1) | Space Complexity: O(1) 
def mprobability(k):
    return (1 - 1/4**k) 

# Time Complexity: O(klog(N)) | Space Complexity: O(1) 
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
        if mod_exp(a, N-1, N) != 1: # O(log N)
            return 'composite'
    
    return 'prime'

# Time Complexity: O(klog(N)) | Space Complexity: O(klog(N))
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
    r, d = 0, N - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k): # O(k)
        a = random.randint(2, N - 2)
        x = mod_exp(a, d, N)  # O(log N)
        if x == 1 or x == N - 1:
            continue
        for _ in range(r - 1):  # O(r)
            x = mod_exp(x, 2, N)  # O(log N)
            if x == N - 1:
                break
        else:
            return "composite"
    return "prime"