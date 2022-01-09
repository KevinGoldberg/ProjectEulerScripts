#Problem43

def sub_string_divisible(x):
    """Returns True if the number is sub string divisible"""
    value = str(x)
    if int(value[1:4]) % 2 == 0:
        if int(value[2:5]) % 3 == 0:
            if int(value[3:6]) % 5 == 0:
                if int(value[4:7]) % 7 == 0:
                    if int(value[5:8]) % 11 == 0:
                        if int(value[6:9]) % 13 == 0:
                            if int(value[7:10]) % 17 == 0:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def pandigital(x, n):
    """Returns True if x is n digits pandigital and False otherwise"""
    value = str(x)
    if '0' not in value and len(value) < n:
        value = '0' + value
    count = 0
    while count < n:
        if str(count) in value:
            count += 1
        else:
            return False
    if count == n:
        return True

def permutations(n):
    """Returns a list of pandigital permutations of n digits that ends with
    a three digit number that is divisible by 17"""
    l = ['017', '034', '051', '068', '085']
    for i in range(100, 1000):
        value = str(i)
        if i % 17 == 0 and (value[0] != value[1] != value[2]):
            l.append(str(i))
    return l

def new_digit(x, p):
    l = []
    value = int(x[0:2])
    value = int(p - (value % p))
    for i in range(0, 1000, 100):
        if i % p == value % p:
            l.append(str(int(i/100)) + x)
    return l

def recursive_digit(l):
    """Recursively adds digits to each number of the list until 9 digits"""
    length = len(l[0])
    m = []
    p = [17, 13, 11, 7, 5, 3, 2]
    for number in l:
        new_values = new_digit(number, p[(length-2)])
        for new_number in new_values:
            m.append(new_number)
    if m == []:
        return m
    elif len(m[0]) == 9:
        return m
    else:
        return recursive_digit(m)
    
    
    
def main():
    m = []
    p = [13, 11, 7, 5, 3, 2]
    seventeen = permutations(10)
    nine_digits = recursive_digit(seventeen)
    #Add all possible 10 digits to front
    for value in nine_digits:
        for i in range(0, 9):
            m.append(str(i) + value)

    l = []
    for item in m:
        if pandigital(item, 10) == True:
            l.append(item)

    print(l)
    sum = 0
    for number in l:
        sum += int(number)
    print(sum)

if __name__ == '__main__':
    main()
