#Problem36

import Problem4

def binary(n):
    """takes a number and returns the integer binary (base 2) value"""
    x = 0
    while 2**x <= (n - 2**x):
        x += 1

    value = ''
    while x >= 0:
        if 2**x <= n:
            n = n - 2**x
            value = value + '1'
        else:
            value = value + '0'
        x = x - 1

    return int(value)

def hexadecimal(n):
    """ it goes from 1-f"""
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    x = 0
    while 16**x <= n:
        x += 1

    value = ''
    while x >= 0:
        if 16**x <= n:
            value += str(l[n//(16**x)])
            n = n % (16**x)
        else:
            value += '0'
        x = x - 1
    return value

def main():
    l = []
    for i in range(0, 1000000):
        if Problem4.palindrome(i) == True:
            if Problem4.palindrome(binary(i)) == True:
                l.append(i)
    print(sum(l))

if __name__ == '__main__':
    main()
