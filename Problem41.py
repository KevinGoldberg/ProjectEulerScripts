#Problem41

import Problem46 as prime

import Problem49 as perm

"""
primes = prime.prime_list(10000000)

print("done")

potentials = perm.permutations(1234567)

for value in potentials:
    if value in primes:
        print(value)
"""

def rabin_miller(n):
    p = [2, 3, 5, 7, 11, 13, 17, 19]
    for prime in p:
        if n % prime == 0:
            return False
    if n < 2047:
        l = [2]
    elif n < 1373653:
        l = [2, 3]
    elif n < 9080191:
        l = [31, 73]
    elif n < 25326001:
        l = [2, 3, 5]
    elif n < 4759123141:
        l = [2, 7, 61]
    elif n < 1122004669633:
        l = [2, 13, 23, 1662803]

    m = n-1
    r = 0
    while m % 2 == 0:
        r += 1
        m = m/2
    d = m

    for a in l:
        x = a**d % n
        if x == 1:
            pass
        else:
            count = 0
            while x != n-1 or r > count:
                count += 1
                x = x**2 % n
                if x == 1 % n:
                    return False
        if x != n-1:
            return False

    return True

for i in range(2, 100):
    if rabin_miller(i) == True:
        print(i)
