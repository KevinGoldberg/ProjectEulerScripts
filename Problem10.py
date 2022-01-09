#Problem 10
import math

def add_primes(end):
    sum = 0
    for i in range(1, end, 2):
        j = 3
        while 3 <= j < math.sqrt(i) + 1:
            if i % j != 0:
                j = j + 1
            else:
                j = 0
        if j >= (math.sqrt(i) + 1):
            sum = sum + i
            print(i)
    #this sum includes 1, but not 2
    sum = sum + 1
    return sum


def main():
    print(add_primes(200))

if __name__ == '__main__':
    main()
