# EJ26_P2  Prime number
import time # to messure time execution
import math

def is_prime_v1(n):
    """Return "True" if "n" is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime
    for d in range(2, n):
        if n % d == 0:
            return False #Not prime
    return True # If any of the conditions worked, "n" is prime

def is_prime_v2(n):
    """Return "True" if "n" is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + int(max_divisor) ):
        if n % d == 0:
            return False #Not prime
    return True # If any of the conditions worked, "n" is prime
# ======= Test function 1 =======
#for n in range(1, 21):
#    print n, is_prime_v1(n)

# ======= Test function 1 =======
#t0 = time.time()
#for n in range(1, 100000):
#    is_prime_v1(n)
#t1 = time.time()
#print "Time required: ", t1-t0

# ======= Test function 2 =======
#for n in range(1, 21):
#    print n, is_prime_v2(n)

# ======= Test function 2 =======
t0 = time.time()
for n in range(1, 100000):
    is_prime_v2(n)
t1 = time.time()
print "Time required: ", t1-t0
