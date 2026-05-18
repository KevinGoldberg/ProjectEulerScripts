#Problem 31

"""
Coin values: 1, 2, 5, 10, 20, 50, 100, 200

Solve recursively
"""

def currency_helper(n, m):
    if n==0:
        return 1
    
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    l = [x for x in coins if x <= m]
    
    #print(l)
    
    total = 0
    
    for i in l:
        if n-i >= 0:
            total += currency_helper(n-i, i)
    
    return total
    

def currency(n):
    return currency_helper(n, n)

print(currency(200))