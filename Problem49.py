#Problem49

import Problem46 as prime


def digit_picker(x, n):
    """returns a list of the digits in n not included in x
    Note: The list entries are strings"""
    l = [str(n)[i] for i in range(0, len(str(n)))]
    for digit in str(x):
        if digit in l:
            l.remove(digit)
    return l

def permutations(n):
    """Returns a list of the permutations for a number (n)"""
    
    #isolate digits as both strings and  integers
    digits = [str(n)[i] for i in range(0, len(str(n)))]
    l = [int(str(n)[i]) for i in range(0, len(str(n)))]
    
    #generate the permuations by picking digits not already included
    while len(str(l[-1])) < len(str(n)):
        new_list = []
        for value in l:
            new_digits = digit_picker(value, n)
            for digit in new_digits:
                new_list.append(value * 10 + int(digit))
                
        l = new_list
    
    m = []
    for i in l:
        if i not in m:
            m.append(i)
    
    return m


def find_arithmetic_sequence(l):
    """Given a list, see if there is an arithmetic sequence of three numbers"""
    i = 1
    while i < len(l) - 1:
        abs_min_delta = []
        for j in l:
            if max(j-l[i], l[i]-j) not in abs_min_delta:
                abs_min_delta.append(max(j-l[i], l[i]-j))
                
            #if for a given value there are two numbers the same distance away
            # then this number is the middle of the arithmetic sequence
            else:
                m = [l[i]-max(j-l[i], l[i]-j), l[i], l[i]+max(j-l[i], l[i]-j)]
                return m
            
        i += 1
    
    return []
            


def main():
    primes = prime.prime_list(9999)
    print("done") 
    
    #l is a list of the primes from 1000 to 9999 (~1061)
    l = []
    for p in primes:
        if p > 1000:
            l.append(p)
    
    m, r = [], []
    
    for i in range(0, len(l)):
        perms, perm_primes = permutations(l[i]), []
        for p in perms:
            if p in l:
                perm_primes.append(p)
        
        #candidates (~174 sets of permuations)
        if len(perm_primes) >= 3:
            min_perm = min(perm_primes)
            if min_perm not in m:
                check = find_arithmetic_sequence(perm_primes)
                if len(check) > 0:
                    r.append(check)
                m.append(min_perm)
    
    for i in r:
        print("Sequence: ", i, "Concat :", str(i[0])+str(i[1])+str(i[2]))

if __name__ == '__main__':
    main()
