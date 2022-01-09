#Problem19

#sunday = 6

x = 2
count = 0

for i in range(1, 101):
    if i % 4 == 0:
        february = 29
    else:
        february = 28
    for j in range(0, 12):
        if j == 1:
            #month is february
            x = x + february
        elif j == 0 or j == 2 or j == 4 or j == 6 or j == 7 or j == 9 or j == 11:
            x = x + 31
        else:
            x = x + 30
        if x % 7 == 6:
            count += 1

print(count)


