#Problem56

def sum_digits(n):
    x = 0
    for i in range(0, len(str(n))):
        x += int(str(n)[i])
    return x

m = 0

for a in range(1, 100):
    for b in range(1, 100):
        if sum_digits(a**b) > m:
            m = sum_digits(a**b)

print(m)

            
