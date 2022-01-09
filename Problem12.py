#Problem 12

import math

import Problem46 as prime

def triangular(x):
    """Determines if a number is a triangular number"""
    if math.sqrt(1 + 8*x) % 1 == 0:
        return True
    else:
        return False

def divisors(n):
    if n % 2 == 0:
        n = n/2
    d = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    d = d * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        d = d * (count + 1)
        p += 2
    return d

def total(limit):
    #the divisors x = (n*(n+1))/2 is divisors(n) * divisors(n+1)

    n = 1
    a = divisors(n)
    b = divisors(n+1)
    x = a*b
    while x < limit:
        n += 1
        a = b
        b = divisors(n+1)
        x = a*b
    return int(n*(n+1)/2)

def products(n):
    count = 2
    for i in range(2, n//2 + 1):
        if n % i == 0:
            count += 1
    return count

def main():
    print(total(500))

if __name__ == '__main__':
    main()
