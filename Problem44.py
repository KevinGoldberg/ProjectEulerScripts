#Problem44

import math

def pentagonal(n):
    return (3*n - 1) * n/2

def is_pentagonal(p):
    if (math.sqrt(1 + 24*p) % 6) - 5 == 0:
        return True
    else:
        return False

def pentagonal_list(n):
    l = []
    for i in range(1, n + 1):
        l.append(int(pentagonal(i)))
    return l

def main():
    for i in range(1, 10000):
        for j in range(i, 10000):
            if is_pentagonal(pentagonal(j) - pentagonal(i)) == True:
                if is_pentagonal(pentagonal(i) + pentagonal(j)) == True:
                    print(i, j)
    
if __name__ == '__main__':
    main()
