#Problem57

m, n = 3, 2

count = 0
expansion = 1
while expansion < 1000:
    expansion += 1
    m, n = m + 2*n, m + n
    if len(str(m)) > len(str(n)):
        count += 1

print(count)
    
