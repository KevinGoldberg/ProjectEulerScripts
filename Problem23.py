#Problem23

import Problem3

l = []
m = []
n = []

count = 0
for i in range(0, 28123):
    count += i
    factors = Problem3.products(i)
    total = 0
    for value in factors:
        total += value
    if total > i:
        l.append(i)

for x in l:
    for y in l:
        m.append(x + y)

for a in range(0, 28123):
    if a not in m:
        n.append(a)
print(sum(n))
