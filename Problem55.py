#Problem55

import time

def palindrome(n):
    reverse = ''
    for i in range(1, len(str(n))+1):
        reverse += str(n)[len(str(n))-i]
    if reverse == str(n):
        return True
    else:
        return False

def palindrome2(n):
    for i in range(0, len(str(n))//2):
        if str(n)[i] != str(n)[len(str(n))-i-1]:
            return False

    return True

"""
import time
import random

l = [random.randint(1, 10000000) for i in range(0, 1000)]

start = time.clock()
for x in l:
    palindrome(x)
end = time.clock()
time1 = end - start

start = time.clock()
for x in l:
    palindrome2(x)
end = time.clock()
time2 = end - start

print("1:", time1, "2:", time2, sep = '\t')
print(time1/time2)


Palindrome2 is faster since it fails earlier on. 
"""

def make_reverse(n):
    reverse = ''
    for i in range(1, len(str(n))+1):
        reverse += str(n)[len(str(n))-i]
    return int(reverse)

def reverse_add(n):
    return n + make_reverse(n)

def main():
    start = time.clock()

    m = []
    non_lychrel = dict()
    x = 10000
    count = 0
    while x >= 1:
        x -= 1
        n = reverse_add(x)
        l = [x, n]
        while len(l) < 50 and palindrome2(n) == False and n not in non_lychrel:
            n = reverse_add(n)
            l.append(n)
        if palindrome2(n) == True or n in non_lychrel:
            for value in l:
                non_lychrel[value] = 'T'
        else:
            m.append(x)
    t = time.clock() - start
    


    print(len(m))
    print(t, "seconds")

if __name__ == '__main__':
    main()
    
