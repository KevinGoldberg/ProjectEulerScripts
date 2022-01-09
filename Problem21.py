#Problem21

import Problem3

def factor_add(n):
    l = Problem3.products(n)
    sum = 0
    for x in l:
        sum = sum + x
    return sum

def amicable(x, y):
    if factor_add(x) == y and factor_add(y) == x and x != y:
        return True
    else:
        return False

def main():
    l = []
    for i in range(0, 10001):
        if amicable(i, factor_add(i)) == True:
            print(i)
            l.append(i)
    print(sum(l))

if __name__ == '__main__':
    main()
