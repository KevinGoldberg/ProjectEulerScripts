#Problem14

def sequence_length(n):
    count = 1
    while n != 1:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        count += 1
    return count

def update(x, dictionary):
    count = 0
    n = x
    while n not in dictionary:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        count += 1
    #At this point the n is in the dictionary
    count += dictionary[n]

    #Add x to dictionary
    dictionary[x] = count

    return dictionary

def main():
    counts = dict()
    counts[1] = 1
    for i in range(1, 1000000):
        update(i, counts)

    print("done")

    n, m = 1, 1
    for j in range(1, 1000000, 2):
        if counts[j] > m:
            n = j
            m = counts[j]
    print(n)

if __name__ == '__main__':
    main()
