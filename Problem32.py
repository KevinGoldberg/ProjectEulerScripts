#Problem 32

def pandigital(x, y, z):
    a = str(x)
    b = str(y)
    c = str(z)
    value = a + b + c
    i = 1
    if len(value) != 9:
        return False
    while i < 10:
        if str(i) not in value:
            return False
        else:
            i += 1
    if i == 10:
        return True

def main():
    l = []
    for i in range(2, 999):
        for j in range(11, 9999):
            if pandigital(i, j, i*j) == True and i*j not in l:
                l.append(i*j)

    print(l)
    print(sum(l))

if __name__ == '__main__':
    main()
