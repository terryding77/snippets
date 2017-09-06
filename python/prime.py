import math
        
def is_prime(x):
    for i in range(2, int(math.sqrt(abs(x))) + 1):
        if x % i == 0:
            return False
    return True

def get_prime_set(n):
    prime_set = set()
    prime_mark = [False, False] + [True for _ in range(n - 1)]
    for base in range(2, n + 1):
        if prime_mark[base]: 
            prime_set.add(base)
        for prime in prime_set:
            composite = prime * base
            if composite > n:
                break
            prime_mark[composite] = False 
    return prime_set
