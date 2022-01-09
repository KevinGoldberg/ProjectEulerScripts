#Problem 58

import Problem46 as prime
import math

def diagonals(n):
    """ Returns a list of all the numbers in the diagonals of the spiral
    with sidelength (n)"""
    l = [1]
    for i in range(1, n//2+1):
        l.append((2*i+1)**2)
        l.append((2*i+1)**2 - 2*i)
        l.append((2*i+1)**2 - 4*i)
        l.append((2*i+1)**2 - 6*i)
    l.sort()
    return l

#figure out how to put this to work
def update_diagonals(l):
    x = (len(l) + 1)/2 + 2
    l.append(x**2 - 6*i)
    l.append(x**2 - 4*i)
    l.append(x**2 - 2*i)
    l.append(x**2)

    return l

def four_new_numbers(n):
    """Returns a list of the four diagonal values new to a spiral of length n"""
    l = []
    x = int((n-1)/2)
    l.append(n**2 - 6*x)
    l.append(n**2 - 4*x)
    l.append(n**2 - 2*x)
    l.append(n**2)
    
    return l

def check_four(l):
    count = 0
    for number in l:
        if is_prime(number) == True:
            count += 1
    return count
    

def is_prime(n):
    if n%2 == 1:
        prime = True
    else:
        return False
    for i in range(3, int(math.sqrt(n)//1), 2):
        if n%i == 0:
            prime = False
    return prime
    

def percent(n):
    """Input is the list of the diagonals, returns the %of primes represented"""
    count = 0
    for value in diagonals(n):
        #using is_prime instead of prime_list is much much faster
        if is_prime(value) == True:
            count += 1
    return (count/(2*n - 1))*100


def fibonacci(n):
    l = [1, 1, 2]
    while l[-1] < n:
        l.append(l[-2] + l[-1])
    return l

def update_fib(l):
    """Updates a list from fibonacci by adding one entry"""
    l.append(l[-2] + l[-1])
    return l

def main():
    #brute force ugh
    """n = 7
    while percent(n) >= 10:
        n += 2
        print(n, percent(n))
    print("The answer is ", n)
    
    #initial values
    n = 7
    primes = 8
    diags = 13

    #optimized big-0 run time for brute force
    while (primes/diags) * 100 >= 10:
        n += 2
        diags += 4
        primes += check_four(four_new_numbers(n))
        #print(n, primes/diags)
    print("The answer is ", primes/diags)

    l = fibonacci(10)
    while (l[-2]/l[-1])*100 >= 10:
        update_fib(l)
        print(l)
        #print((l[-2]/l[-1])*100)
    print(l[-2], l[-1], (l[-1]+1)/2)
    """
    #loljk it's definitely not fibonacci
    #the ratio is ~consistent (golden ratio)

    #print(math.sqrt(14), math.sqrt(14)//1, int(math.sqrt(14)//1) + 1)
    #print('\n')
    #print(is_prime(65))
    #primeCount, diagonals = 5, 4
    while (100*primeCount)/(4*diagonals -3) >= 10:
        #print(diagonals, primeCount, (100*primeCount)/(4*diagonals + 1))
        #print((2*diagonals-1)**2 - (diagonals-1)*2, (2*diagonals-1)**2 - 2*(diagonals-1)*2, (2*diagonals-1)**2 - 3*(diagonals-1)*2)
        if is_prime((2*diagonals-1)**2 - (diagonals-1)*2) == True:
            primeCount += 1
        if is_prime((2*diagonals-1)**2 - 2*(diagonals-1)*2) == True:
            primeCount += 1
        if is_prime((2*diagonals-1)**2 - 3*(diagonals-1)*2) == True:
            primeCount += 1
        diagonals += 1
    print(diagonals, primeCount)
    print("The answer is", 2*diagonals -1)
        

if __name__ == '__main__':
    main()
    
