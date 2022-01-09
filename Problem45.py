#Problem45

import math

def triangular_list(n):
    l = []
    for i in range(1, n+1):
        l.append(int(i*(i+1)/2))
    return l

def is_pentagonal(p):
    if (math.sqrt(1 + 24*p) % 6) - 5 == 0:
        return True
    else:
        return False

def is_hexagonal(h):
    if (math.sqrt(1 + 8*h) % 4) - 3 == 0:
        return True
    else:
        return False

def main():
    numbers = triangular_list(1000000)
    for number in numbers:
        if (is_pentagonal(number) == True) and (is_hexagonal(number)) == True:
            print(number)

if __name__ == '__main__':
    main()
