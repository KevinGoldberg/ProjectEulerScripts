#Problem47

import math

import Problem46

def unduplicated_factors(n):
    """ Returns a list of unduplicated prime factors of n"""
    primes = Problem46.prime_list(n)
    l = []
    for i in range(2, int(n/2) + 1):
        if n % i == 0 and i in primes:
            l.append(i)
    return l

def factor_reducer(n):
    x = 2
    l = []
    while n % x != 0:
        x += 1
    if x == n:
        l.append(x)
        return l
    else:
        l.append(x)
        return l + factor_reducer(n/x)

def factor_reducer_p(n):
    primes = Problem46.prime_list(n)
    x = 0
    l = []
    while n % primes[x] != 0:
        x += 1
    if x > len(primes):
        l.append(primes[x])
        return l
    else:
        l.append(primes[x])
        return l + factor_reducer(n/primes[x])

def unreplicate(l):
    m = []
    for value in l:
        if value not in m:
            m.append(value)
    return m

def main():
    print(factor_reducer_p(240))
    print(unreplicate(factor_reducer_p(240)))

    for i in range(3, 1000000):
        if len(unreplicate(factor_reducer_p(i))) == 4:
            if len(unreplicate(factor_reducer_p(i+1))) == 4:
                if len(unreplicate(factor_reducer_p(i+2))) == 4:
                    if len(unreplicate(factor_reducer_p(i+3))) == 4:
                        print(i)
    
    """for i in range(1, 100000):
        if len(unduplicated_factors(i)) == 4:
            if len(unduplicated_factors(i+1)) == 4:
                if len(unduplicated_factors(i+2)) == 4:
                    if len(unduplicated_factors(i+3)) == 4:
                        print(i)
    """

if __name__ == '__main__':
    main()
