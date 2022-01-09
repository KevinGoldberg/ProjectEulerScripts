#Problem48



total = 0
for i in range(1, 1001):
    total = total + (i**i) % 10000000000
total = total % 10000000000

print(total)
