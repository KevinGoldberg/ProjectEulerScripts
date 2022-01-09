#Problem42

def triangular(x):
    n = 1
    while int(n * (n+1) * (1/2)) < x:
        n += 1
    if int(n * (n+1) * (1/2)) == x:
        return True
    else:
        return False

def letter_values(word, dictionary):
    value = 0
    for letter in word:
        value += dictionary[str(letter)]
    return value

def main():
    letters = dict()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(1, 27):
        letters[alphabet[i-1]] = int(i)
    
    with open("triangular_words.txt", 'r') as infile:
        l = []
        count = 0
        for text in infile:
            text = text.replace(',', ' ')
            text = text.replace('"', ' ')
            words = text.lower()
            words = words.split()
            for word in words:
                phrase = ''
                for letter in word:
                    if letter.isalpha() == True:
                        phrase += str(letter)
                if triangular(letter_values(phrase, letters)) == True:
                    count += 1

    print(count)

if __name__ == '__main__':
    main()
