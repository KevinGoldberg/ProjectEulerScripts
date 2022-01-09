#Problem25

def fib(n):
    """returns a list of the fibonacci numbers less than n"""
    l = [1,1]
    while l[-1] < n:
        l.append(l[-2] + l[-1])

    return l

def main():
    #1000 digits is 10**999
    l = (fib(10**999))
    i = l.index(l[-1])
    print(i + 1)
    
if __name__ == '__main__':
    main()
