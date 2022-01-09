#Problem 112: Bouncy numbers

def isIncreasing(n):
    number = str(n)
    increasing = True
    x = 0

    while x < len(number) - 1 and increasing == True:
        if int(number[x+1]) >= int(number[x]):
            x+=1
        else:
            return False
    return True


def isDecreasing(n):
    number = str(n)
    increasing = True
    x = 0

    while x < len(number) - 1 and increasing == True:
        if int(number[x+1]) <= int(number[x]):
            x+=1
        else:
            return False
    return True

def isBouncy_check(n):
    if isIncreasing(n) == True or isDecreasing(n) == True:
        return False
    else:
        return True

def isBouncy_DictionaryCheck(n, d):
    if d[int(str(n)[1:])] == True:
        return True
    else:
        return isBouncy_check(n)
    

def main():

    #print(110, isBouncy_check(110))

    #print(110, isDecreasing(110))

    isBouncy_Dictionary = dict()
    for i in range(0, 101):
        isBouncy_Dictionary[i] = False

    count, total = 0, 100

    while (count/total) * 100 != 99:
        total += 1

        isBouncy = isBouncy_DictionaryCheck(total, isBouncy_Dictionary)
        isBouncy_Dictionary[total] = isBouncy

        if isBouncy == True:
            count += 1


        #print(count, total, count/total * 100)
        #"""
        if total == 21780:
            print(count, total, count/total * 100)
        if total == 538:
            print(count, total, count/total * 100)
        if total == 999:
            print(count, total, count/total * 100)
        if total == 9999:
            print(count, total, count/total * 100)
        #"""

        if total % 10000000 == 0:
            print(count, total, count/total * 100)
            
    print(count, total, count/total * 100)
    
if __name__ == '__main__':
    main()
