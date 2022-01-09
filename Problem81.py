#Problem81

def interpret_grid(file):
    """Returns a list of lists that represents the grid: the inner lists are
    rows."""
    l = []
    with open(file, 'r') as infile:
        for line in infile:
            cursor = 0
            value = ''
            m = []
            while cursor != len(line):
                if line[cursor] != ',':
                    value += str(line[cursor])
                else:
                    m.append(int(value))
                    value = ''
                cursor += 1
            m.append(int(value))
            l.append(m)
    return l

def update(grid, row):
    x, y = row+1, 0
    while x >= 0:
        if y == 0:
            grid[y][x] += grid[y][x-1]
        elif x == 0:
            grid[y][x] += grid[y-1][x]
        else:
            grid[y][x] += min(grid[y-1][x], grid[y][x-1])
        x -= 1
        y += 1
    return grid

def update_second_half(grid, row):
    x, y = len(grid)-1, row - len(grid) + 1
    while x > row-len(grid):
        #print(row, x, y, grid[y][x], grid[y-1][x], grid[y][x-1])
        grid[y][x] += min(grid[y-1][x], grid[y][x-1])
        x -= 1
        y += 1
    return grid


import random
        
def min_sum(file):
    grid = interpret_grid(file)
    """
    l = []
    m = [131, 673, 234, 103, 18]
    l.append(m)
    m = [201, 96, 342, 965, 150]
    l.append(m)
    m = [630, 803, 746, 422, 111]
    l.append(m)
    m = [537, 699, 497, 121, 956]
    l.append(m)
    m = [805, 732, 524, 37, 331]
    l.append(m)

    grid = l
    for chain in grid:
        print(chain)
    print(' ')
    """
    row = 0
    while row < len(grid)-1:
        grid = update(grid, row)
        row += 1
    row += 1
    while row < 2*len(grid):
        grid = update_second_half(grid, row)
        row += 1

    return grid[-1][-1]

def main():
    print(min_sum("matrix1.txt"))

if __name__ == '__main__':
    main()
