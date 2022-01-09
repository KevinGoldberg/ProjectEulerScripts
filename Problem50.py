#Problem50

import Problem46 as prime

print(prime.not_prime(17))

primes = prime.prime_list(1000000)
print("done computing")
print(len(primes))

"""
index = 0
length = 0
longest = False
longest_prime_chain = 0

while longest == False:
    total = sum(primes[index:index + length + 1])
    #print(length, total, index)
    if total in primes #or rabin_miller(total) == True:
        #print("This one should send it back to the top")
        index = 0
        length += 2
        longest_prime_chain = total
    else:
        index += 1
        
        if index == len(primes) - 1 - length:
            longest = True

print(longest_prime_chain)

#define the rabin miller function here and use it on primes > 1000000
"""

#Add the primes, starting at 2, until you have a longer chain or until
# you get to a sum above 1 million, then start from 3, then 5 etc.
"""
def primeSum(index, longest, limit):
    l = longest
    if len(primes) - index < longest:
        return longest
    total = 0
    for i in range(index, longest+index):
        total += primes[i]
    distance = 0 
    while total < limit: 
        total = total + primes[l+index+distance]
        if distance == 0:
            distance += 1
        if prime.not_prime(total) == False:
            l = l + distance
            distance = 0
            print("The prime is", total)
            a = 0
            for i in range(0, l):
                a += primes[index+i]
            print("It should be:", a, "Length:", l)
        distance += 1
    return l

x = 0
l = 1
while x < len(primes):
    if l != primeSum(x, l, 1000):
        l = primeSum(x, l, 1000)
        print("The length of the chain", l)
    x += 1

"""

def primeSum2(index, longest, limit):
    if len(primes) - index < longest:
        return longest
    total = 0
    for i in range(index, index+longest):
        total = total + primes[i]
    #At this point, total is the sum of the int(longest) primes, starting at
    # index

    #Add next prime, check to see if total is prime, update longest as needed
    l = longest
    distance = 0
    while total < limit:
        total = total + primes[index+l+distance]
        if prime.not_prime(total) == False:
            l = l + distance + 1
            distance = 0
            print(total)
        else:
            distance += 1
    return l


x = 0
l = 1
while x < len(primes):
    if l != primeSum2(x, l, 1000000):
        l = primeSum2(x, l, 1000000)
        print("The length of the chain", l)
    x += 1



