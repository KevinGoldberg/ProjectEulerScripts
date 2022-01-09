#Problem 69

"""
n divided by the totient function is highest when there are a maximum of
distinct prime divisors. Thus, calculate the largest composite number
consisting of distinct primes.
"""

import Problem46 as prime

primes = prime.prime_list(1000)

n = 1
x = 0

while n < 1000000:
    n = n * primes[x]
    x += 1

n = n/(primes[x-1])

print(n)
    
