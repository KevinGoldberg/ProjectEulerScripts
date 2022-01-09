#Problem26

def repeating(x):
    l = []
    a = 1
    repeat = 'n'
    while repeat == 'n':
        while a / x < 1:
            l.append(0)
            a = a * 10
        for i in range(0, len(l)):
            if l[i] == int(a % x):
                repeat = 'y'
        l.append(a % x)
        a = 10*(a % x)
        
    return len(l)

def main():
    max = 0
    location = 0
    for i in range(3, 1000, 2):
        print(i)
        remainders = repeating(i)
        if remainders > max:
            max = remainders
            location = i
            print(max, location)

    print(location, max)

if __name__ == '__main__':
    main()
