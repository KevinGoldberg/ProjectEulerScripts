#Problem34

import math

def digit_factorial(x):
    value = str(x)
    sum = 0
    for digit in value:
        sum = sum + math.factorial(int(digit))
    return (sum == x)

def main():
    for i in range(0, 2000000):
        if digit_factorial(i) == True:
            print(i)
    #The only numbers like this are 145 and 40585

if __name__ == '__main__':
    main()
