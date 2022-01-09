#Problem87

import Problem46 as prime

primes = prime.prime_list(7100)
primes2 = prime.prime_list(370)
primes3 = prime.prime_list(86)
print(len(primes) * len(primes2) * len(primes3))

"""
    a < 7072
    b < 369
    c < 85
"""

def prime_triple(a, b, c):
    return a**2 + b**3 + c**4

def elim_repeats(l):
    l.sort()
    for i in range(0, len(l)):
        if l[i+1] == l[i]:
            l.remove(l[i])
    return l


m = []

for i in primes:
    for j in primes2:
        for k in primes3:
            if prime_triple(i, j, k) < 5*10**7 and prime_triple(i, j, k) not in m:
                m.append(prime_triple(i, j, k))
                


print(len(m))
print(len(elim_repeats(m)))


