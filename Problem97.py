#Problem97

def mods(x, n):
    for i in range(0, n-1):
        x = x * 2 % 10000000000
    return x

answer = (mods(2, 7830457) * 28433 + 1) % 10000000000
print(answer)
