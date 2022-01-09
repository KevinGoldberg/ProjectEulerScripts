#Problem17

def letter_length(end):
    ones = ['and', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']
    count = 0
    for x in range(1, end):
        i = x % 100
        if 0 < i <= 10:
            count = count + len(ones[i])
        elif 10 < i < 20:
            count = count + len((teens)[i-11])
        elif 20 <= i < 100:
            if i%10 == 0:
                count = count + len(tens[(int(str(i)[0])-2)])
            else:
                count = count + len(tens[(int(str(i)[0])-2)]) + len(ones[i%10])
        if 1000 > x >= 100:
            y = x//100
            if x % 100 == 0:
                count = count + len(tens[8]) + len(ones[y])
            else:
                count = count + len(tens[8]) + len(ones[y]) + len(ones[0])
        if x == 1000:
            count = count + 11
    return count

def main():
    print(letter_length(1001))

if __name__ == '__main__':
    main()
