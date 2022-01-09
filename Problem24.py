#Problem24

import math

def permutation(numbers, spot):
    """Takes the number of digits and which spot to look for and returns a
    list dictating which factorials to compute"""
    n = numbers
    l = []
    count = 0
    while spot != 1:
        print(spot, math.factorial(n-1))
        if math.factorial(n-1) < spot:
            count = count + 1
            spot = spot - math.factorial(n-1)
        else:
            l.append(count)
            count = 0
            n = n - 1
    if spot == 1:
        l.append(count)

    while len(l) < numbers:
        l.append(0)
    
    return l

def number(l):
    """returns the number based on the returned list from permutation"""
    m = []
    n = ''
    for j in range(0, len(l)):
        m.append(j)
    print(m, l)
    i = 0
    for item in l:
        print(m, item)
        n = n + str(m[item])
        del m[item]
        

    return n

def spot(l):
    """ For shits and giggles, gives the location of a permutation"""
    number = 0
    x = len(l)
    for i in l:
        number = number + (i*(math.factorial(x-1)))
        x = x - 1
    return (number + 1)

def main():
    print(number(permutation(10, 1000000)))

if __name__ == '__main__':
    main()
