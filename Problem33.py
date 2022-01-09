#Problem33

def reduce(m, n):
    a = str(m)
    b = str(n)
    if a[1] == b[0]:
        x = int(a[0])
        y = int(b[1])
        if x != 0 and y != 0:
            return (m/n == x/y)
        else:
            return False
    elif a[0] == b[1]:
        x = int(a[1])
        y = int(b[0])
        if x != 0 and y != 0:
            return (m/n == x/y)
        else:
            return False
    else:
        return False

def main():
    for i in range(11, 100):
        for j in range(11, 100):
            if i < j:
                potential = reduce(i, j)
                if potential != False:
                    print(i, j)

if __name__ == '__main__':
    main()
