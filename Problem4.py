#Problem 4

#starts and ends in 9, so products end in 1/9 or 3/3

def palindrome(phrase_int):
    """Determines if the phrase is a palindrome"""
    phrase = str(phrase_int)
    if len(str(phrase)) == 1:
        return True
    if len(str(phrase)) == 2:
        if str(phrase[0]) == str(phrase[1]):
            return True
        else:
            return False
    if (str(phrase)[0] != str(phrase)[-1]):
        return False
    else:
        return palindrome(phrase[1:-1])

def main():
    l = []
    for i in range(901, 1000):
        s = str(i)
        if s[2] == '1' or s[2] == '3' or s[2] == '9':
            l.append(i)
    print(l)


    x = len(l) - 1
    while l[x] > 901:
        y = len(l) - 1
        while l[y] > 901:
            if palindrome(str(l[x] * l[y])) == True:
                print(l[x] * l[y])
                x = 1
                y = 1
            y = y - 1
        x = x - 1

if __name__ == '__main__':
    main()
