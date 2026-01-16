import math

def prime_factors(n):
    factors = []

    # Step 1: divide by 2 as long as possible
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Step 2: n is now odd, test odd divisors up to sqrt(n)
    i = 3
    while i <= math.sqrt(n):
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # Step 3: if n > 2, it is prime
    if n > 2:
        factors.append(n)

    return factors

