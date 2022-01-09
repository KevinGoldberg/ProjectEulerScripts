#Problem79


with open("keylog.txt") as infile:
    l = []
    for line in infile:
        l.append(int(str(line)))


#l is a list of the successful passcodes

def translate(passcode, index):
    return int(str(passcode)[index])

def potential(passcode, dictionary):
    for digit in [translate(passcode, 1), translate(passcode, 2)]:
        if digit not in dictionary[translate(passcode, 0)]:
            new_list = dictionary[translate(passcode, 0)]
            new_list.append(digit)
            dictionary[translate(passcode, 0)] = new_list
    return dictionary

def second_place_update(passcode, dictionary):
    if translate(passcode, 1) in dictionary:
        if translate(passcode, 2) not in dictionary[translate(passcode, 1)]:
            new_list = dictionary[translate(passcode, 0)]
            new_list.append(translate(passcode, 2))
            dictionary[translate(passcode, 0)] = new_list
    else:
        dictionary[translate(passcode, 1)] = [translate(passcode, 2)]
    return dictionary

def third_place_update(passcode, dictionary):
    if translate(passcode, 2) not in dictionary:
        dictionary[translate(passcode, 2)] = []


def update(passcode, dictionary):
    if translate(passcode, 0) in dictionary:
        #update the potential new numbers
        potential(passcode, dictionary)
    else:
        #make a new dictionary entry with the two number the new value precedes
        dictionary[translate(passcode, 0)] = [translate(passcode, 1), translate(passcode, 2)]
    
    return dictionary


sizes = dict()

for passcode in l:
    update(passcode, sizes)
for passcode in l:
    second_place_update(passcode, sizes)
for passcode in l:
    third_place_update(passcode, sizes)

print(sizes)

m = []
for entry in sizes:
    m.append([entry, len(sizes[entry])])

print(m)
answer = []
x = len(m)
while x >= 0:
    for pair in m:
        if pair[1] == x:
            print(pair[0], end = '')
    x -= 1


    
    
