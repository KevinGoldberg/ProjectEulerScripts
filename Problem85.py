#Problem85

"""
In looking at a grid of length = n and width = 1, we see that the potential
for any sized rectangle (x,y) is 1<=x<=n is n-x rectangles. Thus, if we look
at a 5x1 grid, there are
    - 5 possible 1x1 rectangles
    - 4 possible 2x1 rectangles
    - 3 possible 3x1 rectangles   =>   5+4+3+2+1 = 5*(5+1)/2
    - 2 possible 4x1 rectangles                  = 5th triangular number
    - 1 possible 5x1 rectangle

If we look at a grid of legnth = n and width = m != 1, we can see by the same
principle that if there are n*(n+1)/2 possible rectangles in each row,
then there are
    - m * n*(n+1)/2 rectangles (width = 1)
    - (m-1) * n*(n+1)/2 rectangles (width = 2)
    - (m-2) * n*(n+1)/2 rectangles (width = 3)
    - . . .                                      
    - 2 * n*(n+1)/2 rectangles (width = m-1)
    - 1 * n*(n+1)/2 rectangles (width = m)

=> (m + m-1 + m-2 + ... + 2 + 1) * n*(n+1)/2 = (m*(m+1)/2)*(n*(n+1)/2)
=>                                           = (m*(m+1)*n*(n+1)/4)
"""
import time

def space_determination(length, l):
    return length+1-l

def rectangle_counter(length, width):
    """This function goes the long way, where it adds n+n-1+...+1 and multiplies
    this value by m+m-1+..+1"""
    count = 0
    l, w = 1, 1
    for i in range(w, width+1):
        for j in range(l, length+1):
            count += space_determination(length, j) * space_determination(width, i)
    return count

def rectangle_counter_triangular(length, width):
    """Uses the triangular number principle shown above instead of computing
    the potential rectangles for each sized row"""
    return (length*(length+1)*width*(width+1))/4

def main():
    #Determine which grid is the closest to 2 million

    start = time.clock()
    difference = 2000000
    location = [1, 1]
    for i in range(1, 100):
        for j in range(1, 100):
            if abs(2000000 - rectangle_counter_triangular(i, j)) < difference:
                difference = abs(2000000 - rectangle_counter(i, j))
                location = [i, j]
                #print(difference, i, j, sep = '\t')
    t = time.clock() - start

    print("Final value:", difference, "at", location)
    print(location[0]*location[1])
    print(t, "seconds")
    


    

if __name__ == '__main__':
    main()
