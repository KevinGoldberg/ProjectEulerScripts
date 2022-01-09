#Problem63

import math

#brute force:

def power(n):
    length = len(str(n))
    x = 2
    while x**length < n and x < 10:
        x += 1
    if x**length == n:
        return x
    else:
        return False

def check(x):
    l = []
    for i in range(1, 100):
        if len(str(x**i)) == i:
            l.append(i)
    return l


"""count = 0
for j in range(1, 100):
    if check(j) != []:
        print(j, check(j))
        for x in check(j):
            count += 1
print(count)"""

for x in range(1, 10):
    print(x, int(math.log10(10)//(math.log10(10) - math.log10(x))))
