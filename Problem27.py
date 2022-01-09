#Problem27

import Problem7

def prime_list(end):
    """Faster way to produce a list of the primes up to end"""
    l = [2]
    for i in range(3, end):
        x = 0
        remain = 1
        while remain != 0 and x < len(l):
            remain = i % l[x]
            x += 1
        if remain != 0:
            l.append(i)
            
    return l

def quadratic(a, b, primes):
    n = 1
    p = n**2 + n*a + b
    while p in primes:
        n = n + 1
        p = n**2 + n*a + b
        
    return n

def main():
    primes = prime_list(100000)
    primes.remove(2)
    
    m = []
    for items in primes:
        m.append(-(items))

    primes.extend(m)

    primes.sort()
    #primes is now an ordered list of negative and positive primes except 2

    max = 0
    for i in range(-999, 999, 2):
        for j in range(-999, 999, 2):
            if quadratic(i, j, primes) > max:
                max = quadratic(i, j, primes)
                product = i * j
                print(i, j)
    print(product)

if __name__ == '__main__':
    main()
