#Problem 9

#answer is [200, 375, 425]

def pythagorean_list(start, end):
    """Returns a list of all pythagorean triples with
    start < a < b and c < end"""
    a = start
    b = start
    c = start
    l = []
    for i in range(0, end):
        b = 4
        for j in range(0, end):
            c = 3
            for k in range(0, end):
                if a**2 + b**2 == c**2 and a < b:
                    l.append([a, b, c])
                
                c = c + 1
            b = b + 1
        a = a + 1

    return l

def main():
    list = pythagorean_list(200, 500)
    print(list)
    for triple in list:
        if triple[0] + triple[1] + triple[2] == 1000:
            print(triple)

if __name__ == '__main__':
    main()
