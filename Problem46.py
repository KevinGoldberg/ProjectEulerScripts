#Problem46

import math

def prime_list(n):
    l = [2, 3, 5]
    for i in range(7, n):
        j = 0
        while i % l[j] != 0 and l[j] <= math.sqrt(i) + 1:
            j += 1
        if l[j] > math.sqrt(i) + 1:
            l.append(i)

    return l

def not_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

def goldbach(x):
    a = 1
    primes = prime_list(x)
    while (x - 2*(a**2)) not in primes and a**2 < x:
        a += 1
    if a**2 >= x:
        return False

def main():
    for i in range(1, 10000, 2):
        if goldbach(i) == False and not_prime(i) == True:
            print(i)

if __name__ == '__main__':
    main()
