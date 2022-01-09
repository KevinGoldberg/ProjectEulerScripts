#Problem16

def digits(n):
    count = 0
    while len(str(n)) > 1:
        place = len(str(n)) - 1
        count = count + n//(10**place)
        n = n - (n//(10**place))*(10**place)
    count = count + n % 10

    return count

def main():
    print(digits(2**1000))

if __name__ == '__main__':
    main()
