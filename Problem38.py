#Problem38

import Problem32

def pandigital_new(n):
    return Problem32.pandigital('', '', n)

def main():
    l = []
    for i in range(1, 10000):
        n = 9//(len(str(i)))
        value = str(i)
        for j in range(2, n+1):
            value = value + str(j*i)
        if pandigital_new(value) == True:
            l.append(value)

    l.sort()
    print(l)

if __name__ == '__main__':
    main()
