#Problem35

import Problem46

def rotate(phrase, rotations):
    return phrase[rotations:] + phrase[0:rotations]

def permutate(x):
    """Returns a list of the rotated strings"""
    m = []
    number = str(x)
    for i in range(1, len(number)):
        m.append(rotate(number, i))
    return m

def circular(p, primes):
    #check to see if there's any easy disqualifiers for primes
    value = str(p)
    nopes = ['2', '4', '5', '6', '8', '0']
    for n in nopes:
        if n in value and p > 10:
            return False
    x = 0
    l = permutate(p)
    is_prime = True
    while is_prime == True and x < len(l):
        if int(l[x]) not in primes:
            is_prime = False
        else:
            x += 1
    if is_prime == True:
        return True
    else:
        return False

def main():
    primes = Problem46.prime_list(1000000)
    count = 0
    for p in primes:
        if circular(p, primes) == True:
            count += 1
            print(p)
    print("The answer is ", count)
    
if __name__ == '__main__':
    main()
