#Problem22

def alphabet():
    string = 'abcdefghijklmnopqrstuvwxyz'
    alpha = dict()
    for i in range(0, 26):
        alpha[string[i]] = i+1
    return alpha

def letter_score(name, dictionary):
    count = 0
    for letter in name:
        if letter.isalpha() == True:
            count += dictionary[letter]
    return count

with open("names.txt", 'r') as infile:
    #strip the punctuation
    l = []
    for line in infile:
        l.append(line.split(','))
    m = []
    for name in l[0]:
        m.append(name.lower())
    m.sort()

    total = 0

    for i in range(0, len(m)):
        total += (i+1)*(letter_score(m[i], alphabet()))
    print("The answer is", total)


    
                
    #split into a list of the names
    #order the list
    #compute scores and total them
