# Factorial - Recursive function using memorization
import time

# This dictionary store the data already known
# This is for optimize time for execution
factorial_cache = {}
def get_factorial(n):
    # Check if you have already store that number
    if n in factorial_cache:
        return factorial_cache[n]
    # Factorial algorithm
    if (n >= 1):
        value = get_factorial(n-1) * n
    else:
        value = 1
    # Store the result in our dictionary
    factorial_cache[n] = value
    return value

def get_factorial_2(n):
    # Factorial algorithm
    value = 1
    for i in range(n):
        i += 1
        value *= i
    return value

print "\n  "
t0 = time.time()
for n in range(1, 1000):
    #print "  ", n, ":", get_factorial(n)
    #print "  ", n, ":", get_factorial_2(n)
    get_factorial_2(n)
t1 = time.time()
print "\n Time required: ", t1-t0
