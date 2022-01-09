#Problem 18

def read_triangle(text_name):
    """Opens text file and interprets the triangle"""
    with open(text_name, 'r') as infile:
        triangle = []
        for line in infile:
            #Makes strings, not integers
            l = line.split()
            
            triangle.append(l)
    return triangle

def make_integer_list(l):
    """transforms the strings in the list of lists (triangle) into integers"""
    m = []
    for string in l:
        m.append(int(string))
    return m

def make_triangle(text_name):
    """calls make_integer_list and read_triangle into action"""
    m = read_triangle(text_name)
    triangle = []
    for l in m:
        triangle.append(make_integer_list(l))
    return triangle

def new_line(high_values, triangle):
    """Updates the last line in the trianlge by adding the larger value of the
    two it precedes"""
    for i in range(0, len(high_values)):
        triangle[len(high_values)-1][i] += high_values[i]
    return triangle
            

def update_triangle(triangle):
    """Adds the new_line to the second to last line and deletes the last line"""
    last_line = triangle[len(triangle)-1]
    high_values = []
    for i in range(0, len(last_line) - 1):
        high_values.append(max([last_line[i], last_line[i+1]]))
    triangle = new_line(high_values, triangle)
    triangle.remove(last_line)
    return triangle

def max_sum(text_name):
    """interprets the triangle by calling make_triangle and returns the max sum
    by updating the triangle"""
    l = make_triangle(text_name)
    while len(l) > 1:
        update_triangle(l)
    return l[0][0]
    

def main():
    print("The max sum of the triangle is", max_sum("triangle.txt"))
    

if __name__ == '__main__':
    main()
