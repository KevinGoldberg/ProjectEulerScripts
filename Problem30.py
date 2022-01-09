#Problem30

l = []

for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    for f in range(0, 10):
                        if int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)) == a**5+b**5+c**5+d**5+e**5+f**5:
                            l.append(int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)))
                    
print(l)
print(sum(l))
