#Problem37

import Problem46

def nopes(value):
    no = ['0', '2', '4', '5', '6', '8']
    value = str(value)
    for digit in value:
        if digit in no:
            return False
        
    return True

def truncate(n):
    l = [str(n)]
    value = str(n)
    for i in range(1, len(value)):
        l.append(value[i:])
        l.append(value[:i])
    l.sort()

    return l

def check(l, primes):
    x = 0
    result = True
    if l == []:
        return False
    while x < len(l) and result == True:
        result = (int(l[x]) in primes)
        if result == False:
            return False
        else:
            x += 1
    if x >= len(l):
        return True

def generate(digits):
    l = []
    for digit1 in digits:
        for digit2 in digits:
            l.append(int(str(digit1) + str(digit2)))
            for digit3 in digits:
                l.append(int(str(digit1)+str(digit2)+str(digit3)))
                for digit4 in digits:
                    l.append(int(str(digit1)+str(digit2)+str(digit3)+str(digit4)))
                    for digit5 in digits:
                        l.append(int(str(digit1)+str(digit2)+str(digit3)+str(digit4)+str(digit5)))
                        for digit6 in digits:
                            l.append(int(str(digit1)+str(digit2)+str(digit3)+str(digit4)+str(digit5)+str(digit6)))
                            
    l.sort()
    return l


#figure out a better way to build permutations than the brute force way above    

def main():
    
    primes = Problem46.prime_list(1000000)
    """
    print("done")
    for p in primes:
        if check(truncate(p), primes) == True:
            l.append(p)
    print(l)
    print(sum(l))
    """

    l = []
    
    permutations = generate([1, 2, 3, 5, 7, 9])
    for perm in permutations:
        if check(truncate(perm), primes) == True:
            l.append(perm)
        
    print(l)

    
        

if __name__ == '__main__':
    main()
