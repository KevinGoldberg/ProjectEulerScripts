#Problem71

x = 2
y = 5

while x <= (1000000-3) and y <= (1000000-7):
    x += 3
    y += 7

print(x, y)
print(x/y < 3/7)

"""As d increases, we see a pattern; the closest value is (x+3)/(y+7)"""

