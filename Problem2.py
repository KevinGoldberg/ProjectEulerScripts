#Problem 2

l = [1, 2]

x = 0
y = 1

while (l[x] + l[y]) <= 4000000:
    l.append(l[x] + l[y])
    x = x + 1
    y = y + 1


sum = 0
for i in l:
    if i % 2 == 0:
        sum = sum + i
print(sum)
