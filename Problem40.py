#Problem40

s = ''

for i in range(0, 1000005):
    s += str(i)

value = int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])
print(value)
