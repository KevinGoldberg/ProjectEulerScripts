#Problem52

def remainders(n):
    l = []
    for i in range(1, 7):
        l.append(str(n * i % 10))
    return l

def check(n, modten_list):
    value = str(n)
    x = 0
    while x < len(modten_list):
        if modten_list[x] not in value:
            return False
        else:
            x += 1
    if x == len(modten_list):
        return True

def sixes(n):
    value = str(n)
    i = 2
    while i < 7:
        multiple = str(n * i)
        x = 0
        if len(multiple) != len(value):
            return False
        while x < len(multiple):
            if value[x] not in multiple:
                return False
            else:
                x += 1
        i += 1
    if i == 7:
        return True

def main():
    m = []
    for i in range(0, 10):
        m.append(remainders(i))

    for n in range(1, 1000000):
        value = str(n)
        digit = int(value[-1])
        if check(n, m[digit]) == True:
            if sixes(n) == True:
                print("The answer is ", n)

if __name__ == '__main__':
    main()
