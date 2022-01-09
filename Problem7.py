#Problem 7

import Problem27

import math

def prime(n):
    """Returns a list of the primes < n"""
    l = [2, 3, 5]
    for i in range(7, n, 2):
        j = 0
        while i % l[j] != 0 and l[j] < math.sqrt(i) + 1:
            j += 1
        if i % l[j] != 0:
            l.append(i)
    return l

def prime_counter(n):
    """Determines the nth prime number"""
    count = 3
    for i in range(3, 1000000, 2):
        j = 3
        while i % j != 0 and j < math.sqrt(i) + 1:
            j += 2
        if i % j != 0:
            count += 1
        if count == n:
            return i
            

def main():
    print(prime_counter(10001))
    print(prime(1000000)[10000])

if __name__ == '__main__':
    main()
