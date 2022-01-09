#Problem92

def square_digits(n, d):
    original = n
    while n not in d:
        x = 0
        for i in range(0, len(str(n))):
            x += int(str(n)[i])**2
        n = x
    d[original] = d[n]
    return d


def main():
    counts = dict()

    counts[1] = 1
    counts[89] = 89

    for i in range(1, 10000000):
        square_digits(i, counts)

    print("done updating")

    count = 0
    for j in range(1, 10000000):
        if counts[j] == 89:
            count += 1
    print("The answer is ", count)


if __name__ == '__main__':
    main()
