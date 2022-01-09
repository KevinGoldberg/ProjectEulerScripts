#Problem53

import math

def combinatoric(n, r):
    return int(math.factorial(n)/(math.factorial(r) * math.factorial(n-r)))

#Equal to Pascal's Triangle
count = 0
for j in range(1, 101):
    l = []
    for i in range(1, j):
        if combinatoric(j, i) > 1000000:
            count += 1
print(count)
