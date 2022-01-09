#Problem 11

def grid_list(file):
    """Opens a file (of integers) and makes a usable grid in list of lists
    format."""
    l = []
    with open(file) as infile:
        for line in infile:
            m = []
            numbers = line.split()
            
            #add every two digits as a list item
            for i in range(0, len(numbers)):
                m.append(int(numbers[i]))
                
            #make the list of lists
            l.append(m)
    return l

def max_product(l):
    """ Reads a table (in list of list format) and determines the maximum
    product of four adjacent numbers in any direction."""
    max_val = 0
    
    #calculate each product (down, right and diagonal) from top left corner
    #Left-Right
    for i in range(0, len(l)):
        for j in range(0, len(l[i]) - 3):
            value = l[i][j] * l[i][j+1] * l[i][j+2] * l[i][j+3]
            if value > max_val:
                max_val = value


    #Top-Bottom
    for i in range(0, len(l) - 3):
        for j in range(0, len(l[i])):
            value = l[i][j] * l[i+1][j] * l[i+2][j] * l[i+3][j]
            if value > max_val:
                max_val = value

    
    #Diagonal \
    for i in range(0, len(l) - 3):
        for j in range(0, len(l[i]) - 3):
            value = l[i][j] * l[i+1][j+1] * l[i+2][j+2] * l[i+3][j+3]
            if value > max_val:
                max_val = value

    
    #Diagonal /
    for i in range(4, len(l)):
        for j in range(0, len(l[i]) - 3):
            value = l[i][j] * l[i-1][j+1] * l[i-2][j+2] * l[i-3][j+3]
            if value > max_val:
                max_val = value

    return max_val

def main():
    grid = grid_list("number_grid1.txt")
    print(grid)
    print(max_product(grid))

if __name__ == '__main__':
    main()
