#Problem 74

import math

"""
The length of a chain for a value in the sequence found after the repeated value
is the same length of a chain for the repeated value. 
"""

def factorial(n):
    total = 0
    for digit in str(n):
        total += math.factorial(int(digit))
    return total

def check_repeat(l):
    m = []
    for item in l:
        if item not in m:
            m.append(item)

    return len(m)

def chain_dictionary_update(n, dictionary):
    l = [n]
    x = factorial(n)
    while len(l) == check_repeat(l) and l[-1] not in dictionary:
        l.append(factorial(l[-1]))

    print(n, l, l[-1])
    if l[-1] in dictionary:
        #remove the last entry in the list and save as variable

        print("dictionary:", n, dictionary[n])

        #There's a problem here 
        repeat = l.pop()
        for i in range(0, len(l)):
            dictionary[l[i]] = dictionary[repeat] + len(l) - i - 1
    else:
        #The cycle is in the list itself
        print("balls")
        y = 0
        while l[y] != x:
            dictionary[l[y]] = len(l) - y
            y += 1
        for j in range(y, len(l)):
            dictionary[l[j]] = len(l) - y

    return dictionary

def chain_dictionary_update2(n, dictionary):
    l = [n]
    new_value = n
    repeat = False
    while repeat == False and l[-1] not in dictionary:
        new_value = factorial(l[-1])
        if new_value in l or new_value in dictionary:
            repeat = True
        l.append(new_value)

    location = l.index(new_value)
    
    if new_value not in dictionary:
        for i in range(location, len(l)-1):
            dictionary[l[i]] = len(l)-1 - location
            
    for j in range(0, location):
        dictionary[l[j]] = dictionary[l[location]] + location - j

    return dictionary
        

import time

def main():

    start = time.clock()
    
    chain_counts = dict()
    l = []
    
    for i in range(1, 1000000):
        chain_dictionary_update2(i, chain_counts)
        if chain_counts[i] == 60:
            l.append(i)
    t = time.clock() - start

    print(chain_counts[69])
    print(len(l))
    print(t)
    
if __name__ == '__main__':
    main()
    
    
