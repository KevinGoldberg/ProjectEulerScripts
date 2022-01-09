#Problem206

"""

30^2 => 900
*30^2 => (*00 + 30)^2 => (*^2)0000 + (*x3x2)000 + 900 => no effect on 900

10: 0 2 4 6 8 10
19: 1 3 5 7 9 19

"""

import math

def check(x):
    """Checks if x**2 fits the criteria of 1_2_3_4_5_6_7_8_9_0 """
    x = str(int(x)**2)
    if x[0] == '1' and x[2] == '2' and x[4] == '3' and x[6] == '4' and x[8] == '5' and x[10] == '6' and x[12] == '7' and x[14] == '8' and x[16] == '9' and x[18] == '0':
        return True
    else:
        return False

def check2(x):
    if len(str(x)) < 19:
        x = (19 - len(str(x))) * '*' + str(x)
    else:
        x = str(x)

    cursor = 0
    concealed_square = True
    while concealed_square == True:
        if x[cursor] != '*' and x[cursor] != str(cursor/2 + 1):
            concealed_square = False
        else:
            cursor += 2

    return concealed_square

def check3(x):
    if len(x) < 10:
        value = str(int(x)**2)[-(len(str(int(x))) + 1):]
        #print("The checked value is:", value, "The root is:", x)
    
        concealed_square = True
        cursor = -3
        digit = 9
        while concealed_square == True and abs(cursor) <= len(str(value)):
            #print(cursor, digit)
            if value[cursor] != str(digit):
                concealed_square = False
            else:
                digit -= 1
                cursor -= 2
        #print(concealed_square)
        return concealed_square
    
    else:
        return check(x)

def update_potential(value):
    #Each potential has to be extended two digits before being checked
    new = []
    l = [str(j)+str(i) for j in range(0, 10) for i in range(0, 10)]
    for pair in l:
        #print((pair + value), check3(str(pair + value)))
        if check3(str(pair + value)) == True:
            new.append(str(pair + value))
    return new

#---------------------------------------------------------------------

def main():
    """
    l = ['30']
    while len(l[-1]) < 19:
        print(l[0], l[len(l)//2], l[-1])
        m = []
        for potential in l:
            for new_value in update_potential(potential):
                m.append(new_value)
        l = m.copy()
        print(len(l), len(l[0]))

    print(l)
    """
    begin, end = int(math.sqrt(1020304050607080900)), int(math.sqrt(1929394959697989990))
    for x in range(begin, end, 10):
        if check(x) == True:
            print(x)

if __name__ == '__main__':
    main()
        
        
