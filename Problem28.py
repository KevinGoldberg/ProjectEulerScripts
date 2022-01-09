#Problem28

total = 1

for i in range(1, 501):
    total = total + 4*((2*i) + 1)**2 - (12 * i)

print(total)
