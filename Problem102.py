#Problem 102

""" Assume triangle abc works. Then each line intersects one axis at least once,
    but at most twice (I checked the file and no triangle has a vertex
    at the origin). Thus, it suffices to check if 0 lies between these
    intersections. Moreover, it suffices to check only one axis (otherwise,
    the triangle won't contain the origin).

"""

def slope(a, b):
    """a and b are coordinates. returns equation of line between a and b"""
    m = float((b[1] - a[1])/(b[0] - a[0]))
    b = a[1] - a[0] * m
    return (m, b)

def line_equation(a, b):
    if (a[0] < 0 < b[0]) or (b[0] < 0 < a[0]):
        return (slope(a, b))[1]
    else:
        return False

def unduplicated(l):
    m = []
    for item in l:
        if item not in m:
            m.append(item)
    return m

def contained(triangle):
    count = 0
    ab = line_equation(triangle[0], triangle[1])
    if ab == False:
        count += 1
    bc = line_equation(triangle[1], triangle[2])
    if bc == False:
        count += 1
    ac = line_equation(triangle[0], triangle[2])
    if ac == False:
        count += 1
    if count > 1:
        #this eliminates triangles that do not intersect anywhere with the axes
        return False
    else:
        #There are two intercepts. Find out if they surround the y axis.
        l = []
        for line in [ab, bc, ac]:
            if line != False:
                l.append(line)
        #print(l)
        l = unduplicated(l)
        if (l[0] < 0 < l[1]) or (l[0] > 0 > l[1]):
            return True
        else:
            return False
    

def main():
    #Create a list of tuples for each triangle
    with open("triangles.txt", 'r') as infile:
        coordinates = []
        for line in infile:
            l = line.split(',')
            m = []
            for i in range(0, 6, 2):
                m.append((int(l[i]), int(l[i+1])))
            coordinates.append(m)

    #Find the intersections with the x axis
    count = 0
    for j in range(0, len(coordinates)):
        #print(contained(coordinates[j]))
        if contained(coordinates[j]) == True:
            count += 1
    #print(count)
    print("Of the 1000 triangles,", count, "of them contain the origin")
    

if __name__ == '__main__':
    main()
