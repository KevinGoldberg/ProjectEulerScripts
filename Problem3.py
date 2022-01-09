#Problem 3

import math



def products(x):
    """Produces the products of a given integer"""
    l = []
    for i in range(1, int(x/2) + 1):
        if x % i == 0:
            m = []
            m.append(products(i))
            l.append(i)
    return l

def main():
    y = 600851475143
    products(y)


if __name__ == '__main__':
    main()
