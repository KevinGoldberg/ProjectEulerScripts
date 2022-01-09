#Problem15

def pascal(rows):
    l = [[1], [1,1]]
    for i in range(1, rows):
        m = [1]
        for j in range(1, len(l[i])):
            m.append(l[i][j-1] + l[i][j])
        m.append(1)
        l.append(m)

    return l

def binomial(top, bottom):
    triangle = pascal(top)
    index = len(triangle[top]) - 1 - bottom
    return triangle[top][index]

def main():
    print(binomial(40, 20))

if __name__ == '__main__':
    main()
