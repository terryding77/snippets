import math
        
def is_prime(x):
    for i in range(2, int(math.sqrt(abs(x))) + 1):
        if x % i == 0:
            return False
    return True

def get_prime_list(n):
    prime_list = []
    prime_mark = [False, False] + [True for _ in range(n - 1)]
    for base in range(2, n + 1):
        if prime_mark[base]: 
            prime_list.append(base)
        for prime in prime_list:
            composite = prime * base
            if composite > n:
                break
            prime_mark[composite] = False 
    return prime_list
